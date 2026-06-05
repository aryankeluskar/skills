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

### [`brand-naming`](./brand-naming)

Generate brand, product, company, startup, app, AI agent, feature, or project name candidates — grounded in David Placek's (Lexicon Branding) methodology, the same process behind Sonos, Pentium, Blackberry, Powerbook, Swiffer, Vercel, Windsurf, CapCut, and Azure.

Two modes:
- **Quick** — one-shot generator, ~50 candidates across coined/compound/metaphor/cross-domain buckets with sound-symbolism rationales.
- **Full** — guided multi-phase workshop: Diamond exercise → disguised-brief generation → polarization/fluency screening → stakeholder-ready shortlist with prototypes.

Install:

```bash
npx skills add aryankeluskar/skills --skill brand-naming
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

## License

MIT.
