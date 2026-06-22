---
name: creativity-rejectionism
description: Apply Henry Shevlin's "Strong Rejectionist" methodology (Shevlin 2021, EJPS) for handling claims that some non-human system — an animal OR an AI/LLM — is "creative," or exhibits an adjacent contested capacity such as insight, intelligence, understanding, or reasoning. Use this skill whenever someone asks whether a model/animal/system is "really creative," wants to design or critique a benchmark or eval for creativity or a similar fuzzy cognitive capacity, is reviewing a paper that claims a system shows creative intelligence, or needs to operationalize a vague folk-psychological concept into measurable constructs. Trigger it even when the word "creativity" never appears but the request hinges on a contested, bundle-of-criteria capacity concept (e.g. "does this LLM truly reason?", "is this animal genuinely insightful?").
---

# Creativity Rejectionism

A procedure for appraising claims of the form **"system S is creative"** (or insightful, intelligent, understanding, reasoning) when S is non-human — an animal or an AI system. It encodes the argument of Shevlin (2021), *Rethinking creative intelligence: comparative psychology and the concept of creativity* (EJPS 11:16).

The skill exists because these claims feel tractable but aren't. "Creativity" is not a scientific natural kind with an agreed definition; it is a folk-psychological **bundle of criteria** whose membership conditions researchers actively dispute. Asserting or denying it of a non-human system inherits every one of those disputes, plus new ones unique to the non-human case. The job of this skill is to stop you from adjudicating the unanswerable question ("but is it *really* creative?") and redirect you toward the answerable one ("which operationalized capacities does it exhibit, on which measure?").

## When this lens applies

Run the diagnostic before engaging the substance. The lens applies when **all** of these hold:

1. The claim ascribes a cognitive *capacity* (not a behavior) — "is creative", not "bent the wire".
2. The concept is a **bundle of criteria** with no consensus definition: people invoke different necessary/sufficient conditions and reach different verdicts. Creativity, insight, understanding, reasoning, intelligence, consciousness all qualify. Memory and learning are closer to settled and usually do *not*.
3. The subject is **non-human** (animal or machine), so the human escape hatches — agreed exemplars, first-person phenomenological access — are unavailable or contested.

If the request is really about a *behavior* ("did the crow raise the water level?") or a settled construct, skip the skill and answer directly. The skill earns its place only when someone is reaching for the contested umbrella term.

## Step 1 — Name the criterion being smuggled in

Whoever makes the claim is implicitly using *some* theory of creativity. Surface it. There are four broad families (full taxonomy in `references/theories-and-cases.md`):

- **Experiential** — creativity requires surprise (Boden) or an "aha!"/insight phenomenology (Kounios & Beeman).
- **Capacity/agency** — creativity requires *flair*, judgement, intentional agency directed at the task (Gaut; Paul & Stokes).
- **Spontaneity** — creativity requires independence from prior knowledge and intentional control; it is *unlike* ordinary goal-directed behavior (Kronfeldner; Amabile).
- **Process/stage** — creativity is a temporal sequence: prepare→incubate→illuminate→verify (Wallas), or blind-variation→selective-retention (Campbell, Simonton), or generate→explore ("geneplore").

Two conditions are near-universal across families: the output must be **novel** and **valuable**. State which family the claim depends on, because the verdict will flip depending on the choice — a behavior that counts as creative under a spontaneity theory may fail an experiential one. **Do not let a verdict ride on an unstated criterion.**

## Step 2 — Run the hazard checklist

For each hazard, say whether it bites this specific claim and how. These are the load-bearing arguments of the paper; cite them when you flag them.

1. **Definitional disagreement (§4.1).** Different theories partition nature differently. Worse than ordinary scientific dispute (wave/particle, kin selection) because here there is no agreement on how to *identify the phenomenon at all*, and — unlike memory research, which agrees on the concept and on tasks like n-back — creativity research lacks even that floor. Note that researchers disagree on whether value is required (Weisberg; Hills & Bird say no), whether surprise is required, whether the process is conscious. In the non-human case there are not even agreed exemplars to anchor on (some deny animal creativity wholesale — Fuentes 2017).

2. **The novelty grain problem (§4.2).** "Novel to the individual" is the *least* controversial criterion and still breaks. Individuate behavior finely and *everything* is novel (no two performances identical → novelty is ubiquitous and trivial). Individuate coarsely and *nothing* is (a painter trying a new form is still "painting" → novelty is near-impossible). There is no principled grain. For animals: is a crow's tool-bending novel, given wild crows bend twigs (Rutz et al. 2016)? The fine/coarse choice decides the verdict and nothing decides the choice. Contextualism about novelty leaks into a radical contextualism about creativity itself.

3. **Value-ladenness (§4.2).** Value varies across cultures and individuals. Anchoring value in the agent's own attitude fails (artists despised masterpieces — Michelangelo's Pietà, Virgil's Aeneid). For animals, metacognitive evaluation is mostly unavailable, so value must be cashed out objectively (fitness/survival) — but creativity-associated traits (neophilia, exploration) are frequently *dangerous* and fitness-*reducing* in the relevant environment (keas), and captive specimens can be "creative" in ways that would be lethal in the wild. Fitness and creativity come apart.

4. **The criterion / measurement problem (§4.3).** Human psychometrics (Alternative Uses, Remote Associates, Torrance) may measure divergent thinking rather than *creativity per se* (Amabile 1982). Arden et al. (2010): 45 neuroimaging studies, little overlap in implicated brain areas — the criterion problem had *worsened*, not resolved. If we can't pin a measure, neural signature, or criterion in humans, the prospect is far worse across the sensorimotor and cognitive diversity of animals.

