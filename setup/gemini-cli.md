# Git for Strategy — Gemini CLI Setup

## Quick Install

```bash
# Clone the repo
git clone https://github.com/TresPies-source/GitForStrategy.git

# Point Gemini CLI to the skills directory
export GEMINI_SKILLS_PATH="/path/to/GitForStrategy/skills"
```

Or add to your configuration:
```json
{
  "skills_paths": [
    "/path/to/GitForStrategy/skills"
  ]
}
```

## Initialize a Workspace

```bash
bash /path/to/GitForStrategy/scripts/init-strategy.sh "my-project"
```

## Usage

Reference skills in your prompts:
- "Using the strategic-scout skill, explore this tension"
- "Follow the specification-writer process to spec this"
- "Suggest seed patterns for what I'm working on"

## Templates & Seeds

Copy templates and seed references to your project:
```bash
cp -r /path/to/GitForStrategy/templates ./
cp -r /path/to/GitForStrategy/seeds ./
```

The seeds directory contains 13 reusable thinking patterns that work with any AI assistant.
