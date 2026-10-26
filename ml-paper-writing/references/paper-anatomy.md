# Paper anatomy

Contents: the reader funnel · title · abstract · introduction · main body · captions · discussion and limitations · related work · appendices · pitfalls · drafting conventions

## The reader funnel

Many people read the title, a good number read the abstract, fewer read the introduction or skim the figures, and very few read the whole paper. Two consequences:

- The abstract and introduction must each work as a self-contained summary. Do not save the punchline for later; repeating the key idea in varied forms helps it stick.
- Spend effort roughly equally on (title + abstract), introduction, figures, and everything else.

## Title

Short, specific, and ideally states the finding or the object of study. A title that states a claim ("X is mediated by a single direction") is memorable but commits you to it, so it must be well supported.

## Abstract

The reader arrives cold, possibly not even knowing the subfield. Orient them fast, then deliver the claims in plain language. One idea per sentence. A dependable plan:

1. **Field sentence.** Something uncontroversial that places the paper (e.g. "Reasoning models now lead many math and coding benchmarks.").
2. **Gap sentence.** The need, puzzle or problem (e.g. "It is unclear whether RL post-training teaches new reasoning or surfaces ability the base model already has.").
3. **Main contribution.** The central claim and why it is exciting. Losing nuance here is fine.
4. **(Optional) Clarification.** What the claim means or how one could test it; define any unavoidable jargon.
5. **Evidence / further claims.** One sentence each. Include at least one concrete number that shows the effect is real and substantial, ideally folded into the sentence that states the claim.
6. **Close.** Why it matters, implications, and the standard of evidence: "a first step toward...", "shows practitioners should...", "provides compelling evidence that...", "establishes best practice for...".

Typical length: 150 to 250 words; check the venue limit (ACL allows 200). When drafting with missing numbers, keep the sentence and insert `[RESULT: ...]`. Keep each number attached to its model and benchmark. A result measured on one model should not read as general, and a weaker result on a second model should not be hidden behind "replicates".

Skeleton:

```
[Field sentence.] [Gap sentence.] We show that [main claim], [key number].
[Clarify how/what, if needed.] [Evidence or second claim, with number.]
[Evidence or third claim.] [Implication + standard of evidence.]
```

## Introduction

An extended, self-contained version of the abstract. A dependable order:

1. **Context and motivating question.** What is studied, what question drives the paper, why it matters. Optionally one sentence on how the paper answers it. Cite to establish that the area is real, the problem matters, and others have tried.
2. **Technical background.** What is known, which established techniques the paper rests on, why existing work is insufficient. Cite to show the methods are standard and to orient readers.
3. **Main contribution.** The precise main claim, with key nuance and scope.
4. **The case.** The most important evidence for that claim, summarized. (Can merge with 3.)
5. *(Optional)* Repeat 3-4 for a second or third claim.
6. **Impact.** What readers should take away and who should act differently: practical utility, basic science, correcting a misconception.
7. **Contributions list.** Bullets, one per claim, each with a short pointer to its evidence. A reader should be able to scan it and decide whether they care.

The introduction is the place to define terms the claims depend on. Citations here serve the argument (roughly one per key step) rather than covering everything; exhaustive coverage belongs in related work. The introduction also sets the structure of the paper: sections should appear in the order the intro promised.

## Main body (background, methods, results)

Most of the word count goes here, communicating exactly what was done and observed so experts can draw their own conclusions. Readers need, at several levels of detail:

- the background needed to disambiguate the work (terms and techniques),
- what the results are and how to interpret them,
- what the experiments actually were,
- why those experiments are relevant to the claims,
- the technical choices made and how they affect interpretation.

Default structure:

- **Background.** Define terms and techniques. Err toward defining (skip "transformer", define "sparse autoencoder" or "steering vector"). Keep new definitions introduced by this paper visibly separate from reviews of known material. A glossary appendix helps when space is tight.
- **Methods**, then **Results**, with each experiment in its own subsection when methods are similar.
- **If claims rest on different kinds of evidence**, organize by claim instead: one section per claim containing its method and result, each tied back to the theme. Readers forget a method described four pages before its result.

Every section and subsection should have a clear job in the narrative. Plan each paragraph's first sentence (what it shows) and last sentence (how it connects) before filling in the middle.

## Captions

A figure plus its caption should be understandable without the main text. Include:

1. What is shown (conditions, models, data, metric).
2. How to read it (axes, encodings, what error bars are).
3. The takeaway, stated directly. Leading the caption with the takeaway, often bolded, works well.
4. Technical details needed to interpret it (n, seeds, benchmark).

## Discussion and limitations

Limitations are essential. Readers need them to know what they actually learned, and the authors know the weak spots far better than any reader. A paper that states its limits up front is more trusted by the readers who matter. Also include broader implications, future work, and open questions. A separate conclusion that only restates the introduction can usually be cut.

## Related work

Usually the penultimate section. Move it forward only if the paper is heavily defined by prior work (plugging a specific gap, correcting a mistake, extending a specific method). Its real job: for each closely related paper, explain how this work differs. If it does not differ much, say so ("concurrent work"), or explain the remaining value, or explain the flaw this work fixes, politely. Coverage of loosely related work is a social norm; keep it brief and accurate. Never invent citations; leave `[CITE: ...]` placeholders.

## Appendices

Think of the paper as a long document whose first eight or nine pages are the highlights reel. Appendices hold the full technical detail, extra experiments, hyperparameters and examples. They are read rarely and held to a lower polish standard, so do not over-invest in them.

Consider an appendix (or companion blog post) for tacit knowledge that the formal paper discards: what was hard and how it was made to work, failure modes encountered, intuitions the authors hold but cannot fully defend, common misreadings of the results, advice for replication and hyperparameter search, and favorite future directions.

## Pitfalls

- **Optimizing for acceptance over truth.** Peer review is noisy (the NeurIPS 2021 consistency experiment showed reviewer committees often disagree on the same paper). Do the best science first; package it for the venue at the end, and undo any packaging that made the work worse before posting the preprint.
- **Verbosity and false sophistication.** Readers who cannot follow a paper usually skip it or distrust it. Be precise, then as simple as possible within that precision.
- **Writing last.** Writing quality multiplies the impact of the work. Aim to switch from experimenting to writing about a month before a deadline, leaving time for feedback and iteration.
- **Grab-bag papers.** Unrelated findings dilute each other. Keep the theme.
- **Hiding contradictory results.** Report them, explain them, or narrow the claim.

## Drafting conventions

- Draft in bullets before prose, at every level.
- Placeholders: `[RESULT: ...]`, `[CITE: ...]`, `[TODO: ...]`, `[FIG: ...]`. In LaTeX, `\cite{TODO-key}` (compiles with a warning) and `% TODO:` comments. Use `\todo{...}` only if the author's preamble already loads todonotes.
- When offering alternatives (e.g. two framings of the main claim), label them and say what each prioritizes.
- After drafting, reread as a cold reader: is the subfield clear by sentence two? Is every term defined before use? Is there a number in the abstract?
- Writer's block: outline plus a rough LLM draft can break the logjam, but the final text should be rewritten in the authors' own understanding and voice.
