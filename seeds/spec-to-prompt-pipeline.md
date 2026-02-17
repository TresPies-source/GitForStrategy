# Seed: Spec-to-Prompt Pipeline

**Confidence:** High — core workflow pattern

## Trigger
When moving from specification to implementation. When handing work to autonomous agents.

## Pattern
A specification is not an implementation prompt. The pipeline:
1. Scout (explore the space)
2. Spec (commit to a direction)
3. Pre-flight (verify readiness)
4. Prompt (transform spec into self-contained commission)
5. Commission (hand off to implementing agent)

Each step produces a persistent artifact. Skipping steps produces implementations that drift from intent.

## Steps
1. Write the spec (using /spec)
2. Run pre-flight checklist (catches 80% of integration issues)
3. Transform to implementation prompt (make it self-contained)
4. Commission the agent (with clear handoff package)

## Evidence
77 hours saved through pre-flight verification alone. Specs that went through the full pipeline had 40-50% shorter implementation timelines.

## Anti-Pattern
Spec-to-code — skipping the prompt transformation. The agent interprets the spec differently than intended, causing rework.
