# Decision 001: Web first, offline required

**Date:** 2026-03-04
**Status:** Accepted
**Decider:** Product lead (illustrative)
**Related:** [Scout](../scouts/2026-03-02_native-or-web.md) · [Research](../research/2026-03-03_where-inspectors-work.md)

## Context

The [scout](../scouts/2026-03-02_native-or-web.md) mapped three routes. The [research](../research/2026-03-03_where-inspectors-work.md) showed inspectors work without signal often enough that offline is a requirement, and that the camera is the only device feature anyone asked for.

## Options considered

| Option | What you get | What you give up | Risk | Cost to undo |
|---|---|---|---|---|
| Native apps | Full offline and device access | Weekly releases; one codebase | Medium | High |
| Web app with offline support | One codebase, weekly releases | Some device features | Medium | Medium |
| Web now, native shell later | Web's speed, with a way out | A later migration, if needed | Low to medium | Low |

### What was not chosen, and why

Native apps: the device needs found so far do not justify giving up weekly releases. A native shell stays available as the way out.

## Decision

Build a web app that works fully offline. Add a native shell only if a revisit trigger fires.

## Ruling

> "Web first, but offline is not optional. If an inspector loses a checklist in a basement, we've failed."

— Product lead (illustrative), 2026-03-04

## Consequences

Offline sync becomes the riskiest part of the first release and gets tested first. Device features beyond the camera wait.

### Propagation

- [x] Spec written: [offline inspection checklists](../specs/offline-inspection-checklists.md)
- [x] STATUS.md decision notes updated

## Dissent

The engineer who preferred native noted that offline storage limits in mobile browsers are not well documented. Kept as a revisit trigger.

## Revisit when

- Inspectors need a device feature the browser cannot reach.
- Offline storage limits cause lost work in the field.

## Verification

Checked: the research dossier's claims and the team's release history. Not checked: storage limits on the inspectors' devices, which went into the commission's pre-flight.
