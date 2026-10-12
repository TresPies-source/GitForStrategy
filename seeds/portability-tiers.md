---
name: portability-tiers
tagline: Classify what you build by how deep its dependencies go.
group: structure
triggers:
  - will this work elsewhere
  - portable
  - cross-platform
  - vendor lock-in
  - which tools does this need
---

# Portability Tiers

*Classify what you build by how deep its dependencies go.*

## What it is

Sort components by dependency depth:

- **Tier 1** needs nothing beyond files.
- **Tier 2** needs common tools, reached through thin adapters.
- **Tier 3** needs a particular host's abstractions.
- **Tier 4** is locked to one host.

## Why it matters

Portability decided late is expensive. Knowing each piece's tier tells you what travels, what needs an adapter, and what to keep small.

## The pattern

1. List the components.
2. Give each the tier of its deepest dependency.
3. Keep the core in the lowest tier you can.
4. Put host-specific parts behind thin adapters.

## Revisit when

You decide where a method or tool should run. You add a dependency to something meant to travel.

## What it refuses

Assuming portability — "it's just markdown" — without checking what each piece actually needs.

## Grew from

Classifying a practice library for use across several agent hosts in the Dojo Genesis practice. Git for Strategy's conformance levels apply it.
