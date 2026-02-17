# Git for Strategy — Windsurf Setup

## Quick Install

```bash
# Clone the repo
git clone https://github.com/TresPies-source/GitForStrategy.git

# Copy skills to Windsurf's skill directory
cp -r GitForStrategy/skills/* ~/.windsurf/skills/
```

## Configure

Add to your Windsurf rules or system prompt:

```
Use Git for Strategy skills for strategic work.
Pipeline: Explore → Decide → Execute → Learn.
Save artifacts to scouts/, specs/, commissions/, retros/.
Reference seed patterns in seeds/ when relevant.
```

## Initialize a Workspace

```bash
bash /path/to/GitForStrategy/scripts/init-strategy.sh "my-project"
```

## Usage

Windsurf will pick up the skills automatically. Prompt it with:
- "Scout this problem before we decide"
- "Write a spec following the specification-writer skill"
- "What seed patterns apply to this situation?"

## Templates

Available in the `templates/` directory. Copy to your project as needed.
