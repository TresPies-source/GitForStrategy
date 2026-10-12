---
name: spec-quality-paradox
tagline: The better the spec, the easier it is to fake grounding.
group: execution
triggers:
  - the spec is great
  - high compliance
  - it matches the spec
  - review passed
---

# The Spec-Quality Paradox

*The better the spec, the easier it is to fake grounding.*

## What it is

A detailed spec lets a builder produce work that restates the spec in code without touching the real system. High compliance scores can hide it.

## Why it matters

Spec quality is usually counted only as a strength. It is also a risk.

## The pattern

1. In review, ask: is this grounded in the referenced files, or is it the spec paraphrased?
2. Check a few claims against the actual codebase.
3. Treat spec-paraphrase as a finding.

## Revisit when

You review work that matches its spec suspiciously well.

## What it refuses

Treating compliance as proof of grounding.

## Grew from

A February 2026 release retrospective in the Dojo Genesis practice.
