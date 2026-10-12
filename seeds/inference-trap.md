---
name: inference-trap
tagline: A guess that looks correct is worse than a visible failure.
group: grounding
triggers:
  - the agent filled in the gaps
  - looks right but
  - missing context
  - hand this to an agent
  - it compiled
---

# The Inference Trap

*A guess that looks correct is worse than a visible failure.*

## What it is

When a builder is missing grounding but holds a detailed brief, it does not fail visibly. It infers something plausible. The result passes a surface review and is not grounded in the real system.

## Why it matters

This failure scales the wrong way: the better your specs get, the harder it is to catch.

## The pattern

1. Have the builder confirm access to every file it depends on before it starts.
2. Treat "plausible but ungrounded" as a failure mode of its own, and test for it.
3. Prefer a hard stop to a guess.

## Revisit when

You write any brief for an autonomous builder. Work passes review faster than it should.

## What it refuses

Silent inference: filling a gap instead of reporting it.

## Grew from

A February 2026 release retrospective in the Dojo Genesis practice, after builders worked from inferred context that review then had to unwind.
