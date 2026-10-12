# Decision 004: Scope of the artifact contract

**Date:** 2026-10-12
**Status:** Accepted
**Decider:** Cruz
**Related:** [Decision 001](001-pipeline-contract.md)

## Context

Version 1.0.0 covered scouts, specs, commissions, retros, seeds, and status. The Dojo Genesis practice uses more artifact types than that. Version 1.0.0 also carried material about agent runtimes, memory policy, and handing work between agents, which is not strategy practice.

## Options considered

| Option | What you get | What you give up | Risk | Cost to undo |
|---|---|---|---|---|
| Keep the 1.0.0 types | A small contract | The types the practice actually uses | Low | Low |
| Add the practice's types; keep everything else | A wider contract | A clear boundary | Medium | Medium |
| Add the practice's types; remove what is not strategy practice | A wider contract with a clear edge | Material some readers used | Low | Low |

### What was not chosen, and why

Keeping runtime, memory-policy, and agent-handoff material would make the contract about running agents rather than recording strategy.

## Decision

The contract adds decision records, contracts, evidence dossiers, verification sections in scouts and decisions, runbooks, drift audits, drafts of public copy, a workspace front door, and session closes. Runtime-architecture notes, the agent-runtime seed patches, memory-retention material, and agent-handoff material are removed. The spec's non-goals say what the contract is not.

## Ruling

> Artifacts: "Contracts", "Evidence dossiers", "Verification sections", "Runbooks", and "Drift audits", "Public-copy drafts", "Project nexus", "Session close".
>
> Removals: "Runtime architecture docs", "Runtime seed patches", "Memory retention material", "Handoff protocol material".

— Cruz, 2026-10-12. Selected from options the agent wrote.

## Consequences

`SPEC.md` lists fourteen artifact kinds — twelve folder types plus `STATUS.md` and `STRATEGY.md` — each with a template. The Context Iceberg, Agent Workspace, and Handoff Protocol seeds are removed.

### Propagation

- [x] `SPEC.md` types table and non-goals
- [x] A template for every type, checked by `selfcheck`
- [x] Removed files listed in the changelog

## Dissent

None recorded.

## Revisit when

- Someone needs an artifact type the contract lacks, twice.
- A type sits unused across several workspaces.

## Verification

Checked: `selfcheck` renders every template and validates the output. Checked: the removed material no longer appears in the tree. Not checked: removed material still present in git history, which is unchanged.
