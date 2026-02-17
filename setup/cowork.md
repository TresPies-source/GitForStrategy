# Git for Strategy — Cowork Setup

## Quick Install

1. Open Cowork
2. Go to Settings → Plugins
3. Add plugin from local path: point to the cloned GitForStrategy directory

Or install from the marketplace (when available):
```
Search: "Git for Strategy"
Click: Install
```

## Verify Installation

Type `/scout` in the chat. You should see the strategic scout prompt.

## Initialize a Workspace

Select a folder in Cowork, then ask:
> "Initialize a Git for Strategy workspace here"

Or run:
```bash
bash scripts/init-strategy.sh "my-project"
```

## Using the Skills

All 21 skills are automatically available. Cowork will suggest relevant skills based on your context. You can also invoke them directly:

- "Scout this tension for me" → triggers strategic-scout
- "Write a spec for this direction" → triggers specification-writer
- "What seeds apply here?" → triggers seed-library

## Available Commands

Type any of these in the chat:
- `/scout` — Start exploring
- `/spec` — Start specifying
- `/commission` — Generate implementation prompts
- `/retro` — Reflect on completed work
- `/seed` — Get pattern suggestions
- `/status` — Check pipeline health
- `/explore` — Deep-dive before scouting
