#!/usr/bin/env python3
"""Fetch an arXiv paper's LaTeX source (stripped of heavy media) + PDF.

Given an arXiv URL, arXiv ID, or paper title, this:
  1. Determines the arXiv ID.
     - URL or ID input  -> taken directly, NO network lookup.
     - Title input      -> the ONLY case that queries the arXiv API (text->id).
  2. Downloads the LaTeX source bundle (arxiv.org/e-print/<id>) into <refs>/<Title>/
  3. Strips heavy elements (videos + fonts); image/PDF/vector figures are KEPT.
  4. Reads the paper title from the source (\\title{...}) to name everything.
  5. Downloads the PDF (arxiv.org/pdf/<id>) into <papers>/<Title> - <arxiv_id>.pdf

Stdlib only. Usage:
    python3 fetch_paper.py "<url | id | title>" [--refs DIR] [--papers DIR]
                                                 [--yes] [--source-only] [--pdf-only]
"""
from __future__ import annotations

import argparse
import gzip
import io
import os
import re
import shutil
import sys
import tarfile
import time
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

ARXIV_API = "https://export.arxiv.org/api/query"
UA = "Mozilla/5.0 (compatible; fetch-paper/1.1; +https://arxiv.org)"
ATOM = {"a": "http://www.w3.org/2005/Atom"}

# Heavy elements to remove from the source bundle.
# Keep figures (png/jpg/jpeg/pdf/eps/ps/svg) — graphs & architecture diagrams
# are valuable context. Drop videos/animations and font blobs.
DROP_EXT = {
    ".mp4", ".mov", ".avi", ".webm", ".mkv", ".m4v", ".wmv", ".flv", ".ogv", ".gif",
    ".ttf", ".otf", ".tfm", ".pfb", ".pfm", ".afm", ".woff", ".woff2", ".eot", ".vf",
}

ID_NEW = r"\d{4}\.\d{4,5}"          # 2605.26106
ID_OLD = r"[a-z\-]+(?:\.[A-Z]{2})?/\d{7}"  # cs/0309047


def http_get(url: str, timeout: int = 90, retries: int = 4) -> bytes:
    """GET with backoff on 429/503 (arXiv rate limiting)."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503):
                wait = int(e.headers.get("Retry-After", 0)) or (5 * (attempt + 1))
                sys.stderr.write(f"  rate-limited ({e.code}); waiting {wait}s...\n")
                time.sleep(wait)
                continue
            raise
    raise last  # type: ignore[misc]


def extract_id(text: str):
    """Return (bare_id_no_version, is_explicit) for a url/id, else (None, False).

    is_explicit is True when the input clearly denotes an id (URL or pure id),
    meaning we should NOT do a title search.
    """
    text = text.strip()
    explicit = bool(
        re.search(r"arxiv\.org/(abs|pdf|src|e-print)/", text, re.I)
        or re.fullmatch(rf"(arxiv:)?({ID_NEW}|{ID_OLD})(v\d+)?", text, re.I)
    )
    m = re.search(rf"({ID_NEW}|{ID_OLD})(v\d+)?", text)
    if m:
        return m.group(1), explicit
    return None, False


# ---------------------------------------------------------------- title search
def api_title_search(query: str, assume_yes: bool):
    url = ARXIV_API + "?" + urllib.parse.urlencode(
        {"search_query": f'ti:"{query}"', "max_results": 5})
    root = ET.fromstring(http_get(url, timeout=30))
    res = []
    for e in root.findall("a:entry", ATOM):
        idurl = e.find("a:id", ATOM).text.strip()
        title = " ".join(e.find("a:title", ATOM).text.split())
        m = re.search(r"abs/(.+?)(v\d+)?$", idurl)
        res.append({"id": m.group(1) if m else idurl, "title": title})
    if not res:
        sys.exit(f"ERROR: no arXiv title match for: {query}")
    top = res[0]
    if not assume_yes and top["title"].lower() != query.strip().lower():
        sys.stderr.write(f"Top match: {top['id']}  {top['title']}\n")
        for r in res[1:]:
            sys.stderr.write(f"  alt: {r['id']}  {r['title']}\n")
    return top["id"], top["title"]


# ----------------------------------------------------------- title from source
def _grab_braced(s: str, i: int):
    """s[i] == '{' -> (inner_text, index_of_matching_close)."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j
    return s[i + 1:], len(s) - 1


