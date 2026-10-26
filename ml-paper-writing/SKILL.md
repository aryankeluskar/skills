---
name: ml-paper-writing
description: Plan, write, review and polish machine-learning research papers and their figures - finding the 1-3 claims a project actually supports, drafting abstracts, intros and results sections, red-teaming evidence, storyboarding figures, and turning result plots into publication-quality matplotlib figures. Use this whenever someone is working on an ML/AI paper, preprint, workshop submission, thesis chapter or research write-up (e.g. "help me write my NeurIPS abstract", "what's the story of my paper", "review my intro", "make this plot paper-ready", "design a teaser figure", "turn my research notes into an outline"), even if they never say the word "paper".
---

# ML Paper Writing

A paper succeeds when a reader walks away understanding a small number of claims, believing the evidence behind them, and knowing why they matter. Readers rarely retain more than a few sentences of any paper, so everything here is about choosing those sentences deliberately and making every section, figure and caption serve them.

This skill distills three practitioner guides (see Sources at the end). Their shared view: writing is part of the research, not a chore after it. Working out how to communicate a finding often exposes gaps in it, and sketching the figures you hope to show is a good way to design the experiments that would produce them.

## Step 1: Work out where the author is

Different requests need different work. Identify the situation, then read the matching reference file before producing anything substantial.

| Situation | What to do | Read |
|---|---|---|
| Has results or notes, no clear story yet ("what's my paper?", "turn these notes into an outline") | Build a narrative card (below), red-team it, then outline | `references/narrative-and-evidence.md` |
| Has a story, needs text (abstract, intro, results, related work, limitations) | Confirm the claims, then draft the section with its recipe | `references/paper-anatomy.md` |
| Has a draft and wants feedback | Review in priority order: narrative, evidence, structure, figures, sentences | `references/review-checklist.md` |
| Planning experiments or figures, possibly before results exist | Storyboard each figure as a falsifiable spec | `references/figures.md` |
| Has data or a plot and wants it publication-ready | Restyle with `scripts/paper_style.py`, one message per plot | `references/figures.md` |
| Wants a teaser / Figure 1 / method diagram | Find the single mental picture of the paper, then design it | `references/figures.md` |

Requests often span several rows (e.g. "here are my notes, write the abstract and suggest figures"). Do them in table order: narrative first, because the abstract and figures both depend on it.

## Ground rules for every mode

1. **Never invent results, numbers, citations or prior work.** Use visible placeholders instead: `[RESULT: pass@1 for base+cue on MATH]`, `[CITE: grokking, Power et al. 2022?]`, `[TODO: confirm number of seeds]`. A fabricated number or reference that slips into a submitted paper is a serious integrity problem; a placeholder costs the author ten seconds and shows them exactly what to check. The same goes for experiments: do not describe an analysis that has not been run as if it had, even without numbers. In LaTeX the author will paste, use `\cite{TODO-key}` and `% TODO:` comments; avoid `\todo{}` unless they already load todonotes, because it breaks compilation in a stock venue template.
2. **Hunt for the closest prior work, and flag it as unverified.** The most damaging review is "this was already done". Actively recall the nearest prior and concurrent papers, especially recent ones on the same behavior, models or method, and list each with a question mark for the author to verify (or verify them yourself if web search is available and appropriate). Naming a competitor that turns out to be irrelevant costs a minute; missing one costs the paper.
3. **Calibrate claims to evidence.** Match wording to what was shown (existence proof, hedged, narrow, systematic; see the confidence ladder in `references/narrative-and-evidence.md`). Point out overclaiming plainly. Researchers worth impressing see through hype, and a paper that states its limits earns more trust.
4. **Fight the illusion of transparency.** The author has lived in this project for months; the reader arrives cold. Say early what kind of paper this is and which subfield it belongs to, define non-standard terms (steering vector, token cue, SAE) on first use, and state the obvious-to-the-author motivation explicitly.
5. **Plain, precise language.** Use jargon only where it buys precision. Simple techniques applied carefully read as strength, not weakness. Cut text written to sound impressive.
6. **It is the author's paper.** Propose, explain why, and let them decide. Ask about what only they know: which result surprised them, what is actually new versus borrowed, what they would defend under hostile questioning. When you substantially rewrite their text, say what changed and why.
7. **Match their working format.** LaTeX in, LaTeX out; Markdown in, Markdown out. Keep their notation and terminology unless it is causing confusion, and then flag the change.
8. **Deliver what was asked, first, at a length that gets used.** Researchers are busy and often close to a deadline. Put the requested artifact (the rewritten abstract, the figure, the story) near the top, then the reasoning and supporting notes. Apply the advice in this skill to your own output: prioritize the few points that matter most, and cut the rest or move it to a clearly marked "more detail" section. A planning document for a co-author should be readable in about ten minutes. Leave production details (fonts, column widths, exact colors) out of story-stage documents; they belong to the figure-making stage.

## The core object: a narrative card

A narrative is one to three concrete claims that fit one theme, the strongest evidence for each, and a reason the reader should care. Before drafting any prose, write (or ask the author to confirm) a card like this:

