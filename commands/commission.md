---
name: commission
description: Generate implementation prompts from a specification for autonomous agents.
---

# /commission

Commission implementation. This is Phase 3 of the Git for Strategy pipeline.

## What This Does

1. Take a completed specification (from `/spec` output)
2. Run the pre-implementation checklist to verify readiness
3. Transform the spec into structured, self-contained implementation prompts
4. Optionally split into parallel tracks for concurrent execution
5. Save prompts to `commissions/`

## How to Start

Ask the user: **"Which spec are we commissioning? Point me to a spec document."**

Then:
1. Run pre-implementation-checklist from `skills/execute/pre-implementation-checklist/SKILL.md`
2. If the checklist passes, run implementation-prompt from `skills/execute/implementation-prompt/SKILL.md`
3. If the work can be parallelized, use parallel-tracks from `skills/execute/parallel-tracks/SKILL.md`

## Output

Implementation prompts saved to `commissions/{spec-name}/` using the template in `templates/commission_template.md`.

## After Commissioning

Suggest next steps:
- Hand off to implementation agents (use handoff-protocol if needed)
- `/status` to update pipeline state
- After implementation completes: `/retro`
