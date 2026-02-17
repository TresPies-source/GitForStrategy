#!/usr/bin/env python3.11
"""
suggest_seeds.py - Suggest relevant seeds based on task context
Usage: python3.11 suggest_seeds.py <keywords...>
Example: python3.11 suggest_seeds.py multi-agent architecture coordination
"""

import sys
import json
from pathlib import Path
from datetime import datetime

SEEDS_DIR = Path(__file__).parent.parent / "seeds"

# Seed trigger keywords (extracted from seed definitions)
SEED_TRIGGERS = {
    "01_three_tiered_governance": [
        "governance", "capabilities", "complexity", "multi-agent", "coordination",
        "policy", "standards", "rules", "framework"
    ],
    "02_harness_trace": [
        "debugging", "trace", "transparency", "performance", "evaluation",
        "logging", "monitoring", "inspect"
    ],
    "03_context_iceberg": [
        "token", "cost", "context", "window", "limit", "budget", "pruning",
        "memory", "overhead"
    ],
    "04_agent_connect": [
        "multi-agent", "routing", "coordination", "specialized", "handoff",
        "permission", "swarm", "orchestration"
    ],
    "05_go_live_bundles": [
        "export", "sharing", "reuse", "artifact", "package", "bundle",
        "repeatability", "trust"
    ],
    "06_cost_guard": [
        "cost", "budget", "estimation", "planning", "infrastructure",
        "investment", "pricing"
    ],
    "07_safety_switch": [
        "fallback", "conservative", "alert", "drift", "failure", "recovery",
        "validation", "error"
    ],
    "08_implicit_perspective_extraction": [
        "perspective", "constraint", "metaphor", "scope", "extraction",
        "implicit", "natural"
    ],
    "09_mode_based_complexity_gating": [
        "mode", "complexity", "routing", "simple", "query", "reasoning",
        "adaptive"
    ],
    "10_shared_infrastructure": [
        "infrastructure", "reuse", "duplication", "foundation", "shared",
        "common", "service"
    ],
    "11_voice_before_structure": [
        "voice", "philosophy", "design-language", "manifest", "description",
        "readme", "ecosystem", "identity", "grounding", "plugin"
    ],
    "12_pointer_directories": [
        "empty", "missing", "pointer", "provenance", "registry", "audit",
        "gap", "coverage", "directory", "reference"
    ],
    "13_granular_visibility": [
        "progress", "tracking", "visibility", "todo", "granular", "steering",
        "transparency", "trust", "delegation", "status"
    ]
}

def load_seed_metadata(seed_file):
    """Load metadata from seed file"""
    content = seed_file.read_text()
    
    # Extract frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            metadata = {}
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            return metadata
    
    return {}

def calculate_relevance(keywords, seed_id):
    """Calculate relevance score for a seed based on keywords"""
    triggers = SEED_TRIGGERS.get(seed_id, [])
    keywords_lower = [k.lower() for k in keywords]
    
    score = 0
    for keyword in keywords_lower:
        for trigger in triggers:
            if keyword in trigger or trigger in keyword:
                score += 1
    
    return score

def suggest_seeds(keywords, top_n=3):
    """Suggest top N relevant seeds based on keywords"""
    suggestions = []
    
    for seed_id, triggers in SEED_TRIGGERS.items():
        score = calculate_relevance(keywords, seed_id)
        if score > 0:
            seed_file = SEEDS_DIR / f"{seed_id}.md"
            if seed_file.exists():
                metadata = load_seed_metadata(seed_file)
                suggestions.append({
                    'seed_id': seed_id,
                    'name': metadata.get('name', seed_id),
                    'score': score,
                    'file': str(seed_file)
                })
    
    # Sort by score descending
    suggestions.sort(key=lambda x: x['score'], reverse=True)
    
    return suggestions[:top_n]

def generate_markdown_output(keywords, suggestions):
    """Generate markdown output"""
    md = f"""# Seed Suggestions

**Keywords:** {', '.join(keywords)}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

"""
    
    if suggestions:
        md += "## Recommended Seeds\n\n"
        for i, suggestion in enumerate(suggestions, 1):
            md += f"### {i}. {suggestion['name']} (Seed {suggestion['seed_id'][:2]})\n\n"
            md += f"- **Relevance Score:** {suggestion['score']}\n"
            md += f"- **File:** `{suggestion['file']}`\n\n"
            
            # Read first few lines of seed for preview
            seed_file = Path(suggestion['file'])
            if seed_file.exists():
                content = seed_file.read_text()
                # Find "What It Is" section
                if "## What It Is" in content:
                    what_it_is = content.split("## What It Is")[1].split("##")[0].strip()
                    md += f"**What It Is:** {what_it_is[:200]}...\n\n"
        
        md += "\n## How to Apply\n\n"
        md += "To apply a seed, run:\n"
        md += "```bash\n"
        md += "python3.11 apply_seed.py <seed_id>\n"
        md += "```\n"
    else:
        md += "No relevant seeds found for these keywords.\n\n"
        md += "**Available seeds:**\n"
        for seed_id in SEED_TRIGGERS.keys():
            md += f"- {seed_id}\n"
    
    return md

def main():
    if len(sys.argv) < 2:
        print("Usage: python3.11 suggest_seeds.py <keywords...>")
        print("Example: python3.11 suggest_seeds.py multi-agent architecture coordination")
        sys.exit(1)
    
    keywords = sys.argv[1:]
    
    print(f"🔍 Suggesting seeds for: {', '.join(keywords)}")
    
    suggestions = suggest_seeds(keywords)
    output = generate_markdown_output(keywords, suggestions)
    
    print(output)
    
    # Save to file
    output_file = Path.home() / "seed-suggestions.md"
    output_file.write_text(output)
    print(f"\n✅ Suggestions saved to: {output_file}")

if __name__ == "__main__":
    main()
