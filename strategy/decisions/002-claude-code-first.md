# Decision 002: Lead with Claude Code

**Date:** 2026-10-12
**Status:** Accepted
**Decider:** Cruz
**Related:** [Scout](../scouts/2026-10-12_role-in-dojo-genesis.md) · [Decision 001](001-pipeline-contract.md)

## Context

The contract is plain files, so it works with any tool. The Dojo Genesis family presents itself as a protocol layer for Claude Code. The question was which frame the repository leads with.

## Options considered

| Option | What you get | What you give up | Risk | Cost to undo |
|---|---|---|---|---|
| Claude Code first | Fits the family; one clear install path | Other tools read as secondary | Low | Low |
| Tool-neutral first | The widest reach | A blurrier fit with the family | Medium | Low |

### What was not chosen, and why

Tool-neutral first. The contract stays portable — conformance levels L0 and L1 need no particular tool — but the README leads with the Claude Code path.

## Decision

The README and install path lead with Claude Code. Other agents are covered in `docs/adapters.md`. Naming Claude Code carries a non-affiliation line.

## Ruling

> "Claude Code first"

— Cruz, 2026-10-12. Selected from options the agent wrote.

## Consequences

The plugin is the main path. Portability is a property of the contract, not the headline.

### Propagation

- [x] README install section leads with Claude Code
- [x] `docs/adapters.md` covers other agents, the MCP server, and OpenClaw
- [x] Non-affiliation line in the README

## Dissent

None recorded.

## Revisit when

- The family's positioning changes.
- Use from other tools outgrows use from Claude Code.

## Verification

Checked: the plugin loads in Claude Code 2.1.296 with all commands and the hook. Not checked: the OpenClaw mapping end to end.
