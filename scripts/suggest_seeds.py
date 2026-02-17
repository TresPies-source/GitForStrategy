#!/usr/bin/env python3
"""suggest_seeds.py — Recommend seed patterns for the current context.

Usage: python3 suggest_seeds.py "description of what you're working on"

Matches keywords in the description against seed triggers to suggest
relevant patterns. Simple keyword matching — no ML required.
"""

import sys
import os

SEEDS = {
    "three-tiered-governance": {
        "triggers": ["structure", "governance", "organize", "scale", "team", "quality", "fast", "growing"],
        "summary": "Organize into Principles — Protocols — Practices"
    },
    "pace-of-understanding": {
        "triggers": ["rush", "pressure", "deadline", "ship", "fast", "hurry", "understand", "confused"],
        "summary": "Work at the pace of understanding, not expectation"
    },
    "cost-consciousness": {
        "triggers": ["cost", "budget", "expensive", "resource", "constraint", "limit", "infrastructure"],
        "summary": "Treat cost as a design constraint that sharpens thinking"
    },
    "voice-before-structure": {
        "triggers": ["template", "artifact", "document", "spec", "write", "create", "new project"],
        "summary": "Read project philosophy before writing artifacts"
    },
    "liberation-psychology": {
        "triggers": ["barrier", "access", "contribute", "open source", "democratize", "gatekeep", "inclusive"],
        "summary": "Remove barriers to contribution"
    },
    "patient-learning": {
        "triggers": ["learn", "new", "onboard", "unfamiliar", "stuck", "overwhelm", "rabbit hole"],
        "summary": "Use methodology to prevent learning rabbit holes"
    },
    "era-architecture": {
        "triggers": ["release", "roadmap", "multi-release", "version", "long-term", "vision", "era", "phase"],
        "summary": "Group releases into coherent eras with shared constraints"
    },
    "semantic-clustering": {
        "triggers": ["codebase", "understand", "architecture", "capability", "system", "map", "what does"],
        "summary": "Map what a system DOES, not where files ARE"
    },
    "context-iceberg": {
        "triggers": ["context", "memory", "knowledge", "retrieve", "organize", "information", "compress"],
        "summary": "Structure info in 4 tiers: tip, waterline, below, archive"
    },
    "spec-to-prompt-pipeline": {
        "triggers": ["implement", "commission", "agent", "hand off", "prompt", "spec", "build"],
        "summary": "Scout → Spec → Pre-flight → Prompt → Commission"
    },
    "field-portability-tiers": {
        "triggers": ["portable", "cross-platform", "dependency", "migrate", "tier", "classify"],
        "summary": "Classify components by dependency depth (Tier 1-4)"
    },
    "field-agent-workspace": {
        "triggers": ["collaborate", "multi-agent", "workspace", "shared", "coordinate"],
        "summary": "Structured workspaces for multi-agent collaboration"
    },
    "field-handoff-protocol": {
        "triggers": ["handoff", "hand off", "relay", "pass", "transition", "agent"],
        "summary": "Package handoffs with state, decisions, questions, done criteria"
    }
}


def suggest(description: str, top_n: int = 3) -> list:
    """Score seeds against description and return top matches."""
    description_lower = description.lower()
    scores = []
    
    for seed_name, seed_data in SEEDS.items():
        score = sum(1 for trigger in seed_data["triggers"] if trigger in description_lower)
        if score > 0:
            scores.append((seed_name, score, seed_data["summary"]))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 suggest_seeds.py \"description of what you're working on\"")
        sys.exit(1)
    
    description = " ".join(sys.argv[1:])
    suggestions = suggest(description)
    
    if not suggestions:
        print("No strong seed matches found. Try describing your situation differently.")
        print("Available seeds:", ", ".join(SEEDS.keys()))
        sys.exit(0)
    
    print(f"Suggested seeds for: \"{description}\"\n")
    for i, (name, score, summary) in enumerate(suggestions, 1):
        print(f"  {i}. {name} (relevance: {score})")
        print(f"     {summary}")
        print(f"     → Read: seeds/{name}.md")
        print()


if __name__ == "__main__":
    main()
