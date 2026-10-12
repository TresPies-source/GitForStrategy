---
name: stubs-are-lies
tagline: A visible gap is honest. A stub that looks finished is not.
group: honesty
triggers:
  - we'll implement it later
  - placeholder
  - stub
  - mock it for now
  - not supported yet
---

# Stubs Are Lies

*A visible gap is honest. A stub that looks finished is not.*

## What it is

A piece that compiles but cannot do its job on its own creates false confidence. When something is missing, make the gap visible — an explicit "not implemented" — instead of faking it or leaving it out without a word.

## Why it matters

Hidden gaps get built on. Visible gaps get fixed.

## The pattern

1. If a part cannot stand on its own, mark it internal until it can.
2. If a capability is missing, say so explicitly where its caller will see it, with the reason.
3. Track each gap where the next spec will find it.

## Revisit when

A module is "planned for future extraction." An interface lacks something its consumer needs.

## What it refuses

Faking it, and silent omission.

## Grew from

A runtime release retrospective and a later working session in the Dojo Genesis practice, 2026, where a service answered "not implemented" on purpose rather than pretend.
