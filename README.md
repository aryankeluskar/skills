# skills

[![skills.sh](https://skills.sh/b/aryankeluskar/skills)](https://skills.sh/aryankeluskar/skills)

Public collection of agent skills by [@aryankeluskar](https://github.com/aryankeluskar)

Install one with the [skills CLI](https://skills.sh):

```bash
npx skills add aryankeluskar/skills --skill <skill-name>
```

Or install all skills in this repo globally:

```bash
npx skills add aryankeluskar/skills -g --all
```

## Available skills

### [`add-umami-analytics`](./add-umami-analytics)

Add self-hosted [umami](https://umami.is) analytics plus automatic click/event tracking to any website — no manual tagging. Points at a self-hosted umami fork, creates a new website project, injects the tracking script, and wires detailed event tracking for every `<a>`, `<button>`, `role="button"`, and submit input.

- Auto-detects project type (Next.js App/Pages Router, static HTML, Vite/SPA) and injects the right snippet.
- Event name is the element's readable label (e.g. `link: Resume`); `href`, `id`, text, and path stored as properties.
- Includes a helper to create the umami website and return its ID, a React client component, and a vanilla HTML snippet.

Install:

```bash
npx skills add aryankeluskar/skills --skill add-umami-analytics
```

### [`brand-naming`](./brand-naming)

Generate brand, product, company, startup, app, AI agent, feature, or project name candidates — grounded in David Placek's (Lexicon Branding) methodology, the same process behind Sonos, Pentium, Blackberry, Powerbook, Swiffer, Vercel, Windsurf, CapCut, and Azure.

Two modes:
- **Quick** — one-shot generator, ~50 candidates across coined/compound/metaphor/cross-domain buckets with sound-symbolism rationales.
- **Full** — guided multi-phase workshop: Diamond exercise → disguised-brief generation → polarization/fluency screening → stakeholder-ready shortlist with prototypes.

Install:

```bash
npx skills add aryankeluskar/skills --skill brand-naming
```

### [`creativity-rejectionism`](./creativity-rejectionism)

Apply Henry Shevlin's "Strong Rejectionist" methodology (Shevlin 2021, EJPS) to claims that a non-human system — an animal or an AI/LLM — is "really creative" (or insightful, intelligent, understanding, reasoning). Instead of adjudicating the unanswerable "but is it *really* creative?", it redirects you to operationalized, measurable constructs.

- A 5-step procedure: name the smuggled-in criterion, run the hazard checklist (novelty grain, value-ladenness, measurement, serendipity confounds), evaluate rescue strategies, and reframe.
- Includes guidance for AI/LLM benchmark and eval design: build benchmarks for stipulated sub-capacities, pre-register the individuation grain and value rubric, and treat the folk term as out of scope.

Install:

```bash
npx skills add aryankeluskar/skills --skill creativity-rejectionism
```

### [`fetch-paper`](./fetch-paper)

Fetch an arXiv paper from a URL, arXiv ID, or title. Downloads the LaTeX source into `refs/<Title>/` (stripped of fonts and videos, figures kept as AI context) and the PDF into `papers/<Title> - <arxiv_id>.pdf` — one command, two artifacts.

- Stdlib-only Python 3, no pip installs, idempotent.
- URL/ID inputs never hit the arXiv API; only a bare-title search does.
- Flags for `--refs`/`--papers` dirs, `--source-only`, `--pdf-only`, `--yes`.

Install:

```bash
npx skills add aryankeluskar/skills --skill fetch-paper
```

### [`ml-paper-writing`](./ml-paper-writing)

Plan, write, review, and polish machine-learning research papers and their figures. It distills Neel Nanda's *Highly Opinionated Advice on How to Write ML Papers*, the "Behind the scenes of paper writing" post on *Base Models Can Reason By Taking a Cue From Training Data*, and Chengshuai Zhao's *How to Make Good Figures for Scientific Papers*.

- **Story first:** compresses messy notes or results into 1–3 claims, each with its evidence, weakest point, and a confidence level scoped to what was actually tested. Red-teams the claims against controls, baselines, and the closest prior work.
- **Writing and review:** a sentence-by-sentence abstract plan, an intro paragraph plan, and a review checklist that puts narrative before line edits. It never invents results or citations; anything missing becomes a visible `[RESULT: …]` / `[CITE: …?]` placeholder.
- **Figures:** each figure is planned around a one-sentence message and the result that would disprove it. A matplotlib helper (`scripts/paper_style.py`) adds the Tailwind v4 palette, venue column widths, emphasis by lightness that survives greyscale, and vector PDF export with TrueType fonts plus a font check.

Install:

```bash
npx skills add aryankeluskar/skills --skill ml-paper-writing
```

## License

MIT.