def _apply_cmd(text: str, name: str, mode: str) -> str:
    """Rewrite every \\name with its [..]/{..} args.

    mode='drop'      -> remove command + all its args (e.g. \\includegraphics).
    mode='keep_last' -> replace with content of the LAST mandatory {..} arg
                        (e.g. \\textcolor{c}{t} -> t, \\raisebox{x}{y} -> y).
    """
    out, i = [], 0
    pat = re.compile(r"\\" + name + r"(?![a-zA-Z@])")
    while True:
        m = pat.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        j = m.end()
        mandatory = []
        while j < len(text):
            k = j
            while k < len(text) and text[k] in " \t":
                k += 1
            if k < len(text) and text[k] == "{":
                inner, close = _grab_braced(text, k)
                mandatory.append(inner)
                j = close + 1
            elif k < len(text) and text[k] == "[":
                depth = 0
                e = k
                for e in range(k, len(text)):
                    if text[e] == "[":
                        depth += 1
                    elif text[e] == "]":
                        depth -= 1
                        if depth == 0:
                            break
                j = e + 1
            else:
                break
        if mode == "keep_last" and mandatory:
            out.append(mandatory[-1])
        i = j
    return "".join(out)


def _remove_cmd_with_arg(text: str, cmd: str) -> str:
    return _apply_cmd(text, cmd, "drop")


def _clean_title(raw: str) -> str:
    raw = _remove_cmd_with_arg(raw, "thanks")
    raw = _remove_cmd_with_arg(raw, "footnote")
    raw = _remove_cmd_with_arg(raw, "includegraphics")  # logos in titles
    for c in ("textcolor", "raisebox", "scalebox", "resizebox",
              "colorbox", "fcolorbox", "texorpdfstring", "textsuperscript"):
        raw = _apply_cmd(raw, c, "keep_last")
    raw = raw.replace("\\\\", " ").replace("\n", " ")
    raw = re.sub(r"\\[a-zA-Z@]+\*?", " ", raw)  # strip remaining \commands
    raw = re.sub(r"\[[^\]]*\]", " ", raw)        # leftover optional args
    raw = raw.replace("{", " ").replace("}", " ")
    raw = re.sub(r"\s+", " ", raw).strip(" .,-")
    return raw


def _candidate_tex(ref_dir: str):
    """Ordered list of .tex paths likely to hold \\title{}."""
    order, seen = [], set()

    def add(p):
        if p and os.path.isfile(p) and p not in seen:
            seen.add(p)
            order.append(p)

    # 00README.json toplevel hint
    readme = os.path.join(ref_dir, "00README.json")
    if os.path.isfile(readme):
        try:
            import json
            for s in json.load(open(readme)).get("sources", []):
                if s.get("usage") == "toplevel":
                    add(os.path.join(ref_dir, s["filename"]))
        except Exception:
            pass
    for name in ("main.tex", "paper.tex", "arxiv.tex", "0_main.tex", "ms.tex", "root.tex"):
        add(os.path.join(ref_dir, name))
    for root, _d, files in os.walk(ref_dir):
        for f in sorted(files):
            if f.endswith(".tex"):
                add(os.path.join(root, f))
    return order


def title_from_source(ref_dir: str):
    for path in _candidate_tex(ref_dir):
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        # strip comments so commented-out \title lines are ignored
        text = re.sub(r"(?<!\\)%.*", "", text)
        for cmd in (r"\\icmltitle", r"\\title"):
            m = re.search(cmd + r"\s*(\[[^\]]*\])?\s*\{", text)
            if m:
                inner, _ = _grab_braced(text, m.end() - 1)
                cleaned = _clean_title(inner)
                if cleaned:
                    return cleaned
    return None


