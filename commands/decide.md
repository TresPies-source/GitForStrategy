---
description: "Record a decision: options considered, what was not chosen, and the ruling in the decider's own words. Drafts stay Proposed until the person rules."
argument-hint: "<the call to make, or a scout to decide from>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*)
---

Record a decision about: $ARGUMENTS

A decision record holds one call. The person rules; you draft, gather, and record.

1. **Find the workspace** (`STRATEGY.md` here or in `strategy/`). If there is none, ask before running `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" init`.
2. **Find what it grew from.** If a scout or research dossier covers this, read it and link it under Related. If an earlier decision covers the same ground, this one supersedes it: link it, and mark the old record `Superseded by <new number>` without changing anything else in it.
3. **Create the file.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" new decision "<short title>"` and fill in the file it prints.
4. **Draft** Context, Options considered (with what was not chosen and why), Decision, Consequences with a propagation checklist, and Revisit when. Record dissent if anyone disagrees, including you.
5. **Ask for the ruling.** Present the options plainly. Name a default only if every piece of evidence behind it is in hand; otherwise name the missing evidence. Then ask the person to rule.
6. **Record the ruling** under Ruling in the person's own words, with their name and today's date. Fill in Decider. Only then set Status to Accepted (or Rejected). If they have not ruled, leave Status at Proposed and the Ruling section empty. Never write your recommendation as their ruling.
7. **Verification.** Say what was checked before the ruling, and what was not.
8. **Update the record of where things stand.** Add a one-line entry to the Decision notes in `STATUS.md`: date, the ruling, a link to the record.
9. **Check your work.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" validate` and fix any error before reporting.

If the Dojo Genesis MCP server is connected and its ADR path points at this workspace's `decisions/` folder, its decision tool writes conformant records too. This command adds the ruling, options, and revisit triggers that a bare record lacks.
