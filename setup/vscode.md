# Git for Strategy — VS Code Setup

## Quick Install

```bash
# Clone the repo
git clone https://github.com/TresPies-source/GitForStrategy.git
```

### With Copilot Chat
Add to your `.github/copilot-instructions.md`:
```
Use Git for Strategy methodology for strategic decisions.
Skills are in /path/to/GitForStrategy/skills/.
Pipeline: Explore (scout) → Decide (spec) → Execute (commission) → Learn (retro).
Templates in /path/to/GitForStrategy/templates/.
Seed patterns in /path/to/GitForStrategy/seeds/.
```

### With Continue.dev or other extensions
Point your AI extension's skills/context path to the GitForStrategy directory.

## Initialize a Workspace

```bash
bash /path/to/GitForStrategy/scripts/init-strategy.sh "my-project"
```

## Manual Usage

Even without AI integration, the templates and seeds are valuable standalone:

1. Copy `templates/scout_template.md` to `scouts/` and fill it in manually
2. Read seeds in `seeds/` for thinking prompts during strategic discussions
3. Use `scripts/validate-pipeline.sh` to check pipeline health

## Snippets

Add VS Code snippets for quick template access:
```json
{
  "Strategic Scout": {
    "prefix": "scout",
    "body": ["# Strategic Scout: $1", "", "**Date:** $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE", "**Phase:** Explore", "", "## The Tension", "", "$2"],
    "description": "Git for Strategy scout template"
  }
}
```
