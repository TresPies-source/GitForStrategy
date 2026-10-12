---
description: "Turn a Ready spec into a self-contained build brief. Runs the pre-commission gate first and stops if it fails."
argument-hint: "<spec file>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*)
---

Commission the build for: $ARGUMENTS

1. **Run the gate.** `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" gate <spec file>`. If it fails, stop. Report each failed check and what would fix it. Do not write a commission against a spec that fails the gate. If it passes with a staleness warning, re-check the spec's current state against the repository before going on.
2. **Create the file.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" new commission "<short title>"` and link the spec under Related.
3. **Pre-flight.** List the checks the builder runs before writing anything, each with a command or a place to look: files exist and have been read, dependencies are present, the spec passed its gate. State the stop rule plainly: if any check fails, stop and report.
4. **Context.** Decisions already made, with links, and what already exists in the repository.
5. **Requirements and file manifest.** What to read, modify, and create, and why for each.
6. **Success criteria.** Carry the spec's binary criteria over, and add any the build needs.
7. **Constraints and non-goals**, then **Done when**: what the builder hands back — what ran, what passed, where to look.
8. **Check your work.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" validate`. Set Status to Ready when the person agrees, and to Out when the build starts.

Building happens outside this contract, with whatever tools you use. If the Dojo Genesis `specification-driven-development` plugin is installed, its `implementation-prompt`, `pre-implementation-checklist`, and `parallel-tracks` skills cover the brief in depth.
