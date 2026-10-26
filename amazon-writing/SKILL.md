---
name: amazon-writing
description: Write in the plain, data-first style from Amazon's internal "Write Like an Amazonian" guide - short sentences, numbers instead of adjectives, no weasel words, every line passes the "so what" test. Use this for any prose the user will read or send - docs, design docs, status updates, emails, Slack messages, PR descriptions, postmortems, replies to a manager - and when editing or tightening their writing, even if they never mention Amazon or style. Also use it when the user complains that writing sounds like AI, is fluffy, or "gives them an ick".
---

# Amazon-style writing

Readers of work writing are trying to make a decision. Every rule below exists to help them make it faster: claims they can check, sentences they can parse in one pass, and nothing they have to skim past.

This style also happens to remove most of what makes text read as machine-written. Intensifiers, hedges, tidy triplets and summary paragraphs are the habits readers recognize and distrust. Writing that follows these rules does not sound like an LLM, because it does not sound like anything; it just states facts.

## The rules

1. **Keep every sentence under 30 words.** One idea per sentence. Cut wordy phrases:
   - "due to the fact that" → "because"
   - "totally lacked the ability to" → "could not"
   - "in order to" → "to"; "at this point in time" → "now"

2. **Replace adjectives and adverbs with data.** Adjectives are imprecise and do not help anyone decide.
   - "We made the performance much faster" → "We reduced server-side p90 latency from 10 ms to 1 ms"
   - "This will make the launch extremely successful" → "This will increase output by 2.5%"

3. **Eliminate weasel words.** "Nearly all", "significantly", "many", "most", "a lot", "substantially" hide the number. Use the number.
   - "Nearly all customers" → "87% of Prime members"
   - "Significantly better" → "+25 basis points"

4. **Give every metric its unit, period and baseline.** "Up 40%" means little. "Unit sales rose 40% in Q4 2011 compared to Q4 2010" means something.

5. **Pass the "so what" test.** After each sentence, ask what the reader learns or can do now. If nothing, cut it or add the consequence.

6. **Answer questions with one of four answers.** Yes. No. A number. "I don't know; I'll follow up by <when>." Put the answer first, then the one condition or caveat that matters.

## When the user did not give you the number

Do not invent data to satisfy rule 2. Making up a figure is worse than an adjective because it looks checkable. Instead:
- use the numbers the user gave, all of them, exactly;
- if a claim needs a number you don't have, state the claim plainly without the intensifier ("latency improved"), or leave a visible gap like `[p99 before/after?]` and mention it in one line to the user.

## Things that read as AI filler - leave them out

These add length, not information. Readers notice them and stop trusting the rest:

- Openers and closers: "Great question", "I hope this helps", "In summary", "Overall", "Let me know if you have any questions", "This document outlines…"
- Hype and filler words: delve, leverage, robust, seamless, crucial, pivotal, game-changer, cutting-edge, streamline, unlock, empower, "it's worth noting", "in today's fast-paced world"
- Sincerity markers: honestly, genuinely, truly, straightforward
- Reflexive triplets ("fast, reliable, and scalable") when the facts don't come in threes
- "Not just X, but Y" and other set-up/pay-off constructions
- Em dashes used as decoration; use a period or a comma
- Headings, bold and bullets on a message that is three sentences long
- Restating the question before answering it

## Shape

- Lead with the answer or the decision. Background comes after, if at all.
- Match length to the ask. A status update is a few sentences, not a report. A Slack reply is one to three lines.
- Prose for reasoning; bullets only for parallel items (a list of risks, a list of steps).
- Write as the user would. If they will send it as themselves, use first person and their register.

## Editing someone's draft

Apply the rules in place and keep their meaning and voice. Don't add claims they didn't make. If a vague phrase needs a number you don't have, mark it (`[number?]`) rather than guessing. Briefly list the kinds of changes you made only if they ask.

## Quick self-check before sending

- Any sentence over 30 words? Split it.
- Any "very", "significantly", "nearly", "extremely", "much"? Replace with the number or delete.
- Every number from the user included, with its unit?
- First sentence states the point?
- Any sentence that fails "so what"? Cut it.