# ---------------------------------------------------------------- source / pdf
def download_source(aid: str, dest_dir: str) -> int:
    raw = http_get(f"https://arxiv.org/e-print/{aid}")
    os.makedirs(dest_dir, exist_ok=True)
    count = 0
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tar:
            for m in tar.getmembers():
                if not m.isfile():
                    continue
                name = m.name.lstrip("./")
                if name.startswith("/") or ".." in name.split("/"):
                    continue
                target = os.path.join(dest_dir, name)
                os.makedirs(os.path.dirname(target) or dest_dir, exist_ok=True)
                with tar.extractfile(m) as src, open(target, "wb") as out:
                    out.write(src.read())
                count += 1
    except tarfile.ReadError:
        try:
            content = gzip.decompress(raw)
        except OSError:
            content = raw
        with open(os.path.join(dest_dir, "main.tex"), "wb") as out:
            out.write(content)
        count = 1
    return count


def strip_heavy(dest_dir: str):
    removed, freed = [], 0
    for root, _d, files in os.walk(dest_dir):
        for f in files:
            if os.path.splitext(f)[1].lower() in DROP_EXT:
                p = os.path.join(root, f)
                freed += os.path.getsize(p)
                os.remove(p)
                removed.append(os.path.relpath(p, dest_dir))
    for root, _d, _f in os.walk(dest_dir, topdown=False):
        if root != dest_dir and not os.listdir(root):
            os.rmdir(root)
    return removed, freed


def sanitize(title: str) -> str:
    t = title.replace("/", "-").replace(":", " -")
    t = re.sub(r'[<>:"\\|?*]', "", t)
    return re.sub(r"\s+", " ", t).strip().rstrip(".")


def human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}TB"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="arXiv URL, arXiv id, or paper title")
    ap.add_argument("--refs", default="refs")
    ap.add_argument("--papers", default="papers")
    ap.add_argument("--yes", action="store_true")
    ap.add_argument("--source-only", action="store_true")
    ap.add_argument("--pdf-only", action="store_true")
    args = ap.parse_args()

    aid, explicit = extract_id(args.query)
    api_title = None
    if not explicit:  # title input -> the only API call
        aid, api_title = api_title_search(args.query, args.yes)
    if not aid:
        sys.exit(f"ERROR: could not determine arXiv id from: {args.query}")
    print(f"arXiv id: {aid}")

    # --- source (download to a temp id-named dir, then rename by parsed title)
    title = api_title
    ref_final = None
    if not args.pdf_only:
        tmp_dir = os.path.join(args.refs, f".incoming-{aid}")
        if os.path.isdir(tmp_dir):
            shutil.rmtree(tmp_dir)
        n = download_source(aid, tmp_dir)
        removed, freed = strip_heavy(tmp_dir)
        parsed = title_from_source(tmp_dir)
        title = parsed or api_title or aid
        ref_final = os.path.join(args.refs, sanitize(title))
        if os.path.abspath(ref_final) != os.path.abspath(tmp_dir):
            if os.path.isdir(ref_final):
                shutil.rmtree(ref_final)
            os.replace(tmp_dir, ref_final)
        kept = sum(os.path.getsize(os.path.join(r, f))
                   for r, _d, fs in os.walk(ref_final) for f in fs)
        print(f"title:    {title}" + ("" if parsed else "  (from API/id fallback)"))
        print(f"  source -> {ref_final}/  ({n} files, {len(removed)} heavy "
              f"removed / {human(freed)} freed, {human(kept)} kept)")
        if removed:
            print("  dropped: " + ", ".join(sorted(removed)[:12])
                  + (" ..." if len(removed) > 12 else ""))

    # --- pdf
    if not args.source_only:
        if title is None:  # pdf-only with id input and no source parsed
            _, title = api_title_search(args.query, True) if not explicit else (None, aid)
            title = title or aid
        os.makedirs(args.papers, exist_ok=True)
        pdf_path = os.path.join(args.papers, f"{sanitize(title)} - {aid}.pdf")
        data = http_get(f"https://arxiv.org/pdf/{aid}.pdf")
        if data[:5] != b"%PDF-":
            sys.exit(f"ERROR: downloaded PDF is invalid ({human(len(data))})")
        with open(pdf_path, "wb") as out:
            out.write(data)
        print(f"  pdf    -> {pdf_path}  ({human(len(data))})")


if __name__ == "__main__":
    main()
