# Scout: Role in Dojo Genesis

**Date:** 2026-10-12
**Status:** Decided
**Related:** [Decision 001](../decisions/001-pipeline-contract.md) · [Decision 002](../decisions/002-claude-code-first.md)

*A copy of the practice, or the home for its record.*

## Tension

The tension is between Git for Strategy as a self-contained package of strategy skills — easy to install, complete on its own — and Git for Strategy as one part of the Dojo Genesis family, which already maintains those skills and keeps improving them. Cruz asked for a redesign that fits Git for Strategy into the Dojo Genesis experience.

## Routes

These routes were proposed by the agent from a review of the Dojo Genesis repositories. Cruz chose among them.

### Route 1: Pipeline contract

- **What it looks like:** Stop copying skills. Define the file contract that strategy work lands in — invariants, artifact types, conformance levels — with templates, commands, a small script, and seeds. Point to the Dojo Genesis library for the skills.
- **What you gain:** Fills a gap nobody owns: one place and one format for the pipeline's record. Nothing left to drift.
- **What you give up:** The repository is no longer complete on its own for technique; that lives in the library.
- **Risk:** Low to medium. The contract has to earn adoption.
- **Rough size:** Medium.

### Route 2: Canonical strategy pack

- **What it looks like:** Make this repository the canonical home of the strategy skills, refreshed to current versions, and list it in the marketplace as their source.
- **What you gain:** One install for the whole strategy practice.
- **What you give up:** A sync burden between two repositories, and a second home for skills the library already maintains.
- **Risk:** Medium. Drift returns unless the sync is checked.
- **Rough size:** Medium, then ongoing.

### Route 3: Method guide only

- **What it looks like:** A readable guide and copy-paste templates, with no plugin.
- **What you gain:** The smallest thing to maintain.
- **What you give up:** No mechanism. Nothing checks the record.
- **Risk:** Low.
- **Rough size:** Small.

## Cross-route patterns

On every route the 1.0.0 skill copies go, because the library holds newer versions under the same names. On every route the outcome numbers need a source or have to go.

## Open questions

1. Which frame leads: Claude Code, or tool-neutral portability? Settled in [Decision 002](../decisions/002-claude-code-first.md).
2. When will Git for Strategy be listed in the Dojo Genesis marketplace? Open.

## Default

The agent named no default for the role. The evidence about fit with the family was in hand, but the role is an identity call that belongs to Cruz.

## Verification

Checked: every 1.0.0 skill exists under the same name in the Dojo Genesis library (`DojoGenesis/plugins`). Checked: Claude Code 2.1.296 loaded only the seven commands from the 1.0.0 layout — none of the nested skills, and no hooks. Not checked: whether other editors would have loaded the nested skills.
