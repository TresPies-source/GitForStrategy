# Commission: Offline checklists, first release

**Date:** 2026-03-09
**Status:** Done
**Related:** [Spec](../specs/offline-inspection-checklists.md) · [Decision 001](../decisions/001-web-first-with-offline.md)

*A self-contained brief. Whoever builds should need nothing that is not written or linked here.*

## Pre-flight

If any check fails, stop and report. Do not build on partial ground.

- [x] The spec passed the pre-commission gate.
- [x] The existing form's code has been read.
- [x] Local storage works on each inspector device model the team supports.

## Context

### Decisions already made

Web first, offline required: [Decision 001](../decisions/001-web-first-with-offline.md).

### What already exists

A web form that saves only when connected.

## Requirements

1. Cache checklists for offline use.
2. Save answers and photos locally.
3. Queue and sync changes when online, without duplicates.
4. Show each checklist's sync state.

## File manifest

| Action | Path | Why |
|---|---|---|
| Read | the existing form | Current save behavior |
| Modify | the form's save path | Save locally first |
| Create | a sync queue | Ordered, idempotent sync |

## Success criteria

- [x] Every success criterion in the spec passes on a real device with the network off.

## Constraints and non-goals

No native wrapper. No conflict resolution between inspectors.

## Done when

The builder reports which checks ran on which devices, what passed, and where the test notes are. Reported on 2026-04-03: all checks passed on the supported devices.
