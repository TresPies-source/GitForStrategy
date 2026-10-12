# Field Checklists

**Spec:** Git for Strategy 1.0
**Date:** 2026-03-02

*An illustrative workspace, not a real project. It shows one tension carried from scout to seeds.*

## Orientation

A small team is building a checklist app for building inspectors. This workspace holds the strategy behind it. The product lead makes the calls.

## Hot facts

- Inspectors often work where there is no signal. See the [research dossier](research/2026-03-03_where-inspectors-work.md).
- The platform call is made: web first, offline required. See [Decision 001](decisions/001-web-first-with-offline.md).

## Router

| Doing | Go to |
|---|---|
| Exploring a tension | `scouts/` |
| Gathering evidence | `research/` |
| Recording a call | `decisions/` |
| Writing what will be built | `specs/` |
| Briefing whoever builds | `commissions/` |
| Looking back on finished work | `retros/`, `seeds/` |
| Closing a session | `sessions/` |
| Where things stand | [STATUS.md](STATUS.md) |

## Rules that bite here

- The product lead makes the calls. Agents draft, and record rulings in the lead's words.
- No number goes in a file unless it can be re-derived, or it says *not measured*.
- An accepted decision is superseded, never edited.

## Bookend

Before a session ends, record what was decided, the evidence, and what is still open in `sessions/`, then update [STATUS.md](STATUS.md).
