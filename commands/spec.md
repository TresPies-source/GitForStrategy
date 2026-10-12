---
description: "Write a spec from an accepted decision, grounded in a measured current state, with binary success criteria and explicit non-goals."
argument-hint: "<what will be built, or the decision to spec from>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*)
---

Write a spec for: $ARGUMENTS

1. **Find the workspace** (`STRATEGY.md` here or in `strategy/`). If there is none, ask before running `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" init`.
2. **Find the decision.** A spec implements an Accepted decision. If there is none, say so and offer `/decide` first. If the person wants to go ahead anyway, label the spec as exploration in its one-line summary.
3. **Create the file.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" new spec "<short title>"` and link the decision under Related.
4. **Measure the current state.** Read the real repository: the files, counts, and behavior this spec touches. Never spec from documentation alone; where docs and code disagree, record the disagreement. Re-derive every number you write down.
5. **Write** Problem, Scope (in and out), Design, Non-goals, and Risks. Write each success criterion as a binary checkbox (`- [ ] ...`) that a check can pass or fail.
6. **Contracts.** If this work has to unblock other work, or meets another piece of work at an interface, write a contract for each meeting point (`gfs.py new contract`) and link it.
7. **Open questions** go in their own section. Don't resolve them by guessing.
8. **Check your work.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" validate`. Set Status to Ready only when the person agrees the spec is ready, then run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" gate <spec file>` and report the result.

If the Dojo Genesis `specification-driven-development` plugin is installed, its `specification-writer` and `codebase-audit-grounding` skills go deeper on technique.
