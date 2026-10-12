---
name: ship-coupled-work-together
tagline: When two deliverables will integrate at once, ship them together.
group: execution
triggers:
  - blocked by
  - sequence these
  - depends on the previous phase
  - mock the interface
---

# Ship Coupled Work Together

*When two deliverables will integrate at once, ship them together.*

## What it is

Two pieces of work planned in sequence, where the second integrates with the first right away, are often better shipped as one release.

## Why it matters

Delivering coupled work in sequence creates an artificial integration gap, and the second piece gets tested against stand-ins instead of the real thing.

## The pattern

1. For each "blocked by" link, ask whether the two pieces share a test surface.
2. If they do, plan them as one release.
3. Test the second piece against the real first one, not a stand-in.

## Revisit when

Two commissions have a "blocked by" relationship.

## What it refuses

Sequencing for neatness when the work is coupled.

## Grew from

A February 2026 release retrospective in the Dojo Genesis practice.
