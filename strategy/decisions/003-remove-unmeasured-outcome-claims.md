# Decision 003: Remove unmeasured outcome claims

**Date:** 2026-10-12
**Status:** Accepted
**Decider:** Cruz
**Related:** [Decision 001](001-pipeline-contract.md)

## Context

Version 1.0.0 led with figures for timeline reduction, hours saved, and fewer revision cycles. None of them was measured against a baseline. The Dojo Genesis family's rule is that no public number appears without a re-derivable source, a test, or a measurement designed in advance.

## Options considered

| Option | What you get | What you give up | Risk | Cost to undo |
|---|---|---|---|---|
| Remove, and say "not measured" | Every remaining claim holds up | Headline numbers | Low | Low |
| Keep as corrected field notes | Some of the history | A number readers may still quote as a result | Medium | Low |
| Remove, and ship an evaluation plan | A path to a real number | More to build now | Low | Low |

### What was not chosen, and why

Field notes would keep numbers in circulation that were never results. An evaluation plan is worth doing once there is someone to run it; until then the README says how one would measure.

## Decision

Remove every outcome figure. The README's "Not measured" section says so plainly and describes a fair measurement. Seeds lose their unsourced figures too.

## Ruling

> "Remove + 'Not measured' (Recommended)"

— Cruz, 2026-10-12. Selected from options the agent wrote. The "(Recommended)" tag is the agent's, part of the option label.

## Consequences

The README has no headline numbers. Wherever the docs state how many invariants there are, `selfcheck` re-derives the number from `SPEC.md`.

### Propagation

- [x] README "Not measured" section
- [x] Outcome figures removed from the README, docs, and seeds
- [x] `docs/measured-outcomes.md` removed

## Dissent

None recorded.

## Revisit when

A with/without measurement has been designed in advance, run, and published.

## Verification

Checked: no outcome figures remain in the repository's prose. Not checked: copies of the old figures on other sites.
