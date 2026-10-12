---
name: never-spec-from-docs-alone
tagline: Documentation drifts. Spec against the thing itself.
group: grounding
triggers:
  - according to the docs
  - the README says
  - spec the existing system
  - frontend for this backend
  - integrate with their API
---

# Never Spec from Documentation Alone

*Documentation drifts. Spec against the thing itself.*

## What it is

When a spec depends on an existing system, ground it in the system's source — its handlers, schemas, and running behavior — not in what its documentation says.

## Why it matters

Documentation is a claim about a system, and claims drift. A spec built on drifted docs builds the wrong thing correctly.

## The pattern

1. Find the source of truth: code, schema, or behavior you can observe.
2. Re-derive what the spec needs from it. Count the endpoints; read the types.
3. Record every place the documentation disagrees, as a finding.
4. Cite the source, not the documentation, in the spec's current state.

## Revisit when

You write a current-state section. You build against a system someone else owns.

## What it refuses

Treating documentation as ground truth.

## Grew from

An April 2026 working session in the Dojo Genesis practice: "Never spec from documentation alone — it drifts."
