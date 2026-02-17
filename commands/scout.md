---
name: scout
description: Start a strategic scout — explore tensions and map multiple routes before deciding.
---

# /scout

Begin a strategic scout. This is Phase 1 of the Git for Strategy pipeline.

## What This Does

1. Frame a strategic tension (not a problem to solve — a tension to hold open)
2. Scout 3-5 distinct routes with tradeoffs for each
3. Identify cross-route patterns and open questions
4. Save the scout to `scouts/` with today's date

## How to Start

Ask the user: **"What tension are you exploring?"**

Then follow the strategic-scout skill in `skills/explore/strategic-scout/SKILL.md`.

## Output

A dated scout document saved to `scouts/YYYY-MM-DD-{topic}.md` using the template in `templates/scout_template.md`.

## After Scouting

Suggest next steps:
- `/scout` again with iterative-scouting if the first pass raised deeper questions
- `/spec` to commit to a direction and write a specification
- `/status` to update pipeline state
