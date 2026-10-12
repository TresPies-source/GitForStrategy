# {{name}}

**Spec:** Git for Strategy {{spec}}
**Date:** {{date}}

*The front door to this workspace. Every session reads this first.*

## Orientation

<!-- What this workspace is for, in two or three sentences, and who decides here. -->

## Hot facts

<!-- The few things every session needs and keeps getting wrong. Each one checkable. -->

## Router

| Doing | Go to |
|---|---|
| Exploring a tension | `scouts/` |
| Gathering evidence | `research/` |
| Recording a call | `decisions/` |
| Writing what will be built | `specs/`, `contracts/` |
| Briefing whoever builds | `commissions/` |
| Repeating an operation | `runbooks/` |
| Checking docs against reality | `audits/` |
| Writing for the public | `drafts/` |
| Looking back on finished work | `retros/`, `seeds/` |
| Closing a session | `sessions/` |
| Where things stand | `STATUS.md` |

## Rules that bite here

- You bring the perspectives and make the calls. Agents draft, and record your rulings in your words.
- No number goes in a file unless it can be re-derived, or it says *not measured*.
- An accepted decision is superseded, never edited.

## Bookend

Before a session ends, record what was decided, the evidence, and what is still open (`gfs.py new session "<topic>"`), then update `STATUS.md`.
