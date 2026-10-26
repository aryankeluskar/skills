# Narrative and evidence

Contents: what a claim is · confidence ladder · finding the narrative · when to start writing · novelty · evidence checklist · red-teaming · worked decomposition

## What a claim is

A claim is a specific, checkable statement you believe is true and can support. Typical shapes:

- "Method X beats the alternatives on task Y, by metric Z."
- "Most of the model's behavior in setting A is explained by a simple mechanism B."
- "Technique C fails in setting D whenever conditions E and F hold."
- "Intervention P moves quantity Q by R, and removing P removes the effect."

One strong claim with strong evidence is enough for a good paper. With two or three, they must share a theme so the paper reads as one story rather than a grab-bag. If a project has five interesting findings, pick the ones that fit together, and move the rest to an appendix, a follow-up, or a blog post.

## Confidence ladder

Phrase each claim at the strength the evidence earns. Stronger claims are more interesting and need more evidence.

| Level | Typical wording | Evidence needed |
|---|---|---|
| Existence proof | "We find at least one case where X happens" | One trustworthy, well-verified example |
| Hedged | "We find suggestive / tentative / compelling evidence that X" | Consistent results with acknowledged gaps |
| Narrow | "X is the best choice for settings V and W when the goal is Y" | Strong results inside a clearly stated scope |
| Systematic | "X generally holds across a wide range of settings" | Many models, datasets, seeds; diverse methods |
| Guarantee | "X always holds" | A proof. Essentially never available for neural networks |

When editing someone's text, watch for drift up the ladder: "we show that LLMs..." on evidence from one 7B model is a systematic claim with existence-proof evidence. Suggest a scoped rewrite ("in OLMo-3-7B, ...", "across the three models we test, ...").

## Finding the narrative

A project usually ends as a mess of results, confusions, dead ends and half-explained effects. Turning that into a narrative is a skill. Questions that help:

- Which single result would you show a colleague first? Which made you say "huh"?
- If you showed the findings to someone in the field, what would they ask about?
- What was hard about this work that others have not done?
- Why should anyone outside your group care? Who would act differently?
- What do you now believe that you did not believe before the project?

A complete narrative covers: the context, the problem, why it matters, what you showed, why the reader should believe it, and the takeaway.

When working from someone's notes: list every finding, tag each with its evidence strength, cluster findings into candidate themes, and propose the theme that has both the strongest evidence and the clearest "so what". Explicitly list what you are proposing to cut or demote and why, because the author may value something you underrated.

## When to start writing

- Write down the list of things you learned.
- For each, ask how comfortable you are defending that you have real, positive evidence for it.
- Ask why others would care.
- Before switching to writing mode, verify the critical experiments. Re-run them, ideally re-implement them by a different route, and check for bugs. A surprising amount of published work is wrong or misleading because nobody did this. Aim to have verified essentially every experiment the paper relies on.

For a first paper, a project with an obvious narrative shape ("method X beats strong baseline Y on Z") is much easier to write up than an open-ended investigation.

## Novelty

Novelty means the paper should change what a careful reader believes. Rigorous replications, scaled-up confirmations of shaky results, and well-executed negative results all qualify, even though some reviewers undervalue them.

The practical problem is that a reader cannot tell what you consider new. Be explicit in the introduction (and related work) about:

- which techniques are standard and which are yours,
- whether the contribution is a new phenomenon, a new method, a cleaner demonstration of something suspected, or an application of a known idea to an important new target,
- exactly which prior papers come closest and how this one differs (larger effects, more models, causal rather than correlational evidence, a simpler method, a fixed bug).

Two common patterns to phrase carefully:

- **Building directly on a prior result.** Credit it clearly and isolate your delta (for example, "prior work found the representation with nonlinear probes; we show a linear probe suffices, which matters because...").
- **Known kind of finding, important new target.** The novelty is the target and the consequences, not the technique (for example, "linear representations are well documented; we show refusal specifically is mediated by one direction, and that removing it disables refusal cheaply").

If the work fixes a flaw in prior work, say what was wrong, why it matters and how this work resolves it, in a neutral tone about the work, never about its authors.

How a contribution is framed changes how it is received: the same results can read as overreaching or as a solid incremental step. Help the author pick the honest framing.

**Hunting for overlap.** Before endorsing a narrative, actively list the closest prior and concurrent work you can recall:
- the same behavior or phenomenon studied with any method,
- the same method applied to any behavior,
- recent papers (the last year or two) on the same models or benchmarks, which reviewers will know best.

Mark each one `?` so the author verifies it, and say what overlap it would create if it is what you remember. If web search is available and appropriate, check the most threatening ones yourself. Never present a recalled citation as verified, and never invent one to fill a gap. If the author has not mapped the related work, recommend a focused literature pass before writing, since it can change which claims are novel.

## Evidence checklist

With claims, the goal is that everyone grasps the intuition. With evidence, the goal is that an engaged, skeptical expert can check it in full technical detail.

**Does the experiment distinguish hypotheses?** The point of an experiment is that its outcome differs depending on which explanation is true. List the plausible alternatives and check that the key experiments would come out differently under them.

**Can the result be trusted?**
- Bug test: how surprised would you be if this turned out to be an artifact of a bug, leakage, noise or a misunderstanding? Investigate wherever the answer is "not very".
- Noise: sample size, number of seeds, standard deviations or confidence intervals. Is the effect clearly separated from run-to-run variation?
- Statistics: p < .05 is a weak threshold; in fields that study replication, findings at .01 < p < .05 often fail to replicate. For exploratory analyses with many possible hypotheses, be skeptical of anything weaker than about p < .001.
- Surprising results deserve extra verification, ideally a reimplementation or an independent route to the same evidence.

