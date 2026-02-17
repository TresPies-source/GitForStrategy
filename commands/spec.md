---
name: spec
description: Write a production-ready specification from a scouted direction.
---

# /spec

Write a specification. This is Phase 2 of the Git for Strategy pipeline.

## What This Does

1. Take a scouted direction (from `/scout` output or user input)
2. Ground the spec in measured reality — existing code, prior decisions, constraints
3. Write a production-ready specification with clear scope, deliverables, and success criteria
4. Save the spec to `specs/` with version number

## How to Start

Ask the user: **"Which direction are we specifying? Point me to a scout document or describe the decision."**

Then follow the specification-writer skill in `skills/decide/specification-writer/SKILL.md`.

If the user has uploaded files or wants to plan from existing documents, use context-ingestion from `skills/decide/context-ingestion/SKILL.md`.

## Output

A versioned specification saved to `specs/{name}-v{n}.md` using the template in `templates/spec_template.md`.

## After Specifying

Suggest next steps:
- `/commission` to generate implementation prompts
- `/status` to update pipeline state
