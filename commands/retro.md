---
description: "Run a retrospective on a closed stretch of work: what went well, what was hard, what to change, the seeds it grew, and actions that carry forward."
argument-hint: "<the work or period to look back on>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*)
---

Run a retro on: $ARGUMENTS

1. **Check the period is closed.** A retro covers work that shipped or was abandoned. If the work is still moving, say so and offer `/status` or `/close` instead.
2. **Create the file.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" new retro "<short title>"`, fill in Period, and link the commissions, specs, and decisions it covers under Related.
3. **Gather the record.** Read the linked files and what actually happened in the repository. Use what the record shows, not what anyone remembers.
4. **Ask before you write.** Ask the person what went well, what was hard, and what they would change. Their account leads; add what the record shows that they did not mention, marked as yours.
5. **Themes.** Insight, evidence, and the action each one calls for. Every friction point maps to an action.
6. **Seeds.** Name patterns worth reusing: what was seen, why it matters, when to revisit. For each one the person wants kept, run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" new seed "<name>"`, fill it in, and say in Grew from that it came from this retro.
7. **Actions.** At least one carries into the next stretch of work.
8. **Check your work.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" validate`. Set Status to Closed when the person agrees.

If the Dojo Genesis `continuous-learning` and `wisdom-garden` plugins are installed, their `retrospective` and `seed-extraction` skills go deeper on technique.
