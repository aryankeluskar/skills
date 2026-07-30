---
name: explain
description: Use when the user asks for a rich explanation of anything they are working on — a project, folder, system, concept, codebase area, or code change. Produces HTML output with quizzes and interactive micro-worlds. Prefer this over explain-diff when the scope is broader than a single diff/PR.
---

# Explain

Please make me a rich, interactive explanation of the specified subject — a project, folder, system, concept, codebase area, diff, branch, PR, or whatever I point you at.

Do not be shy about using or consuming tokens. Thorough explanations amortize effort and token usage: a deep explainer that actually builds lasting understanding is worth far more than a thin summary that leaves cognitive debt. Explore broadly, write fully, and prefer depth over brevity.

It should have these sections:

- Background: Explain the existing system relevant to this subject. (You should broadly explore surrounding code and context for this.) We don't know how much the reader already knows, so include a deep background for beginners (note that it can be skipped if the reader is already familiar), and then a more narrow background directly relevant to the subject.
- Intuition: Explain the core intuition. The focus here is to explain the essence, not the full details. Use concrete examples with toy data. Use figures and diagrams liberally.
- Code: Do a high-level literate walkthrough of the relevant code (or of the changes, if explaining a diff). Group/order things in an understandable way — prose before each file or unit, in the right teaching order, not just a raw dump of files.
- Micro-world: Build a small interactive playground the reader can inhabit to get an intuitive feel for how the thing works — deeper and richer than a written document alone. This is inspired by Seymour Papert's "mathland": the point isn't shipping software, it's building a little world where understanding clicks by doing. Examples: a scrubbable timeline of internal state, a simplified simulation you can poke at, a step-through of a migration or algorithm with visible state. Use interactivity tastefully — not as decorative slop, but where fiddling provides understanding that's hard to get from static pictures. Embed it in the same HTML page (canvas, SVG, plain JS is fine).
- Quiz: Come up with five questions that test the reader's knowledge of this subject. This should be medium difficulty, difficult enough that you actually need to understand the substance to answer them, but not gotchas. The goal is to help the reader make sure that they've actually understood — a speed regulator so we move at the speed of understanding, not just correctness. These should be presented as interactive multiple-choice questions, and when the user clicks, it tells them whether they were correct and gives feedback.

Format:

- Output a single self-contained HTML file which includes CSS and JavaScript. Make the whole thing one long page with section headers and a table of contents. Don't use tabs for the top-level structure. Basic responsive styling so you can view it on a phone is nice too. Put the file in a global place on my computer outside of the code repo, and make sure the filename always starts with today's date in `YYYY-MM-DD-` format, because it helps keep the files time-sorted and out of version control. For example: /tmp/2026-01-12-explanation-<slug>.html
- Please write with the clarity and flow of Martin Kleppmann, making it engaging and written in classic style. Transitions between sections should be smooth.
- Some tips on diagrams. Ideally, you should pick a small number of diagram families that can be reused throughout the explanation to explain various cases. Some useful kinds of diagrams:
  - A very simplified version of the UI that the user sees in the app, to explain UI changes or surfaces.
  - A system diagram showing data flow or communication between components. Make sure to include example data here!
- Don't use ASCII diagrams. Always use simple HTML designs for your diagrams, HTML lists for lists of things, etc.
  - For code blocks, always use `<pre>` tags. If you use a custom styled div instead, it **must** have
    `white-space: pre-wrap` in its CSS, or the browser will collapse all newlines into a single line.
    Before saving the file, scan each code block in the HTML source and confirm its CSS includes
    `white-space: pre` or `pre-wrap`.
- Use callouts for key concepts or definitions, important edge cases, etc.
