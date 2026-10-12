# Decision 001: Git for Strategy is the pipeline contract

**Date:** 2026-10-12
**Status:** Accepted
**Decider:** Cruz
**Related:** [Scout](../scouts/2026-10-12_role-in-dojo-genesis.md)

## Context

Version 1.0.0 shipped copies of the practice skills. The Dojo Genesis library now maintains newer versions of every one of them under the same names. What no repository owns is the pipeline's record: one place and one format for scouts, decisions, specs, commissions, retros, and seeds. The [scout](../scouts/2026-10-12_role-in-dojo-genesis.md) maps three roles.

## Options considered

| Option | What you get | What you give up | Risk | Cost to undo |
|---|---|---|---|---|
| Pipeline contract | A gap filled; nothing to drift | Technique lives in the library | Low to medium | Low |
| Canonical strategy pack | One install for the practice | A sync burden; a second home for skills | Medium | Medium |
| Method guide only | Least to maintain | No mechanism; nothing checks the record | Low | Low |

### What was not chosen, and why

The canonical pack would recreate the drift that made 1.0.0 stale. A guide alone would drop the mechanism that makes the record trustworthy.

## Decision

Git for Strategy defines the pipeline contract — invariants, artifact types, conformance levels — and implements it with templates, commands, a standard-library script, and seeds. It links to the Dojo Genesis library for practice skills and copies none.

## Ruling

> "Pipeline contract"

— Cruz, 2026-10-12. Selected from options the agent wrote.

## Consequences

The 21 skill copies are removed. `SPEC.md` becomes the source of truth. The commands point to library skills for technique.

### Propagation

- [x] `SPEC.md` written
- [x] `scripts/gfs.py` implements the contract
- [x] Skill copies removed; commands point to the library
- [ ] Listing in the Dojo Genesis marketplace — a change to that repository, not this one

## Dissent

None recorded.

## Revisit when

- The library stops maintaining a skill the commands point to.
- Another tool in the family takes over the pipeline record.

## Verification

Checked: the library holds every 1.0.0 skill under the same name. Checked: `claude plugin validate --strict` passes, and Claude Code loads all eight commands and the hook. Not checked: adoption outside this repository.
