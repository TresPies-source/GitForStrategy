---
name: two-sided-contracts
tagline: An integration contract is only as strong as its weaker side.
group: deciding
triggers:
  - integration
  - interface between
  - the other team
  - API contract
  - unblock the next phase
---

# Two-Sided Contracts

*An integration contract is only as strong as its weaker side.*

## What it is

Every integration has two sides. Finishing one side creates a false sense of completion.

## Why it matters

When one side ships and the other lags, the gap surfaces at integration — the most expensive place to find it.

## The pattern

1. Write a contract when one piece of work has to unblock another.
2. Name both sides: what the provider guarantees, what the consumer assumes.
3. Commission both sides together.
4. Close the contract only when both sides pass.

## Revisit when

A phase's exit criteria include "unblock the next phase."

## What it refuses

Declaring an integration done from one side.

## Grew from

A February 2026 release retrospective in the Dojo Genesis practice.