```
Working title:
One-sentence takeaway:        what a reader who stops after the abstract should know
Context and problem:          what field, what gap or puzzle, why it matters now
Claim 1:                      ...   (confidence: existence | hedged | narrow | systematic)
  Key evidence:               1-3 experiments; note which are qualitatively different
  Weakest point:              strongest objection a skeptical reviewer would raise
Claim 2 / 3:                  (optional; must share the theme)
So what:                      who should think or act differently, and how
Novel vs. prior work:         what is new here; what is borrowed and from whom
Limitations / misreadings:    ways a reader could over-update
Figure storyboard:            Fig 1 teaser = ...; Fig 2 = ...; Fig 3 = ...
```

Fill what you can from the material, mark gaps as questions, and show it to the author before expanding. Fixing a narrative takes minutes; fixing eight pages of prose built on the wrong narrative takes days.

## Writing process: compress, then expand

1. **Compress** the project into the narrative card. Useful tests: explain it aloud in two minutes; ask what a colleague found most interesting; check whether the evidence could be true while the claim is false.
2. **Outline the introduction** in bullets: claims, why they matter, what is novel, a high-level case for why they are true.
3. **Outline the whole paper** in bullets. For every section, be able to answer "what breaks if I cut this?" If nothing does, cut it or move it to an appendix.
4. **Make draft figures from real results** and check that they support the narrative. This is where missing experiments show up.
5. **Draft prose.**
6. **Edit repeatedly**, ideally with outside feedback at each stage.

When asked for a single piece (say, an abstract) with no narrative established, do a quick version of step 1 first and state the claims you are building on, so the author can correct course before you go further.

Allocate effort by readership: title and abstract, introduction, figures, and everything else deserve roughly equal time, because far more people read the first three than the rest.

## Figures tell a parallel story

The figures and the text should each be able to carry the paper alone: a reader who only looks at figures and captions should still get the claims, and a reader who only reads the text should still follow the argument. Key principles (details, specs and examples in `references/figures.md`):

- Each plot conveys one idea. Write its one-sentence message before plotting; drop metrics or panels that answer a different question.
- Storyboard early. Sketching the figure you expect forces a falsifiable prediction. When the result disagrees with the sketch, that is a finding, and often the cue to add a condition that disentangles it.
- Panel order follows the explanation. Put the comparison you care most about side by side, on a shared axis, with whitespace grouping it.
- What is visually loudest is what readers look at. Emphasize the key series and mute the context, using lightness as well as hue, so the emphasis survives greyscale printing and color blindness.
- Give each condition one consistent color across the whole paper. Order conditions as the argument runs (baseline, alternatives, then the method).
- The caption's claim must hold for every condition and model in the figure. If the effect is large for one model and modest for another, say so.
- Export vectors (PDF/SVG) with text kept as text. Never JPEG.

For data plots, use the bundled helper:

```python
import sys; sys.path.insert(0, "<skill-dir>/scripts")
import paper_style as ps

ps.use_paper_style()                          # fonts, sizes, Type 42 PDF fonts, clean axes
fig, ax = plt.subplots(figsize=ps.figsize("column", venue="icml"))
cc = ps.condition_colors(["No intervention", "Prompting", "Ours"],
                         hues={"Prompting": "sky", "Ours": "orange"},
                         baseline=["No intervention"], focus=["Ours"])   # focus = darker shade
ax.bar(names, vals, color=[cc[n]["fill"] for n in names], edgecolor=[cc[n]["edge"] for n in names])
ps.save(fig, "figures/fig2_cue_accuracy")     # vector PDF + color and greyscale PNG previews; warns on font problems
```

Look at both previews before delivering. In the greyscale one, the key condition should still stand out. For a paper with several figures, put `paper_style.py` in the user's repo so every figure shares one palette and style. For a one-off figure, you can instead inline the handful of colors and rcParams you used, so the user gets a single self-contained script.

Run `python scripts/paper_style.py --help` for the palette, venue widths and a demo figure.

## Reviewing a draft

Give feedback in order of impact. A buried narrative problem matters more than forty comma fixes, and line edits on a section that should be cut are wasted. Lead with a short summary and the top three issues. If a rewrite was requested, give it right after them, then section notes, then a few line edits. Use `references/review-checklist.md` for the questions and output format.

## Reference files

- `references/narrative-and-evidence.md`: finding the claims, confidence ladder, novelty, the evidence and red-team checklist, a worked decomposition. Read for any "what is my paper" or "is my evidence enough" question.
- `references/paper-anatomy.md`: section-by-section recipes (title, abstract sentence plan, intro paragraph plan, contributions, body, captions, limitations, related work, appendices) and common pitfalls. Read before drafting or restructuring any section.
- `references/figures.md`: figure storyboard spec, lessons from sketch-to-final revisions, teaser figures, typography, color, layout, visual hierarchy, export, tool choice, venue widths. Read before planning or making any figure.
- `references/review-checklist.md`: prioritized review questions and a feedback template.
- `scripts/paper_style.py`: matplotlib style, Tailwind v4 palette as hex, venue figure sizes, save-and-check helper.

## Sources

Distilled and paraphrased from: Neel Nanda, "Highly Opinionated Advice on How to Write ML Papers" (AI Alignment Forum, 2025); the blog post "Behind the scenes of paper writing" (2026) on the paper "Base Models Can Reason By Taking a Cue From Training Data"; and Chengshuai Zhao, "How to Make Good Figures for Scientific Papers" (2025). Nanda notes his advice leans toward mechanistic interpretability and toward truth-seeking over conference optimization, and the figure-first workflow suited a phenomenon-driven empirical study. Adapt to the author's field and venue norms.
