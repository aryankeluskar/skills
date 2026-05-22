---
name: placek-naming
description: "Generate brand, product, company, project, or feature name candidates using David Placek's (Lexicon Branding) methodology — the same process behind Sonos, Pentium, Blackberry, Powerbook, Swiffer, Vercel, Windsurf, CapCut, and Azure. Use when the user asks to name a product, company, startup, library, feature, project, app, AI agent, or codebase; says things like 'help me name X', 'name ideas for Y', 'brainstorm names', 'rename this', 'what should we call it'; or wants to evaluate an existing name candidate. Two modes — QUICK (one-shot generator, ~50 candidates with rationales) and FULL (guided multi-phase workflow covering the Diamond exercise, disguised-brief generation, polarization/fluency screening, and a shortlist with prototypes). Skip for variable/function/file naming (this is brand-level, not code-symbol naming) unless the user explicitly wants brand treatment."
---

# Placek Naming

This skill encodes David Placek's naming methodology (Lexicon Branding, ~4000 projects, 40+ years). Use it whenever the user wants to invent a brand-level name.

## First step: pick a mode

Ask the user once: **Quick or Full?**

- **Quick** (~5 min): user gives a one-line brief, you return ~50 candidates grouped by direction with sound-symbolism + processing-fluency rationales. Skip the Diamond and disguised briefs.
- **Full** (~30–60 min interactive): run the Diamond exercise, generate against 3 disguised briefs, target 500–1000+ raw ideas, then screen down to a shortlist. Use when stakes are high (company name, public product launch, rebrand).

If they don't specify, recommend Quick for features/internal tools, Full for company/public product.

## Core principles (apply in both modes)

These come from Placek directly. Internalize them — they drive every decision below.

1. **Distinctiveness beats descriptiveness.** "CloudPro" loses; "Azure" wins. Descriptive names disappear into a sea of competitors. A great name starts a *story*, not makes a *statement*.
2. **You won't know it when you see it.** The right name almost always feels uncomfortable on first read. Comfort = familiarity = past = forgettable. Don't filter on "do I like it" — filter on "what does it *do*".
3. **Polarization is a signal of strength.** If half the team loves it and half hates it (Pentium vs. ProChip), that's the right name. Consensus on a name usually means it's safe and weak.
4. **Behavior and experience > positioning and values.** Ask "how do you want to behave in the market, and how should the market behave toward you?" — not "what are your values."
5. **Tangible-ize the intangible.** Software/AI/services need a physical metaphor (Windsurf = flow, Blackberry = device-as-fruit). If the product is abstract, force a concrete image.
6. **Compounds are multipliers.** Powerbook, Facebook, Blackberry, Windsurf. Two familiar morphemes → 1+1=3 associations. Don't dismiss compounds for being "long."
7. **Suspend judgment; speculate.** Generate volume first. 200 names isn't enough — push to 1000+. Then ask "what could we *do* with this?" not "is this good?"
8. **The .com doesn't matter much.** Get the right name first; buy the domain second, or use a prefix/`.ai`/`.co`.

## Mode A: Quick generator

When user picks quick mode:

1. Gather a one-paragraph brief: *what does the product do, who's it for, how should it feel, what's the competition called.*
2. Generate **at least 50 candidates** across these direction buckets (label each bucket):
   - **Coined / invented** (Vercel, Sonos, Pentium) — morpheme + morpheme
   - **Compound** (Windsurf, Blackberry, Powerbook) — two familiar words
   - **Metaphor / experience word** (Azure, Swiffer, Cursor) — evokes feeling
   - **Mythological / classical** (Anduril, Anthropic, Atlas) — use sparingly; warn this is the engineer-default trap
   - **Cross-domain pull** (the "magazine trick" — pick a word from a totally unrelated field like sailing/cooking/architecture)
3. For each name, write one line of rationale citing: sound-symbolism letter assets, morpheme meaning, processing fluency, and what the name *does* for the reader. See [references/sound-symbolism.md](references/sound-symbolism.md).
4. Mark candidates with a `⚡` if they are likely to *polarize* the team (this is good — call it out).
5. Do NOT pre-rank by "best." Present neutrally so the user can react.
6. Close with: "Test the top 3 by telling a friend 'a new competitor just launched called [name]' and listen to what they imagine. Don't ask 'do you like it.'"

## Mode B: Full workflow

When user picks full mode, run these phases in order. Each is interactive — pause for user input between phases.

### Phase 1: Identify (the Diamond)

Walk the user through the Diamond exercise. Draw it in text:

