# Spec: Offline inspection checklists

**Date:** 2026-03-06
**Updated:** 2026-04-06
**Status:** Shipped
**Owner:** Product lead (illustrative)
**Related:** [Decision 001](../decisions/001-web-first-with-offline.md)

*An inspector can open, fill in, and save a checklist with no connection, and it syncs when signal returns.*

## Problem

Inspectors lose work when signal drops partway through a checklist, and then re-enter it from memory.

## Current state

The existing web form saves only when connected. There is no local storage and no sync. Checked against the form's code on 2026-03-06.

## Scope

### In

- Open checklists while offline.
- Save answers and photos locally.
- Sync when a connection returns, and show the sync state.

### Out

- Editing checklist templates while offline.
- Native wrappers.

## Design

Store answers and photos on the device. Queue changes. Sync in order when online, and show each checklist's state: saved on this device, syncing, or synced.

## Success criteria

- [x] A checklist opened online can be completed and saved with the network off.
- [x] Saved work survives closing and reopening the app while offline.
- [x] Work saved offline appears on the server after reconnecting, without duplicates.
- [x] Each checklist shows its sync state.

## Non-goals

- Conflict resolution between two inspectors editing the same checklist.

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Browser storage limits on older devices | Medium | High | Test on the inspectors' own devices in pre-flight |
| Duplicate records after a retried sync | Medium | Medium | Idempotent sync keyed by checklist and answer |

## Open questions

None open at ship time.