5. **Serendipity / reinforcement confounds (§3.2, §3.3).** Many showcase cases reduce to chance + reinforcement + social learning (great tits and milk-bottle lids; meta-analysis of Aesop's-fable performance as trial-and-error + innate object preferences — Hennefield et al. 2019). Note though (footnote 6) that a reinforcement-learning origin does **not** automatically disqualify a behavior as creative — the Thorndike-to-Skinner-to-connectionism tradition grounds even human cognition in association. So "it's just RL" is a confound to flag, not an automatic defeater.

## Step 3 — Evaluate the rescue strategies (don't endorse uncritically)

People will offer fixes. The paper grants each some value but finds each insufficient *for rigorous comparative/AI science*:

- **Creativity comes in degrees.** Intuitive, removes the binary, but if still tied to a unified kind it inherits every hazard above — degrees of an ill-defined thing don't help you apply it.
- **Divide and conquer** (Boden's combinational/exploratory/transformational; Kaufman & Beghetto's four-C). Helpful, but be explicit whether you're doing *folk-conceptual analysis* or *building operational tools* — conflating them breeds confusion and a needless proliferation of distinctions. If the goal is measurement, this strategy is really a step *toward* rejectionism.
- **Prototype concept** (Chen 2018, via Rosch): membership by similarity to exemplars, not necessary/sufficient conditions. Good for modeling *folk usage*. But culturally/context-relative similarity judgments are exactly what makes it **ill-suited to rigorous comparative psychology** — and Chen concedes it may fracture into multiple natural kinds.

## Step 4 — Apply the rejectionist recommendation

Distinguish two positions:

- **Weak rejectionism** — a comparative science of creativity may be possible eventually, but isn't viable *now* given the open controversies.
- **Strong rejectionism** (the paper's tentative recommendation) — we already have good reason to think "creativity" is the *wrong kind of concept* for comparative psychology: more like **wit, charisma, or good taste** (folk, value-laden, context-bound) than like **learning, memory, or g-factor** (operationalizable). So "is animal/machine X creative?" is not a substantive scientific question. This is **not** human exceptionalism or mysterianism — Shevlin grants the component capacities are likely widespread in nature; the objection is to the *umbrella concept*, not to the abilities.

The constructive move: **drop the umbrella term and substitute stipulatively-defined, operationalized constructs** you can actually measure — behavioral plasticity, neophilia, exploration, innovation, divergent thinking, insight-as-restructuring (success after an impasse involving reconceptualization). Define them by fiat for the study at hand, with no deference to the folk concept.

Two payoffs to state explicitly:
1. **Pluralism without essence-hunting** — you can use typologies cutting across many dimensions of behavioral variability without theorizing what they all share.
2. **No dangling question** — if a scientist says "this satisfies my stipulated definition of behavioral-plasticity-type-3," there is no leftover "yes but is it *really* creative?" The austere vocabulary dissolves the trap. (Compare: episodic memory → "episodic-like memory" operationalized as what/when/where; intelligence → g-factor.)

Acknowledge the honest objection (§5): this may "move the bump in the carpet" — novelty is scarcely more perspicuous than creativity. The reply is that stipulation + pluralism still beats chasing a folk essence, even if residual hazards remain.

## Step 5 — For AI / LLM claims specifically (footnote 16)

This is where the skill most often fires in practice. Shevlin flags that strong rejectionism "might also be the best path" for whether a machine is creative: we can sensibly aim to build systems that **produce novel and valuable outputs and respond flexibly and appropriately to environmental change**, and the narrowly conceptual question of whether the machine is *really* creative is "largely irrelevant to achieving these ends."

Operational consequence for benchmark/eval design:
- **Don't build a "creativity benchmark."** Build benchmarks for stipulated, measurable sub-capacities (output novelty under a fixed individuation grain; value under a declared, task-specific rubric; behavioral flexibility under distribution shift; divergent generation; restructuring after impasse).
- **Pre-register the individuation grain and the value rubric** — Step 2's grain and value-ladenness hazards are the two that most silently inflate or deflate model "creativity" scores.
- **Treat "but does it *understand*/*reason*/*create*?" as out of scope** for the eval, by construction. The eval reports construct scores; it does not adjudicate the folk term. This is the strong-rejectionist discipline applied to evaluation.
- The same recipe transfers to other contested LLM capacity terms (reasoning, understanding, agency, planning): substitute operational constructs, declare measures, refuse the dangling essentialist question.

## Output template

When appraising a concrete claim, structure the response like this:

```
## The claim
[Restate it, and name the system S and the behavior(s) at issue.]

## Criterion in play
[Which of the four theory families the claim relies on — and whether it's stated or smuggled.]

## Hazards that bite
[For each relevant hazard from Step 2: how it applies here, with the cite. Skip ones that don't bite.]

## Rescue strategies, if invoked
[Only if the source offers degrees / divide-and-conquer / prototype — evaluate per Step 3.]

## Rejectionist reframing
[Replace the umbrella verdict with operationalized constructs + how you'd measure each.
 For AI: phrase as an eval-design recommendation.]

## Bottom line
[Whether the original "is it creative?" question is substantive here, or should be dissolved.]
```

## Scope notes

- Stay **agnostic on the human case.** The paper confines strong rejectionism to non-humans; humans retain agreed exemplars and phenomenological access. Don't over-extend the conclusion to "humans aren't creative either" — that's not the argument.
- Don't smuggle in human exceptionalism. The component capacities are likely abundant in nature and in machines; the target is the *concept*, not the abilities.
- The four-family taxonomy, the full animal case studies (Köhler's chimps, Pryor's porpoises, Betty the crow, Goffin cockatoos, Aesop's-fable corvids), and the strategy details live in `references/theories-and-cases.md`. Load it when you need the specific theories, citations, or examples rather than the bare procedure.