**Ablations.** If a method changes A, B and C, show the effect of removing each one, so readers know which parts matter.

**Controls for interventions.** When the evidence is an intervention (ablating or adding a direction, editing data, patching activations, a new prompt), ask what a trivial intervention of the same size would do:
- a random or unrelated direction of matched norm, a shuffled edit, or an equally long irrelevant prompt;
- over-correction: does the intervention also break cases where the original behavior was correct? For example, an anti-sycophancy edit should not make the model disagree with users who are right.

**Behavior vs. capability.** If the claim is about a behavior (sycophancy, refusal, hallucination), check that failures are not just missing knowledge or ability. For example, restrict to items the model answers correctly without the manipulation.

**Measurement confounds.** Check that the metric measures the claimed property:
- scores that scale with length, frequency or position, and need normalizing;
- the same model generating the data, the eval set and the judgments;
- templated training pairs whose style the method could pick up instead of the concept;
- an LLM judge that has never been checked against human labels on a sample.

**Alternative explanations.** What else could produce this pattern? Ask others. After a reasonable effort, acknowledge what remains untested.

**Cherry-picking and post-hoc analysis.**
- Say how qualitative examples were chosen. Show some randomly selected ones alongside the best ones. (Exception: for an existence proof, one verified example is the point.)
- Track which analyses were planned before seeing results and which came after. Pre-registered predictions that come true are much stronger evidence. Even confirmed predictions can be right for the wrong reason.

**Quality over quantity.** One decisive, hard-to-deny experiment beats many weak ones. Put the most compelling evidence in the main text; move the rest to the appendix.

**Diverse lines of evidence.** Several qualitatively different methods agreeing (for example, correlational analysis, causal intervention, and qualitative inspection) is far more robust than many variants of one method. Test: given experiment 1's result, how well could you have predicted experiment 2's? If perfectly, it adds little.

**Distill at the end.** By the end you know which kind of evidence is most convincing. If time allows, run one cleaner, decisive version of it, or scale it up (more models, seeds, datasets).

**Baselines.**
- Show the method beats plausible alternatives, not just that it "works".
- Include the cheapest obvious baseline for the paper's own selling point. If the pitch is "cheap and single-pass", compare against the cheapest single-pass signals (token log-probability, entropy). If the pitch is "no training", compare against a simple trained probe on the same data.
- Give baselines the same tuning effort as the new method (hyperparameters, prompting, scaffolding). Weak baselines are among the most common reasons experts dismiss a paper.
- The best papers combine qualitative and quantitative evidence.

**The guiding question.** Ask "should this change a reader's beliefs about my claim?" rather than "does this look like a rigorous paper?" If reading fifty examples by hand is genuinely strong evidence, report it and explain why.

**Reproducibility.** Give enough detail to replicate. Release code if possible: runs on a fresh machine, a README with links to weights and data, a notebook showing the key steps.

## Red-teaming the narrative

The danger of looking for a good story is ignoring evidence that contradicts it. Before writing, and again on the full draft:

- Assume there is a mistake. Where is it most likely?
- Assume there is a hole between the evidence and the headline claim. Where is it?
- Could the evidence be true and the claim still false? How?
- What would the most skeptical reviewer in this subfield say first? Has the paper already answered it with an experiment or an explicit limitation?
- What will readers most likely over-update on? Write that down; it belongs in the limitations or discussion.

Bold claims get read with a strong prior that they are wrong. If a reader finds an unaddressed hole, they usually stop reading. If the paper has anticipated the objection and closed it, the same boldness becomes exciting.

## Worked decomposition

Example of reducing a paper to claims, context, motivation and evidence, based on the token-cue paper behind one of the source guides. Use it as a model for what the narrative card should look like when filled in.

- **Takeaway:** a base model's reasoning ability is largely accessible by steering its first few tokens, and those steering words get their power from the contexts they appear in during training.
- **Claim 1:** forcing a base model to begin its response with a short cue (such as "Okay") brings its single-attempt accuracy close to that of its RL-post-trained counterpart.
  - Evidence: pass@1 of base vs. base + cue vs. RL model on reasoning benchmarks.
- **Claim 2:** RL post-training changes the model's predictions mostly at the start of the response, making such effective openings more likely.
  - Evidence: where base and RL next-token probabilities diverge along a response; how opening-token probabilities shift after RL; supplying the cue during RL reaching high accuracy in fewer steps.
- **Claim 3:** a cue's effect comes from associations in training data.
  - Evidence: a counterfactual data edit (replace "Okay" with an arbitrary word in mid-training data) makes the arbitrary word an effective cue; a second edit redirects "Okay" and removes its effect; representation similarity links different cues to different training sources.
- **Context:** debates about whether RL teaches new reasoning or surfaces existing ability; pass@k comparisons of base and RL models.
- **Why it matters:** suggests cheap ways to elicit reasoning and to make RL more efficient, and supports the view that instruction-like phrases act as pointers into training data rather than carrying meaning themselves.
- **Note the structure:** the claims form one chain (what works, what RL changes, why it works), and each is backed by a qualitatively different kind of experiment (behavioral, distributional, causal data intervention).
