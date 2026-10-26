# Reviewing a draft

Review in order of impact. Narrative problems make everything downstream wasted effort, so they come first, and line edits come last. If the draft has a fundamental narrative problem, say so plainly and keep later sections short rather than polishing text that will be rewritten.

## 1. Narrative

- Can you state the paper's 1-3 claims in one sentence each after reading only the abstract? Write them down. If you cannot, that is the top issue.
- Do the claims share a theme, or is it a grab-bag?
- Is the "so what" explicit: who should think or act differently?
- Is it clear what is novel and what is borrowed? Which recent papers would a reviewer say already did this? List the ones you can recall, marked `?` for verification.
- Does the claim strength match the evidence (see the confidence ladder)? Quote each overclaiming phrase and propose a scoped alternative.

## 2. Evidence

- For each claim, which experiment is the decisive one? Is it in the main text?
- Are baselines present, strong, and tuned with comparable effort? Is the cheapest obvious baseline for the paper's own pitch included (e.g. log-probability for a "cheap single-pass" detector, a linear probe for a "no training" method)?
- For interventions: is there a matched control (random direction, shuffled edit), and a check that the intervention doesn't break cases that were already correct?
- Measurement confounds: length or position effects, the same model generating and judging, an unvalidated LLM judge?
- Internal contradictions: does a selling point in the abstract ("no training", "no labels", "model-agnostic") conflict with a detail in the method?
- Seeds, n, variance, and statistical support reported?
- Ablations for multi-part methods?
- Obvious alternative explanations addressed, by experiment or in limitations?
- Qualitative examples: is the selection procedure stated? Any random examples?
- Is enough detail given to replicate?

Do not demand experiments casually. Prioritize the one or two whose absence a skeptical reviewer would seize on, and say why.

## 3. Structure

- Abstract: field, gap, contribution, evidence with at least one number, implication? Does a cold reader know the subfield by sentence two?
- Introduction: context, background, claim, case, impact, contributions list? Is it self-contained?
- Does every section serve a claim? What could be cut or moved to the appendix?
- Are terms defined before use? Are new definitions separated from background?
- When claims rest on different kinds of evidence, is each method next to its result?
- Limitations section present and honest?
- Related work explains differences from the closest papers rather than just listing them?

## 4. Figures

- Do figures plus captions tell the story on their own?
- One message per figure? Is the key comparison adjacent and emphasized?
- Consistent colors across figures? Colorblind-safe? Readable at print size? Vector?
- Do captions state the takeaway and define error bars?
- Is there a teaser figure that conveys the paper at a glance?

## 5. Sentences

- Jargon that is not buying precision.
- Long sentences with several ideas: split.
- Hedging stacked on hedging ("may potentially suggest"), or the opposite, unqualified universals.
- Vague quantifiers where a number exists ("significantly better" without a number or test).
- Inconsistent terminology for the same thing.

## Feedback format

Keep the whole review short enough to act on in one sitting, typically under about 1,500 words for an abstract plus introduction. Depth goes into the top issues; everything else stays brief.

```
## Summary
What I take the paper's claims to be (1-3 sentences). [If this differs from what the authors intended, that is the first problem.]

## Top issues (highest impact first, max 3-5)
1. <issue>: why it matters, concrete fix.

## Rewritten <section>   (only if a rewrite was requested; it goes here, near the top)
<the rewrite, ready to paste>
What changed and why (a few bullets). Assumptions to confirm.

## Section by section (brief)
### Abstract
### Introduction
...

## Line edits (the handful that matter most)
- "<original>" -> "<suggestion>" (reason)

## What works well
Specific strengths worth keeping, so revisions do not lose them.
```

Make a rewrite pasteable: in LaTeX, put notes for the author in a `%` comment block above the environment (not inside it, and not `\todo{}`), and mark every placeholder in the text itself. Do not slip in specifics the draft does not state ("a few heads", "a small labeled set"). If a detail is needed, leave a placeholder and ask.
