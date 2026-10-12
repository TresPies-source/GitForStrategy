#!/usr/bin/env python3
"""SessionStart hook: tell the agent where the strategy pipeline stands.

Speaks only in projects that keep a workspace (./STRATEGY.md or ./strategy/STRATEGY.md),
so a plugin never nags a project that did not opt in. Off when DOJO_OFF or GFS_OFF is set.
Fail-open: any error prints nothing and exits 0.
"""
import json
import os
import subprocess
import sys

CORE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "gfs.py")
OFF_VALUES = {"1", "true", "yes", "on"}


def switched_off():
    return any(os.environ.get(name, "").strip().lower() in OFF_VALUES for name in ("DOJO_OFF", "GFS_OFF"))


def main():
    if switched_off():
        return
    cwd = os.getcwd()
    if not (os.path.isfile(os.path.join(cwd, "STRATEGY.md"))
            or os.path.isfile(os.path.join(cwd, "strategy", "STRATEGY.md"))):
        return
    result = subprocess.run([sys.executable, CORE, "status", "--brief"],
                            capture_output=True, text=True, timeout=8, cwd=cwd)
    summary = (result.stdout or "").strip()
    if result.returncode != 0 or not summary:
        return
    note = ("This project keeps its strategy in files under the Git for Strategy contract; "
            "read STRATEGY.md before strategic work. The person makes the calls: record rulings "
            "in their own words, and mark agent proposals as proposals.")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": summary + "\n" + note,
    }}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
