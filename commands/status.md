---
name: status
description: Show current pipeline state — what phase you're in, what's current, what's stale.
---

# /status

Show or update pipeline status. This is the connective tissue of the Git for Strategy pipeline.

## What This Does

1. Read the current STATUS.md (or create one if it doesn't exist)
2. Scan the pipeline directories (scouts/, specs/, commissions/, retros/) for artifacts
3. Show what phase is active, what's current, what's stale
4. Optionally update the status with new information

## How to Start

If STATUS.md exists, read it and present the current state.
If not, create one using `skills/track/status-writing/SKILL.md`.

Use status-template from `skills/track/status-template/SKILL.md` for comprehensive status documents.
Use repo-status from `skills/track/repo-status/SKILL.md` when a codebase overview is needed.

## Output

An updated STATUS.md at the project root showing:
- Current pipeline phase (Explore / Decide / Execute / Learn)
- Active artifacts and their dates
- Stale items (scouts older than 1 week without a spec, etc.)
- Open questions and blockers

## Pipeline Health Indicators

- **Healthy:** Each phase has recent artifacts, pipeline is flowing
- **Stale:** Scout exists but no spec after 1 week
- **Blocked:** Spec exists but commission failed pre-flight
- **Overdue:** Implementation shipped but no retro after 2 weeks
