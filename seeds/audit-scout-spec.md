---
name: audit-scout-spec
tagline: Audit before you scout. Scout before you spec.
group: grounding
triggers:
  - spec the next phase
  - touches existing code
  - where do we start
  - we already know what to build
  - estimate this
---

# Audit, Then Scout, Then Spec

*Audit before you scout. Scout before you spec.*

## What it is

The pipeline with the least waste runs audit (gather the data), then scout (analyze the routes), then decide, then spec. Each stage hands the next a better input.

## Why it matters

Skipping the audit means the scout is guessing. Skipping the scout means the spec is ungrounded. The quality of a spec is downstream of the quality of the decision, which is downstream of the quality of the data.

## The pattern

1. Audit what exists.
2. Scout routes with the audit in hand.
3. Decide.
4. Spec from the decision and the audit together.

## Revisit when

You specify anything that touches existing code or content.

## What it refuses

Starting at the spec because the answer feels obvious.

## Grew from

A February 2026 specification retrospective in the Dojo Genesis practice.
