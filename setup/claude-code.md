# Git for Strategy — Claude Code Setup

## Quick Install

```bash
# Clone the repo
git clone https://github.com/TresPies-source/GitForStrategy.git

# Add as a project dependency
cd your-project
echo '/path/to/GitForStrategy' >> .claude/plugins
```

Or add directly to your Claude Code configuration:

```json
// .claude/settings.json
{
  "plugins": [
    "/path/to/GitForStrategy"
  ]
}
```

## Verify Installation

```
You: /scout
Agent: What tension are you exploring?
```

If you see the scout prompt, you're set.

## Initialize a Workspace

```bash
cd your-project
bash /path/to/GitForStrategy/scripts/init-strategy.sh "my-project"
```

This creates the pipeline directories (scouts/, specs/, commissions/, retros/, memory/) and an initial STATUS.md.

## Available Commands

| Command | Phase | What It Does |
|---------|-------|-------------|
| `/scout` | Explore | Start a strategic scout |
| `/spec` | Decide | Write a specification |
| `/commission` | Execute | Generate implementation prompts |
| `/retro` | Learn | Run a retrospective |
| `/seed` | Any | Suggest relevant seed patterns |
| `/status` | Any | Show pipeline state |
| `/explore` | Pre-Scout | Deep-dive before scouting |

## Tips

- Start every new project or major decision with `/scout`
- Run `/status` daily to see pipeline health
- After shipping, always run `/retro` — the seeds you extract compound over time
