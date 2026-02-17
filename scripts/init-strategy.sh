#!/bin/bash
# init-strategy.sh — Initialize a Git for Strategy workspace
# Creates the directory structure for the 5-phase pipeline
#
# Usage: ./scripts/init-strategy.sh [project-name]
#
# This sets up the working directories where pipeline artifacts live.
# Skills, commands, templates, and seeds are in the plugin itself.
# This script creates the PROJECT workspace.

set -e

PROJECT_NAME="${1:-strategy}"
BASE_DIR="${2:-.}"

echo "Initializing Git for Strategy workspace: $PROJECT_NAME"

# Create pipeline directories
mkdir -p "$BASE_DIR/scouts"
mkdir -p "$BASE_DIR/specs"
mkdir -p "$BASE_DIR/commissions"
mkdir -p "$BASE_DIR/retros"
mkdir -p "$BASE_DIR/memory"

# Create initial STATUS.md
cat > "$BASE_DIR/STATUS.md" << EOF
# $PROJECT_NAME — Pipeline Status

**Last Updated:** $(date +%Y-%m-%d)
**Current Phase:** Explore
**Health:** Green — Fresh workspace

---

## Pipeline State

| Phase | Status | Last Artifact | Age |
|-------|--------|--------------|-----|
| Explore | Ready | — | — |
| Decide | Waiting | — | — |
| Execute | Waiting | — | — |
| Learn | Waiting | — | — |

## Next Steps

1. Run \`/scout\` to begin exploring a strategic tension
2. Run \`/status\` at any time to see where you are

---

*Initialized by Git for Strategy*
EOF

echo ""
echo "Workspace initialized:"
echo "   scouts/       — Strategic scouts and exploration notes"
echo "   specs/        — Specifications and decision documents"
echo "   commissions/  — Implementation prompts for agents"
echo "   retros/       — Retrospectives and learnings"
echo "   memory/       — Compressed context and memory artifacts"
echo "   STATUS.md     — Pipeline state (run /status to update)"
echo ""
echo "Start with: /scout"
