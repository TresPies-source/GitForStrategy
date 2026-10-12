---
description: "Suggest the seeds — reusable patterns from real work — that fit what you are doing now, and apply one as a short checklist."
argument-hint: "<what you are working on, or a seed name>"
allowed-tools: Read, Glob, Grep, Bash(python3:*)
---

Find seeds for: $ARGUMENTS

1. If the argument is empty, ask what the person is working on and what feels stuck.
2. If the argument names a seed, read it from the workspace's `seeds/` folder or from `${CLAUDE_PLUGIN_ROOT}/seeds/`.
3. Otherwise run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" seeds suggest "<their words>"`. It searches the workspace's own seeds and the seeds that ship with this plugin.
4. Read the top suggestions. Present each in one line: its tagline, and why it may fit. Let the person choose; if none fits, say so plainly.
5. For the seed they choose, turn The pattern into a short checklist for their actual situation, and name what the seed refuses so they can spot the anti-pattern.

Seeds are suggestions, not rules. The person decides whether one applies.
