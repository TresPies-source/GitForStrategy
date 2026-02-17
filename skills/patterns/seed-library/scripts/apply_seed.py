#!/usr/bin/env python3.11
"""
apply_seed.py - Load and explain how to apply a seed
Usage: python3.11 apply_seed.py <seed_id>
Example: python3.11 apply_seed.py 04_agent_connect
"""

import sys
import json
from pathlib import Path
from datetime import datetime

SEEDS_DIR = Path(__file__).parent.parent / "seeds"
USAGE_FILE = Path.home() / ".seed-usage.json"

def load_usage_state():
    """Load usage state from JSON file"""
    if not USAGE_FILE.exists():
        return {
            "seeds": {},
            "session_seeds": {}
        }
    
    with open(USAGE_FILE) as f:
        return json.load(f)

def save_usage_state(state):
    """Save usage state to JSON file"""
    with open(USAGE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def track_seed_usage(seed_id, session_id=None):
    """Track seed usage"""
    state = load_usage_state()
    
    if seed_id not in state["seeds"]:
        state["seeds"][seed_id] = {
            "usage_count": 0,
            "last_used": None,
            "sessions": []
        }
    
    state["seeds"][seed_id]["usage_count"] += 1
    state["seeds"][seed_id]["last_used"] = datetime.now().isoformat()
    
    if session_id:
        if session_id not in state["seeds"][seed_id]["sessions"]:
            state["seeds"][seed_id]["sessions"].append(session_id)
        
        if session_id not in state["session_seeds"]:
            state["session_seeds"][session_id] = []
        
        if seed_id not in state["session_seeds"][session_id]:
            state["session_seeds"][session_id].append(seed_id)
    
    save_usage_state(state)

def apply_seed(seed_id, session_id=None):
    """Load and display seed content"""
    seed_file = SEEDS_DIR / f"{seed_id}.md"
    
    if not seed_file.exists():
        print(f"❌ Seed not found: {seed_id}")
        print(f"   Expected at: {seed_file}")
        print("\nAvailable seeds:")
        for f in sorted(SEEDS_DIR.glob("*.md")):
            print(f"  - {f.stem}")
        sys.exit(1)
    
    # Track usage
    track_seed_usage(seed_id, session_id)
    
    # Load content
    content = seed_file.read_text()
    
    # Generate application guide
    guide = f"""
# Applying Seed: {seed_id}

---

{content}

---

## Application Checklist

Review the "Checks" section in the seed above and validate each one.

## Next Steps

1. **Review the pattern** - Understand the core pattern and why it matters
2. **Check the trigger** - Confirm this seed is relevant to your current task
3. **Apply the pattern** - Follow the "Dojo Application" section
4. **Validate with checks** - Ensure all checks pass
5. **Note what it refuses** - Avoid the anti-patterns

## Track Effectiveness

After applying this seed, rate its effectiveness:
```bash
python3.11 track_usage.py {seed_id} <session_id> <helpful|not_helpful>
```

"""
    
    return guide

def main():
    if len(sys.argv) < 2:
        print("Usage: python3.11 apply_seed.py <seed_id> [session_id]")
        print("Example: python3.11 apply_seed.py 04_agent_connect session_123")
        sys.exit(1)
    
    seed_id = sys.argv[1]
    session_id = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"📖 Loading seed: {seed_id}")
    
    guide = apply_seed(seed_id, session_id)
    print(guide)
    
    # Save to file
    output_file = Path.home() / f"seed-{seed_id}-applied.md"
    output_file.write_text(guide)
    print(f"\n✅ Application guide saved to: {output_file}")

if __name__ == "__main__":
    main()
