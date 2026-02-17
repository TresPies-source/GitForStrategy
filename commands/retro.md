---
name: retro
description: Run a structured retrospective on completed work — harvest learnings and extract seeds.
---

# /retro

Run a retrospective. This is Phase 4 of the Git for Strategy pipeline.

## What This Does

1. Reflect on completed work: what went well, what was hard, what to change
2. Extract reusable patterns as seed patches
3. Compress session context into memory artifacts for future reference
4. Save the retrospective to `retros/`

## How to Start

Ask the user: **"What work are we reflecting on? Point me to the spec and any implementation notes."**

Then:
1. Run retrospective from `skills/learn/retrospective/SKILL.md`
2. If patterns emerge, run seed-extraction from `skills/learn/seed-extraction/SKILL.md`
3. Optionally compress context using compression-ritual from `skills/learn/compression-ritual/SKILL.md`

## Output

- Retrospective saved to `retros/YYYY-MM-DD-{topic}.md` using template in `templates/retro_template.md`
- Any extracted seeds saved to `seeds/` using template in `templates/seed_template.md`

## After Retrospective

The pipeline loops back to Explore:
- `/scout` to begin the next cycle
- `/status` to update pipeline state
