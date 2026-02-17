# Git for Strategy — Cursor Setup

## Quick Install

```bash
# Clone the repo
git clone https://github.com/TresPies-source/GitForStrategy.git

# Copy skills to your Cursor skills directory
cp -r GitForStrategy/skills/* ~/.cursor/skills/
```

Or symlink for auto-updates:
```bash
ln -s /path/to/GitForStrategy/skills ~/.cursor/git-for-strategy-skills
```

## Configure Cursor Rules

Add to your `.cursorrules` file:

```
When I ask about strategic decisions, use the Git for Strategy skills in skills/.
The pipeline is: Explore (scout) → Decide (spec) → Execute (commission) → Learn (retro).
Always save artifacts to the appropriate pipeline directory.
Suggest seed patterns when relevant.
```

## Initialize a Workspace

```bash
bash /path/to/GitForStrategy/scripts/init-strategy.sh "my-project"
```

## Usage

Reference skills directly in your prompts:
- "Use the strategic-scout skill to explore this tension"
- "Follow the specification-writer skill to spec this feature"
- "Run the pre-implementation-checklist before we build"

## Templates

Copy templates to your project:
```bash
cp -r /path/to/GitForStrategy/templates ./strategy-templates/
```
