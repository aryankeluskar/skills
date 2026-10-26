---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Write the intro (2-3 paragraphs) for a design doc proposing we put a redis cache in front of our product catalog API. Context: catalog API peaks at ~12k req/s, about 70% of reads hit the same 500 SKUs, and postgres CPU hits 85% at peak. We had two brownouts in September.
