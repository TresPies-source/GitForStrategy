---
name: spec-to-prompt-pipeline
tagline: A spec is not a build brief. Translate it, and check readiness first.
group: structure
triggers:
  - let's just build it
  - hand this to an agent
  - turn the spec into tasks
  - commission
  - implementation prompt
---

# Spec-to-Prompt Pipeline

*A spec is not a build brief. Translate it, and check readiness first.*

## What it is

Between an accepted spec and the build sits a translation: a self-contained commission that opens with a pre-flight. Scout, decide, spec, gate, commission — each one a file.

## Why it matters

A builder handed a spec interprets it, and the gaps fill with plausible guesses. A commission leaves less room for interpretation, and its pre-flight stops the work when grounding is missing.

## The pattern

1. Write the spec from an accepted decision.
2. Run the pre-commission gate.
3. Write the commission: context, requirements, file manifest, binary success criteria, non-goals.
4. Open it with a pre-flight that stops the build on any failed check.

## Revisit when

Work is about to go to an autonomous builder.

## What it refuses

Spec-to-code: skipping the translation and hoping the builder reads the spec the way you meant it.

## Grew from

The scout, spec, and commission pipeline as practiced across Dojo Genesis releases. Timeline claims once attached to this seed were never measured against a baseline; they have been removed.
