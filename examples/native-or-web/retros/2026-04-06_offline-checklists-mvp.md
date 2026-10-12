# Retro: Offline checklists, first release

**Date:** 2026-04-06
**Status:** Closed
**Period:** 2026-03-02 to 2026-04-03
**Related:** [Commission](../commissions/2026-03-09_offline-checklists-mvp.md) · [Spec](../specs/offline-inspection-checklists.md)

*Run on a closed stretch of work, shipped or abandoned.*

## What went well

Testing on the inspectors' own devices in pre-flight caught a storage limit before any code depended on it.

## What was hard

Sync without duplicates took longer than planned.

## What we would change

Ask where the work happens before the first scout, not after it.

## Themes

| Theme | Insight | Evidence | Action |
|---|---|---|---|
| Environment first | Where the work happens decided the platform | The research dossier answered the scout's deciding question | Plant a seed |
| Sync is the product | Offline sync was most of the risk | The sync work ran longest | Spec sync behavior first next time |

## Seeds

Ask where the work happens before choosing where the software runs. Planted as [ask-where-the-work-happens](../seeds/ask-where-the-work-happens.md).

## Actions

- [ ] Scout photo capture against Decision 001's revisit triggers.
- [ ] Measure how often signal drops in the field, which the research described but did not measure.
