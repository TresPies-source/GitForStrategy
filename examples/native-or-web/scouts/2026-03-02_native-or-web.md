# Scout: Native app or web app

**Date:** 2026-03-02
**Status:** Decided
**Related:** [Decision 001](../decisions/001-web-first-with-offline.md) · [Research](../research/2026-03-03_where-inspectors-work.md)

*Reach and speed of change, against reliability where the work happens.*

## Tension

The tension is between reaching every inspector quickly and changing the product often (a web app), and working reliably in basements and plant rooms with full use of the device (a native app). In the product lead's words: "I want to ship weekly, but an inspector can't lose a checklist halfway down a stairwell."

## Routes

### Route 1: Native apps on both mobile systems

- **What it looks like:** Two native apps, distributed through the app stores.
- **What you gain:** Offline storage and camera access with no compromise.
- **What you give up:** Speed of change; store review on every release; two codebases.
- **Risk:** Medium. The team has not shipped native before.
- **Rough size:** Large.

### Route 2: Web app with offline support

- **What it looks like:** One web app that installs to the home screen and keeps working without a connection.
- **What you gain:** One codebase, weekly releases, no store review.
- **What you give up:** Some device features; offline behavior varies by browser.
- **Risk:** Medium. Offline sync is the hard part.
- **Rough size:** Medium.

### Route 3: Web app now, native shell later

- **What it looks like:** Route 2, with a thin native wrapper added only if device needs outgrow the browser.
- **What you gain:** Route 2's speed, with a way out.
- **What you give up:** A second migration later, if the way out is needed.
- **Risk:** Low to medium.
- **Rough size:** Medium now, more later.

## Cross-route patterns

Offline reliability is required on every route. The routes differ in who carries that burden: the platform, or the team.

## Open questions

1. How often do inspectors actually lose signal? Answered in the [research dossier](../research/2026-03-03_where-inspectors-work.md).
2. Which device features does the first release truly need?

## Default

No default at the time of scouting. The deciding evidence was how often inspectors work without signal; the research dossier gathered it.

## Verification

Checked: the team's past releases (all web). Not checked: browser offline support on the inspectors' actual devices. The commission's pre-flight carried that check.
