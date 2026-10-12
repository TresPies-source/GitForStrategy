# Decision 006: License and identity

**Date:** 2026-10-12
**Status:** Accepted
**Decider:** Cruz
**Related:** [Decision 001](001-pipeline-contract.md)

## Context

Version 1.0.0 was MIT-licensed under "Tres Pies Design," and its manifest named a different home from its README. The Dojo Genesis plugins are Apache-2.0 under "Dojo Genesis" at `DojoGenesis/*`. A license is a deliberate decision, not a default.

## Options considered

| Option | What you get | What you give up | Risk | Cost to undo |
|---|---|---|---|---|
| Keep MIT, align the names | The current license | A license that differs from the family's | Low | Low |
| Match the family: Apache-2.0 | One license across the family | MIT's brevity | Low | Medium |
| Change nothing yet | No decision now | Mismatched names stay | Low | Low |

### What was not chosen, and why

Keeping MIT would leave Git for Strategy as the one differently licensed member of the family.

## Decision

License under Apache-2.0, with the family's license text. Author: Dojo Genesis. Homepage and repository: `DojoGenesis/git-for-strategy`. Origin line: built by Dojo Genesis at TresPies LLC.

## Ruling

> "Match family: Apache-2.0"

— Cruz, 2026-10-12. Selected from options the agent wrote.

## Consequences

Copies taken under 1.0.0 remain MIT. Contributions from 2.0.0 on are Apache-2.0, under section 5 of the license.

### Propagation

- [x] `LICENSE` replaced with the family's Apache-2.0 text
- [x] `plugin.json`: license, author, homepage, repository
- [x] README license and origin lines
- [ ] Confirm the `DojoGenesis/git-for-strategy` mirror receives this release

## Dissent

None recorded.

## Revisit when

The family's license changes.

## Verification

Checked: the license text matches the Dojo Genesis plugins' `LICENSE` file. Not checked: whether the `DojoGenesis/git-for-strategy` mirror is in sync with this repository.
