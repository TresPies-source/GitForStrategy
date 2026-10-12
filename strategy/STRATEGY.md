# Git for Strategy

**Spec:** Git for Strategy 1.0
**Date:** 2026-10-12

*This repository's own workspace. Changes to the contract start here, as a scout and a decision.*

## Orientation

This workspace holds the strategy behind Git for Strategy itself: why it exists in the form it does, and the calls that shaped each release. Cruz decides here.

## Hot facts

- Git for Strategy is the pipeline contract for Dojo Genesis practice. It ships no practice skills. See [Decision 001](decisions/001-pipeline-contract.md).
- No outcome numbers in any file without a source. See [Decision 003](decisions/003-remove-unmeasured-outcome-claims.md).
- `SPEC.md` at the repository root is the source of truth. `scripts/gfs.py` implements it, and CI checks both.

## Router

| Doing | Go to |
|---|---|
| Exploring a tension | `scouts/` |
| Recording a call | `decisions/` |
| Closing a session | `sessions/` |
| Where things stand | [STATUS.md](STATUS.md) |
| The contract itself | [SPEC.md](../SPEC.md) |

## Rules that bite here

- Cruz makes the calls. Agents draft, and record rulings in his words.
- No number goes in a file unless it can be re-derived, or it says *not measured*.
- An accepted decision is superseded, never edited.
- A change to `SPEC.md` ships with matching changes to `scripts/gfs.py`, the templates, and the tests.

## Bookend

Before a session ends, record what was decided, the evidence, and what is still open in `sessions/`, then update [STATUS.md](STATUS.md).
