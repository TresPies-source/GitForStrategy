---
description: "Show where the strategy pipeline stands, what is stale, and what needs attention. Counts come from disk, not memory."
argument-hint: "[--root DIR]"
allowed-tools: Read, Edit, Glob, Grep, Bash(python3:*)
---

!`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" status $ARGUMENTS 2>&1 || true`

The report above came from the files on disk. Use its numbers; do not restate counts from memory.

1. If it says there is no workspace, offer to create one with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" init`, and ask first.
2. Summarize in plain words: which phase the work is in, what is stale, and each item under "Needs attention" with the move that would resolve it.
3. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" validate` and report any errors alongside the status.
4. Offer to update the Where we are section of `STATUS.md`. Write it only if the person says yes, and keep it a pointer to the record, not a snapshot of counts.
