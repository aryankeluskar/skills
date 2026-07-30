---
name: explain-notion
description: Use when the user asks for a rich explanation of anything they are working on — a project, folder, system, concept, codebase area, or code change — as a Notion page. Prefer this over explain-diff-notion when the scope is broader than a single diff/PR.
---

# Explain

Please make me a rich, interactive explanation of the specified subject — a project, folder, system, concept, codebase area, diff, branch, PR, or whatever I point you at — as a Notion page.

Do not be shy about using or consuming tokens. Thorough explanations amortize effort and token usage: a deep explainer that actually builds lasting understanding is worth far more than a thin summary that leaves cognitive debt. Explore broadly, write fully, and prefer depth over brevity.

It should have these sections:

- Background: Explain the existing system relevant to this subject. (You should broadly explore surrounding code and context for this.) We don't know how much the reader already knows, so include a deep background for beginners (note that it can be skipped if the reader is already familiar), and then a more narrow background directly relevant to the subject.
- Intuition: Explain the core intuition. The focus here is to explain the essence, not the full details. Use concrete examples with toy data. Use figures and diagrams liberally.
- Code: Do a high-level literate walkthrough of the relevant code (or of the changes, if explaining a diff). Group/order things in an understandable way — prose before each file or unit, in the right teaching order, not just a raw dump of files.
- Micro-world: Build a small interactive playground the reader can inhabit to get an intuitive feel for how the thing works — deeper and richer than a written document alone. This is inspired by Seymour Papert's "mathland": the point isn't shipping software, it's building a little world where understanding clicks by doing. Examples: a scrubbable timeline of internal state, a simplified simulation you can poke at, a step-through of a migration or algorithm with visible state. Use interactivity tastefully — not as decorative slop, but where fiddling provides understanding that's hard to get from static pictures. Prefer Notion HTML/embed blocks when available so the simulation lives in the page; otherwise describe the micro-world clearly and link out to a self-contained HTML file if needed.
- **Quiz**: Come up with 5 questions that test the reader's knowledge of this subject. This should be medium difficulty, difficult enough that you actually need to understand the substance to answer them, but not gotchas. The goal is to help the reader make sure that they've actually understood — a speed regulator so we move at the speed of understanding, not just correctness. Each question should have some multiple choice answers with an explanation detailing why an answer is correct or incorrect. Use toggle blocks to represent this. For example:
  ```markdown
  1. Question
     ▶ Option 1
      ❌ Explanation for why it was incorrect
     ▶ Option 2
      ❌ Explanation for why it was incorrect
     ▶ Option 3
      ✅ Explanation for why it was correct
     ▶ Option 4
       ❌ Explanation for why it was incorrect
  2. Question
     ...
  ```

Format:

- Use the Notion MCP tools to create a new page and return the URL of the new page.
- Please write with the clarity and flow of Martin Kleppmann, making it engaging and written in classic style. Transitions between sections should be smooth.
- Some tips on diagrams. Ideally, you should pick a small number of diagram families that can be reused throughout the explanation to explain various cases. Make sure to include example data!
- Use callouts for key concepts or definitions, important edge cases, etc.
