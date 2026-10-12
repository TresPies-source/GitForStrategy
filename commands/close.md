---
description: "Close a working session: record what was decided, the evidence, what is still open, and the next move, then update STATUS.md."
argument-hint: "<what this session was about>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*)
---

Close this session: $ARGUMENTS

1. **Find the workspace** (`STRATEGY.md` here or in `strategy/`). If there is none, ask before running `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" init`.
2. **Create the file.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" new session "<short title>"`.
3. **Decided.** Only rulings the person actually made this session, in their words, linked to decision records. If a ruling has no record yet, offer `/decide` for it. If nothing was decided, write "Nothing decided." Do not promote your own leans to decisions.
4. **Evidence.** What those decisions rest on: files read, checks run, sources. Say plainly what was not checked.
5. **Open questions.** Everything still unresolved, each with what would resolve it.
6. **Next move.** One clear next move, or two to four options for the person to choose between.
7. **Status.** Add any new rulings to Decision notes in `STATUS.md`, and update Next.
8. **Check your work.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" validate` and fix any error before reporting.
