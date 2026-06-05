---
name: fetch-paper
description: Fetch an arXiv paper from a URL, arXiv ID, or title — downloads the LaTeX source into refs/<Title>/ (stripped of fonts & videos, figures kept as AI context) and the PDF into papers/<Title> - <arxiv_id>.pdf. Use when the user wants to add a paper to refs/papers, "download this paper", "grab the latex source", or pastes an arxiv link to ingest.
version: 1.0.0
tags: [research, arxiv, papers, latex, context]
---

# Fetch Paper

Ingest an arXiv paper as both a **lean LaTeX-source context** (for you and other
AI agents to read) and a **PDF** (for humans). One command, two artifacts.

## When to use

- The user gives an arXiv URL, arXiv ID, or a paper title and wants it added.
- Phrases like "download this paper", "add to refs", "grab the latex source",
  "ingest this arxiv link".

## What it does

For input `<url | id | title>`:

1. **Determines the arXiv ID:**
   - **URL or ID** → taken directly, **no network lookup** (`/abs/2605.06548`,
     `2605.06548`, `arxiv:2605.06548v2` all work).
   - **Title** → the *only* case that queries the arXiv API (text→id), with
     429/503 backoff.
2. **Source** → `refs/<Title>/` — pulls `arxiv.org/e-print/<id>`, extracts the
   LaTeX bundle, then strips **heavy elements**: videos/animations
   (`.mp4 .mov .gif .webm …`) and font blobs (`.ttf .otf .tfm .woff …`).
   **Image & vector figures are kept** (`.png .jpg .pdf .eps .svg`) because
   graphs and architecture diagrams are valuable context. Text stays
   (`.tex .bib .bbl .sty …`).
3. **Names intelligently** by reading `\title{}` out of the downloaded source
   (handles `\includegraphics` logos, `\textcolor`, `\raisebox`, `\thanks`,
   `\texorpdfstring`, etc.). Falls back to the API title, then the ID.
4. **PDF** → `papers/<Title> - <arxiv_id>.pdf` (title first, then ID), from
   `arxiv.org/pdf/<id>`.

## Usage

Run from the directory that owns `refs/` and `papers/` (e.g. the project root):

```bash
python3 ~/.claude/skills/fetch-paper/fetch_paper.py "<url | id | title>"
```

Examples:

```bash
# By URL
python3 ~/.claude/skills/fetch-paper/fetch_paper.py "https://arxiv.org/abs/2407.12282"

# By bare ID (version optional)
python3 ~/.claude/skills/fetch-paper/fetch_paper.py 2510.17206

# By title
python3 ~/.claude/skills/fetch-paper/fetch_paper.py "Chip Placement with Diffusion Models"
```

### Flags

- `--refs DIR`     refs output dir (default `./refs`)
- `--papers DIR`   papers output dir (default `./papers`)
- `--source-only`  download/strip LaTeX source only, skip PDF
- `--pdf-only`     download PDF only, skip source
- `--yes`          suppress the candidate-disambiguation printout for title searches

## Agent guidance

- The script is **stdlib-only** (no pip installs) and idempotent — re-running
  overwrites the same paths.
- If `dangerouslyDisableSandbox` is needed for network access in this harness,
  use it; arXiv requires HTTPS (`http://export.arxiv.org` returns empty).
- A **URL/ID never calls the arXiv API** — only a bare-title input does. So
  prefer passing the URL or ID to avoid rate limits entirely.
- For a **title search**, the script prints the top match and any other
  candidates to stderr. If the resolved title looks wrong, show the candidates
  to the user and re-run with the correct URL/ID.
- To batch-ingest several papers, loop over inputs; arXiv is politely rate-
  limited, so add a short `sleep` between calls.

## Conventions

- refs folder name = sanitized official title (path separators removed).
- PDF name = `<Title> - <arxiv_id>.pdf` (no version suffix on the ID).
