---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

write a quick status update for my team slack: we finished migrating the auth service to postgres last week, went pretty smoothly, latency is way better now (p99 went from 340ms to 95ms). found 2 minor bugs after cutover, both fixed. next up is the billing service, starting nov 2.
