#!/usr/bin/env python3
"""Publication-quality matplotlib defaults for ML paper figures.

Usage from a plotting script:

    import sys; sys.path.insert(0, "/path/to/ml-paper-writing/scripts")
    import matplotlib.pyplot as plt
    import paper_style as ps

    ps.use_paper_style()                                   # call once, before creating figures
    fig, ax = plt.subplots(figsize=ps.figsize("column", venue="icml"))
    fill, edge = ps.fill_edge("amber")                     # shade-400 fill, shade-600 outline
    ax.bar(["base", "base+cue"], [0.31, 0.58], color=[ps.color("neutral", 300), fill],
           edgecolor=[ps.color("neutral", 500), edge], linewidth=0.8)
    ps.save(fig, "figures/fig2_accuracy")                  # writes .pdf (+ .png preview) and checks fonts

Command line:

    python paper_style.py --palette              # print hue names and shades
    python paper_style.py --venues               # print venue widths
    python paper_style.py --demo OUT_DIR         # render a demo figure using the conventions
    python paper_style.py --check FIG.pdf        # warn about Type 3 fonts / embedded raster images

Design conventions encoded here (see references/figures.md for the reasoning):
  * One hue per condition across the whole paper; same shade level for comparable elements
    (400 fills, 600 outlines, 500-600 lines). Neutral gray for baselines / context.
  * Sans-serif labels (distinct from the serif body text), monospace for literal tokens/code.
  * Text sized for the final printed width (~7-9 pt), so design at the real column width.
  * Vector PDF export with TrueType (Type 42) fonts so text stays text and venues accept it.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from typing import Iterable, Sequence

import matplotlib

# Tailwind CSS v4 palette (defined in OKLCH), converted to sRGB hex. Hues x shades 50..950.
PALETTE = {
    "slate": {50: "#f8fafc", 100: "#f1f5f9", 200: "#e2e8f0", 300: "#cad5e2", 400: "#90a1b9", 500: "#62748e", 600: "#45556c", 700: "#314158", 800: "#1d293d", 900: "#0f172b", 950: "#020618"},
    "neutral": {50: "#fafafa", 100: "#f5f5f5", 200: "#e5e5e5", 300: "#d4d4d4", 400: "#a1a1a1", 500: "#737373", 600: "#525252", 700: "#404040", 800: "#262626", 900: "#171717", 950: "#0a0a0a"},
    "stone": {50: "#fafaf9", 100: "#f5f5f4", 200: "#e7e5e4", 300: "#d6d3d1", 400: "#a6a09b", 500: "#79716b", 600: "#57534d", 700: "#44403b", 800: "#292524", 900: "#1c1917", 950: "#0c0a09"},
    "red": {50: "#fef2f2", 100: "#ffe2e2", 200: "#ffc9c9", 300: "#ffa2a2", 400: "#ff6467", 500: "#fb2c36", 600: "#e7000b", 700: "#c10007", 800: "#9f0712", 900: "#82181a", 950: "#460809"},
    "orange": {50: "#fff7ed", 100: "#ffedd4", 200: "#ffd6a7", 300: "#ffb86a", 400: "#ff8904", 500: "#ff6900", 600: "#f54900", 700: "#ca3500", 800: "#9f2d00", 900: "#7e2a0c", 950: "#441306"},
    "amber": {50: "#fffbeb", 100: "#fef3c6", 200: "#fee685", 300: "#ffd230", 400: "#ffb900", 500: "#fe9a00", 600: "#e17100", 700: "#bb4d00", 800: "#973c00", 900: "#7b3306", 950: "#461901"},
    "yellow": {50: "#fefce8", 100: "#fef9c2", 200: "#fff085", 300: "#ffdf20", 400: "#fdc700", 500: "#f0b100", 600: "#d08700", 700: "#a65f00", 800: "#894b00", 900: "#733e0a", 950: "#432004"},
    "lime": {50: "#f7fee7", 100: "#ecfcca", 200: "#d8f999", 300: "#bbf451", 400: "#9ae600", 500: "#7ccf00", 600: "#5ea500", 700: "#497d00", 800: "#3c6300", 900: "#35530e", 950: "#192e03"},
    "green": {50: "#f0fdf4", 100: "#dcfce7", 200: "#b9f8cf", 300: "#7bf1a8", 400: "#05df72", 500: "#00c950", 600: "#00a63e", 700: "#008236", 800: "#016630", 900: "#0d542b", 950: "#032e15"},
    "emerald": {50: "#ecfdf5", 100: "#d0fae5", 200: "#a4f4cf", 300: "#5ee9b5", 400: "#00d492", 500: "#00bc7d", 600: "#009966", 700: "#007a55", 800: "#006045", 900: "#004f3b", 950: "#002c22"},
    "teal": {50: "#f0fdfa", 100: "#cbfbf1", 200: "#96f7e4", 300: "#46ecd5", 400: "#00d5be", 500: "#00bba7", 600: "#009689", 700: "#00786f", 800: "#005f5a", 900: "#0b4f4a", 950: "#022f2e"},
    "cyan": {50: "#ecfeff", 100: "#cefafe", 200: "#a2f4fd", 300: "#53eafd", 400: "#00d3f2", 500: "#00b8db", 600: "#0092b8", 700: "#007595", 800: "#005f78", 900: "#104e64", 950: "#053345"},
    "sky": {50: "#f0f9ff", 100: "#dff2fe", 200: "#b8e6fe", 300: "#74d4ff", 400: "#00bcff", 500: "#00a6f4", 600: "#0084d1", 700: "#0069a8", 800: "#00598a", 900: "#024a70", 950: "#052f4a"},
    "blue": {50: "#eff6ff", 100: "#dbeafe", 200: "#bedbff", 300: "#8ec5ff", 400: "#51a2ff", 500: "#2b7fff", 600: "#155dfc", 700: "#1447e6", 800: "#193cb8", 900: "#1c398e", 950: "#162456"},
    "indigo": {50: "#eef2ff", 100: "#e0e7ff", 200: "#c6d2ff", 300: "#a3b3ff", 400: "#7c86ff", 500: "#615fff", 600: "#4f39f6", 700: "#432dd7", 800: "#372aac", 900: "#312c85", 950: "#1e1a4d"},
    "violet": {50: "#f5f3ff", 100: "#ede9fe", 200: "#ddd6ff", 300: "#c4b4ff", 400: "#a684ff", 500: "#8e51ff", 600: "#7f22fe", 700: "#7008e7", 800: "#5d0ec0", 900: "#4d179a", 950: "#2f0d68"},
    "purple": {50: "#faf5ff", 100: "#f3e8ff", 200: "#e9d4ff", 300: "#dab2ff", 400: "#c27aff", 500: "#ad46ff", 600: "#9810fa", 700: "#8200db", 800: "#6e11b0", 900: "#59168b", 950: "#3c0366"},
    "fuchsia": {50: "#fdf4ff", 100: "#fae8ff", 200: "#f6cfff", 300: "#f4a8ff", 400: "#ed6aff", 500: "#e12afb", 600: "#c800de", 700: "#a800b7", 800: "#8a0194", 900: "#721378", 950: "#4b004f"},
    "pink": {50: "#fdf2f8", 100: "#fce7f3", 200: "#fccee8", 300: "#fda5d5", 400: "#fb64b6", 500: "#f6339a", 600: "#e60076", 700: "#c6005c", 800: "#a3004c", 900: "#861043", 950: "#510424"},
    "rose": {50: "#fff1f2", 100: "#ffe4e6", 200: "#ffccd3", 300: "#ffa1ad", 400: "#ff637e", 500: "#ff2056", 600: "#ec003f", 700: "#c70036", 800: "#a50036", 900: "#8b0836", 950: "#4d0218"},
}

# Typical LaTeX widths in inches. Always confirm with \the\columnwidth / \the\textwidth.
VENUE_WIDTHS = {
    "neurips": {"column": 5.5, "text": 5.5},
    "iclr": {"column": 5.5, "text": 5.5},
    "icml": {"column": 3.25, "text": 6.75},
    "acl": {"column": 3.03, "text": 6.30},
    "emnlp": {"column": 3.03, "text": 6.30},
    "naacl": {"column": 3.03, "text": 6.30},
    "cvpr": {"column": 3.25, "text": 6.875},
    "iccv": {"column": 3.25, "text": 6.875},
    "arxiv": {"column": 6.5, "text": 6.5},
}

SANS_FALLBACKS = ["Inter", "Source Sans 3", "IBM Plex Sans", "Helvetica Neue", "Helvetica", "Arial",
                  "Liberation Sans", "DejaVu Sans"]
MONO_FALLBACKS = ["B612 Mono", "JetBrains Mono", "IBM Plex Mono", "Menlo", "Liberation Mono", "DejaVu Sans Mono"]

# Hues ordered for maximum separation when assigning conditions automatically.
# Neutral is reserved for baselines/context; red and green are not placed next to each other.
DISTINCT_HUES = ["amber", "blue", "red", "teal", "violet", "orange", "sky", "pink", "lime", "indigo"]


def color(hue: str, shade: int = 500) -> str:
    """Hex color for a palette hue and shade, e.g. color("amber", 400)."""
    try:
        return PALETTE[hue][shade]
    except KeyError as exc:
        raise KeyError(f"Unknown color {hue}-{shade}. Hues: {', '.join(PALETTE)}; shades 50,100..900,950") from exc


def lightness(hex_color: str) -> float:
    """Perceived lightness CIE L* (0 = black, 100 = white) of a hex color.

    Emphasis should survive greyscale: keep roughly 15+ L* between the key condition and its neighbors.
    """
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    y = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    return round(116 * y ** (1 / 3) - 16 if y > 0.008856 else 903.3 * y, 1)


def fill_edge(hue: str, fill_shade: int = 400, edge_shade: int = 600) -> tuple[str, str]:
    """(fill, edge) pair for bars/markers: a light fill with a darker outline of the same hue."""
    return color(hue, fill_shade), color(hue, edge_shade)


def condition_colors(conditions: Sequence[str], hues: dict[str, str] | None = None,
                     baseline: Iterable[str] = (), focus: Iterable[str] = ()) -> dict[str, dict[str, str]]:
    """Map each condition name to {'hue','fill','edge','line','light'} colors.

    Hue carries identity; lightness carries emphasis:
      * `baseline` conditions: neutral, light (fill neutral-200)        -> recede
      * other conditions:      their hue at shade 400 (or 300 if a focus exists)
      * `focus` conditions:    their hue at shade 600 (fill), 800 (edge) -> clearly darker
    so the key condition stands out in greyscale too. Pin `hues` once per paper and reuse it
    in every figure so a condition keeps its color everywhere. Check with lightness().
    """
    hues = dict(hues or {})
    baseline, focus = set(baseline), set(focus)
    free = [h for h in DISTINCT_HUES if h not in hues.values()]
    other_shade = 300 if focus else 400
    out = {}
    for name in conditions:
        if name in baseline:
            out[name] = {"hue": "neutral", "fill": color("neutral", 200), "edge": color("neutral", 500),
                         "line": color("neutral", 400), "light": color("neutral", 100)}
            continue
        hue = hues.get(name) or (free.pop(0) if free else "slate")
        hues[name] = hue
        if name in focus:
            out[name] = {"hue": hue, "fill": color(hue, 600), "edge": color(hue, 800),
                         "line": color(hue, 600), "light": color(hue, 200)}
        else:
            out[name] = {"hue": hue, "fill": color(hue, other_shade), "edge": color(hue, other_shade + 200),
                         "line": color(hue, other_shade + 200), "light": color(hue, 100)}
    return out


def focus_kwargs(hue: str = "amber", lw: float = 2.0) -> dict:
    """Line kwargs for the series the reader should look at."""
    return {"color": color(hue, 600), "linewidth": lw, "zorder": 3}


def context_kwargs(lw: float = 1.0, alpha: float = 0.9) -> dict:
    """Line kwargs for supporting/context series that should recede."""
    return {"color": color("neutral", 300), "linewidth": lw, "alpha": alpha, "zorder": 1}


def _truetype_families() -> tuple[set[str], set[str]]:
    """(families installed as .ttf/.ttc, families installed only as other formats such as .otf)."""
    from matplotlib import font_manager
    ttf, other = set(), set()
    for f in font_manager.fontManager.ttflist:
        (ttf if f.fname.lower().endswith((".ttf", ".ttc")) else other).add(f.name)
    return ttf, other - ttf


def _usable(candidates: Sequence[str]) -> list[str]:
    """Installed TrueType families from `candidates`, in order.

    Fonts installed only as .otf (CFF outlines) are skipped: matplotlib cannot embed them as
    TrueType (Type 42), so the PDF gets a font-type mismatch that some viewers and venue checkers
    reject. Install the .ttf build of a font (e.g. Inter's) if you want it.
    """
    ttf, otf_only = _truetype_families()
    for c in candidates:
        if c in otf_only:
            print(f"paper_style: skipping {c!r} (installed only as .otf; install the .ttf build to use it)",
                  file=sys.stderr)
    usable = [c for c in candidates if c in ttf]
    return usable or ["DejaVu Sans"]


def use_paper_style(font: str | None = None, mono: str | None = None, base_size: float = 8.0,
                    grid: bool = False) -> None:
    """Apply rcParams for paper figures. Call once before creating figures.

    `font` / `mono` put a preferred family first; it is used only if installed as TrueType.
    """
    sans = _usable(([font] if font else []) + SANS_FALLBACKS)
    monos = _usable(([mono] if mono else []) + MONO_FALLBACKS)
    matplotlib.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": sans,
        "font.monospace": monos,
        "font.size": base_size,
        "axes.titlesize": base_size + 1,
        "axes.titleweight": "bold",
        "axes.labelsize": base_size,
        "xtick.labelsize": base_size - 1,
        "ytick.labelsize": base_size - 1,
        "legend.fontsize": base_size - 1,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": color("neutral", 500),
        "axes.labelcolor": color("neutral", 800),
        "axes.linewidth": 0.6,
        "xtick.color": color("neutral", 600),
        "ytick.color": color("neutral", 600),
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "axes.grid": grid,
        "grid.color": color("neutral", 200),
        "grid.linewidth": 0.5,
        "axes.prop_cycle": matplotlib.cycler(color=[color(h, 500) for h in DISTINCT_HUES]),
        "lines.linewidth": 1.4,
        "lines.markersize": 4,
        "errorbar.capsize": 2,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "text.color": color("neutral", 800),
    })


def figsize(width: str | float = "column", venue: str = "icml", aspect: float = 0.62,
            height: float | None = None) -> tuple[float, float]:
    """(width, height) in inches. `width` is "column", "text", a fraction like 0.5 (of text width), or inches > 1."""
    widths = VENUE_WIDTHS.get(venue.lower())
    if widths is None:
        raise KeyError(f"Unknown venue {venue!r}. Known: {', '.join(VENUE_WIDTHS)}")
    if isinstance(width, str):
        w = widths[width]
    elif width <= 1:
        w = widths["text"] * width
    else:
        w = float(width)
    return (w, height if height is not None else w * aspect)


def label_line_end(ax, x, y, text: str, color_: str, dx: float = 4, **kw) -> None:
    """Direct label at the end of a line (often clearer than a legend)."""
    ax.annotate(text, xy=(x, y), xytext=(dx, 0), textcoords="offset points", va="center",
                color=color_, fontsize=matplotlib.rcParams["legend.fontsize"], **kw)


def check_pdf(path: str) -> list[str]:
    """Return warnings about Type 3 fonts or embedded raster images in a PDF."""
    with open(path, "rb") as fh:
        data = fh.read()
    warnings = []
    if re.search(rb"/Subtype\s*/Type3", data):
        warnings.append(f"{path}: contains Type 3 fonts (set rcParams['pdf.fonttype'] = 42; some venues reject Type 3).")
    n_img = len(re.findall(rb"/Subtype\s*/Image", data))
    if n_img:
        warnings.append(f"{path}: contains {n_img} raster image(s); fine for heatmaps/photos (imshow), "
                        "but lines and text should be vector. Consider rasterized=True only on dense scatter layers.")
    # pdffonts (poppler), when installed, also catches CFF/.otf fonts mis-embedded as TrueType.
    import shutil
    import subprocess
    if shutil.which("pdffonts"):
        proc = subprocess.run(["pdffonts", path], capture_output=True, text=True)
        if "Mismatch between font type and embedded font file" in proc.stderr or re.search(r"Type [01]C", proc.stdout):
            warnings.append(f"{path}: a font was embedded from an .otf (CFF) file under a TrueType label. "
                            "Use a .ttf font (paper_style.use_paper_style() does this automatically).")
    return warnings


def save(fig, path_stem: str, formats: Sequence[str] = ("pdf",), preview_png: bool = True,
         grayscale_preview: bool = True, quiet: bool = False) -> list[str]:
    """Save a figure as vector PDF plus PNG previews, then check the PDF.

    `path_stem` has no extension, e.g. "figures/fig2_accuracy". Writes `<stem>.pdf`, `<stem>.png`
    and `<stem>_gray.png` (greyscale preview: the key condition should still stand out).
    Returns written paths.
    """
    os.makedirs(os.path.dirname(path_stem) or ".", exist_ok=True)
    written = []
    for fmt in formats:
        p = f"{path_stem}.{fmt}"
        fig.savefig(p)
        written.append(p)
    png = f"{path_stem}.png"
    if preview_png and "png" not in formats:
        fig.savefig(png, dpi=200)
        written.append(png)
    if grayscale_preview and os.path.exists(png):
        try:
            from PIL import Image  # pillow ships with matplotlib
            gray = f"{path_stem}_gray.png"
            Image.open(png).convert("L").save(gray)
            written.append(gray)
        except Exception as exc:  # preview only; never block saving
            print(f"paper_style: greyscale preview skipped ({exc})", file=sys.stderr)
    for p in written:
        if p.endswith(".pdf"):
            for w in check_pdf(p):
                print("WARNING:", w, file=sys.stderr)
    if not quiet:
        print("saved:", ", ".join(written))
    return written


def _demo(out_dir: str) -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    use_paper_style()
    cc = condition_colors(["Base", "Base + cue", "RL"], hues={"Base + cue": "amber", "RL": "blue"},
                          baseline=["Base"])
    rng = np.random.default_rng(0)
    fig, (a, b) = plt.subplots(1, 2, figsize=figsize("text", venue="icml", aspect=0.32),
                               gridspec_kw={"wspace": 0.35})

    # (a) grouped bars: one message = the cue closes most of the gap to RL
    names = list(cc)
    vals = [0.31, 0.55, 0.61]
    errs = [0.02, 0.02, 0.015]
    a.bar(names, vals, yerr=errs, color=[cc[n]["fill"] for n in names],
          edgecolor=[cc[n]["edge"] for n in names], linewidth=0.8, width=0.62,
          error_kw={"ecolor": color("neutral", 600), "elinewidth": 0.8})
    for i, v in enumerate(vals):
        a.text(i, v + 0.035, f"{v:.0%}", ha="center", fontsize=7, color=color("neutral", 700))
    a.set_ylabel("pass@1")
    a.set_ylim(0, 0.75)
    a.set_title("(a) A one-token cue closes most of the gap", loc="left")

    # (b) focus vs. context lines with direct labels instead of a legend
    steps = np.arange(0, 201, 10)
    for k in range(4):
        b.plot(steps, 0.3 + 0.25 * (1 - np.exp(-steps / (60 + 25 * k))) + rng.normal(0, 0.004, steps.size),
               **context_kwargs())
    y_rl = 0.3 + 0.3 * (1 - np.exp(-steps / 70))
    y_cue = 0.55 + 0.08 * (1 - np.exp(-steps / 30))
    b.plot(steps, y_rl, **focus_kwargs("blue"))
    b.plot(steps, y_cue, **focus_kwargs("amber"))
    label_line_end(b, steps[-1], y_rl[-1] - 0.012, "RL", cc["RL"]["line"])
    label_line_end(b, steps[-1], y_cue[-1] + 0.012, "RL + cue", cc["Base + cue"]["line"])
    b.set_xlabel("RL steps")
    b.set_ylabel("pass@1")
    b.set_title("(b) Supplying the cue speeds up RL", loc="left")
    save(fig, os.path.join(out_dir, "demo_figure"))


def main(argv: Sequence[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--palette", action="store_true", help="print palette hues and shades")
    ap.add_argument("--venues", action="store_true", help="print venue column/text widths (inches)")
    ap.add_argument("--demo", metavar="OUT_DIR", help="render a demo figure into OUT_DIR")
    ap.add_argument("--check", metavar="PDF", nargs="+", help="check PDFs for Type 3 fonts / raster images")
    args = ap.parse_args(argv)
    if args.palette:
        for hue, shades in PALETTE.items():
            print(f"{hue:8s} " + " ".join(f"{s}:{h}" for s, h in shades.items()))
    if args.venues:
        for v, w in VENUE_WIDTHS.items():
            print(f"{v:8s} column={w['column']}in text={w['text']}in")
    if args.demo:
        _demo(args.demo)
    if args.check:
        problems = [w for p in args.check for w in check_pdf(p)]
        print("\n".join(problems) if problems else "OK: no Type 3 fonts or raster images found.")
    if not any([args.palette, args.venues, args.demo, args.check]):
        ap.print_help()


if __name__ == "__main__":
    main()
