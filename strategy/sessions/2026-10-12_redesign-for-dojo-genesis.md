# Session: Redesign for Dojo Genesis

**Date:** 2026-10-12
**Related:** [Scout](../scouts/2026-10-12_role-in-dojo-genesis.md) · [STATUS.md](../STATUS.md)

*The bookend: before the session ends, deposit what was decided, what it rests on, and what is still open.*

## Decided

Cruz ruled on six calls, each recorded as the option he selected or the words he typed:

- [Decision 001](../decisions/001-pipeline-contract.md) — "Pipeline contract"
- [Decision 002](../decisions/002-claude-code-first.md) — "Claude Code first"
- [Decision 003](../decisions/003-remove-unmeasured-outcome-claims.md) — "Remove + 'Not measured' (Recommended)"
- [Decision 004](../decisions/004-scope-of-the-artifact-contract.md) — the artifact types to add, and the material to remove
- [Decision 005](../decisions/005-seeds-and-lineage.md) — all four seed groups; keep and cite Liberation Psychology; re-ground in the documented lineage; Patricia Hill Collins
- [Decision 006](../decisions/006-license-and-identity.md) — "Match family: Apache-2.0"

## Evidence

- A review of the Dojo Genesis repositories: the practice skills now live in the library; the family leads with Claude Code; its public copy carries no unmeasured numbers.
- Claude Code 2.1.296 loaded only the commands from the 1.0.0 layout, and loads all eight commands and the hook from 2.0.0. `claude plugin validate --strict` passes.
- `gfs.py selfcheck`, the unit tests, and strict validation of `examples/` and of this workspace pass.
- Not checked: the OpenClaw mapping end to end; whether the `DojoGenesis/git-for-strategy` mirror is in sync.

## Open questions

- When, and in what form, Git for Strategy is listed in the Dojo Genesis marketplace.
- The exact wording of the two lineage seeds, pending Cruz's review.
- Contribution terms beyond Apache-2.0 section 5.

## Next move

Cruz reviews the pull request, starting with the two lineage seeds and `SPEC.md`.
