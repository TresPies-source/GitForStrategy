#!/usr/bin/env python3
"""compress_context.py — Compress conversation context into a memory artifact.

Usage: python3 compress_context.py input_file.md [output_dir]

Takes a conversation transcript or session notes and produces a compressed
memory artifact following the Context Iceberg pattern:
- Tip: One-sentence summary
- Waterline: Key decisions and active items
- Below surface: Full reasoning
- Archive: Raw source reference

This is a structural helper — the actual compression is done by the
compression-ritual skill with an LLM. This script provides the template.
"""

import sys
import os
from datetime import date


def generate_template(input_file: str, output_dir: str = "memory") -> str:
    """Generate a compression template from an input file."""
    
    basename = os.path.splitext(os.path.basename(input_file))[0]
    today = date.today().isoformat()
    output_path = os.path.join(output_dir, f"{today}-{basename}-compressed.md")
    
    # Read input to get rough size
    try:
        with open(input_file, 'r') as f:
            content = f.read()
        line_count = content.count('\n')
        word_count = len(content.split())
    except FileNotFoundError:
        line_count = 0
        word_count = 0
    
    template = f"""# Memory Artifact: {basename}

**Compressed:** {today}
**Source:** {input_file}
**Source Size:** {word_count} words, {line_count} lines
**Compression Ratio:** {{ratio}} (fill after compression)

---

## Tip (always visible)

{{One sentence: what is this about and what was decided?}}

## Waterline (on request)

### Key Decisions
1. {{Decision 1 — and why}}
2.

### Active Items
1. {{Item still in progress}}
2.

### Blockers
- {{If any}}

## Below Surface (searchable)

### Full Reasoning
{{Detailed reasoning behind key decisions. Include alternatives considered.}}

### Evidence
{{Data, measurements, or references that support decisions.}}

### Context
{{Background information needed to understand the decisions.}}

## Archive Reference

Source file: `{input_file}`
Compressed by: Git for Strategy — compression-ritual

---

*To expand any section, ask about the specific topic. The source file is preserved for full context.*
"""
    
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(template)
    
    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 compress_context.py input_file.md [output_dir]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "memory"
    
    output_path = generate_template(input_file, output_dir)
    print(f"Compression template created: {output_path}")
    print(f"Fill in the template sections, then use the compression-ritual skill for LLM-assisted compression.")


if __name__ == "__main__":
    main()