```
              WIN
       (how do we define winning?)
             /   \
            /     \
   WHAT TO -+------+- WHAT WE
     SAY    |      |   HAVE
            \     /
             \   /
        WHAT WE NEED
```

Ask each corner in order:
- **WIN** — how do you define winning? (Five people in a room will give five answers. Surface them all.)
- **WHAT WE HAVE** — what do we already have that helps us win?
- **WHAT WE NEED** — what's missing? (Talent, distribution, capability, etc. People often say "a good name" — correct them: *the right name*, not a good one.)
- **WHAT TO SAY** — what do we need to say to the market to win? Spend the most time here.

Then the **behavior question**: "How do you want to behave in the marketplace, and how should the marketplace behave toward you?" Then the **competitive landscape**: list 5–10 competitor names and the language they all use.

Synthesize into a **creative framework** (3–5 bullets). This replaces "objectives" — it's a window, not a target. Get user sign-off before moving on.

### Phase 2: Invent (disguised briefs)

This is the unique Placek move. Generate against **three parallel briefs**:

- **Brief A — real brief.** Generate ~200 candidates directly against the framework.
- **Brief B — adjacent disguise.** Pretend the product is in a different category (if it's an AI IDE, pretend it's a kitchen appliance, or a sailboat, or a sports brand). Generate ~200 candidates for *that* product.
- **Brief C — pure cross-domain.** Pick a totally unrelated context (hunting magazine, architecture journal, cooking show, a sport). Generate ~200 words/phrases from that world. Don't try to make them "fit" — just collect.

**Most winning names come from B or C.** Windsurf came from a "flow / dynamic movement" list, not from an "AI coding tool" list.

Use [references/sound-symbolism.md](references/sound-symbolism.md) to bias letter choice toward the framework's desired feeling (alive → V/Z, reliable → B/D, fast → X/K, calming → soft S/L/M).

Aim for **500–1000+ total ideas** before any screening. Resist the urge to evaluate during generation.

### Phase 3: Screen (the funnel)

Run candidates through these gates in order. Each gate eliminates a lot.

1. **Trademark sanity** — flag obvious conflicts (existing famous brands, identical strings in the same category). For real legal clearance the user needs a TM attorney; say so.
2. **Linguistic / cultural** — flag words that mean something bad in a major language, sound like a slur, or share a string with a known disaster/scandal. If unsure, say "verify with a native speaker of X."
3. **Processing fluency** — drop anything hard to pronounce, spell, or remember on first read. Vercel passes (ver + cel, both familiar). "Xqzlith" fails.
4. **Distinctiveness vs. landscape** — drop anything that sounds like an existing competitor or uses the category's tired vocabulary.

Output: a **shortlist of 10–15** survivors, grouped by direction.

### Phase 4: Implement (pressure-test the shortlist)

Don't ask "which do you like." Run these drills with the user:

- **Polarization check.** Show the list to 3–5 teammates. Names where opinion splits are *good signals* (Pentium story). Names everyone agrees on are usually weak.
- **Competitor drill.** For each top candidate, frame it as: "A new competitor just launched called [name]." Ask what the listener imagines. The name's job is to *fire imagination*.
- **"They're not like the other guys" test.** A winning name makes a stranger say "I don't know what they do exactly, but they're not like the others."
- **Prototype it.** Mock the name into 2–3 contexts: a logo treatment, a headline ("[Name] raises $50M Series B"), a product label. Does it carry?
- **Future-flexibility.** Will the name still work if the product pivots 15 degrees? Sonos worked because it was about *sound*, not "entertainment."

Recommend a top 3. For each, write a one-paragraph rationale the user can take to stakeholders — armor for the inevitable "I don't like it" reaction. Remind them: **boldness > comfort**. There is no power in comfort.

## When to push back on the user

If the user gravitates toward a safe descriptive name ("CodeFlow", "DataPro", "AIAssist"), gently surface the Azure-vs-CloudPro lesson and ask them to live with a bolder candidate for 24 hours before deciding. Don't be preachy — just name the pattern.

If the user is renaming an existing product, confirm the trigger fits one of Placek's three valid reasons: (1) the original was a throwaway "we just needed *something*" name; (2) the company genuinely pivoted; (3) a merger or major capability expansion. If none apply, the rename may not be worth the cost.

## Reference

[references/sound-symbolism.md](references/sound-symbolism.md) — letter-by-letter sonic and semantic associations Placek's team uses to bias name construction, plus compound/morpheme guidance and the named-examples library. Load when generating candidates or writing rationales.
