# Adapters

*Every host reads the same files.*

The contract in [SPEC.md](../SPEC.md) is plain markdown in plain folders, so any tool that can read and write files can take part. What changes from host to host is how much is automated. The conformance levels say what each one needs:

| Level | Needs | What works |
|---|---|---|
| L0 Read | nothing | Read the spec, templates, and seeds. Write artifacts by hand. |
| L1 Files | Python 3.9 or later | `scripts/gfs.py` for init, new, validate, status, gate, and seeds. |
| L2 Host | Claude Code | This repository's plugin: commands and a session-start status note. |
| L3 Connected | the Dojo Genesis MCP server | Its decision tool writes into `decisions/`. |

An adapter is conformant if it keeps the seven invariants and reads and writes the artifact contract. It may add fields and sections. It may not drop required ones.

## Claude Code (L2)

Load the plugin from a clone with `claude --plugin-dir <path to this repository>`. It adds:

- `/scout`, `/decide`, `/spec`, `/commission`, `/retro` — one per phase, each writing through `gfs.py` and validating what it wrote.
- `/status`, `/seed`, `/close` — pipeline health, seed suggestions, and the session bookend.
- A session-start note with the pipeline's state, only in projects that have a workspace.

Set `GFS_OFF=1` to switch the session-start note off. `DOJO_OFF=1`, the switch shared by Dojo Genesis plugins, turns it off too.

Add `@STRATEGY.md` (or `@strategy/STRATEGY.md`) to your project's `CLAUDE.md`, so every session reads the workspace's front door.

## Any other agent (L0 and L1)

Point the agent's rules file — `AGENTS.md`, or your tool's equivalent — at the nexus. For example:

```markdown
## Strategy

This project keeps its strategy in files under the Git for Strategy contract.
Read strategy/STRATEGY.md before strategic work.
Create artifacts with `python3 <path>/scripts/gfs.py new <type> "<title>"`,
and run `python3 <path>/scripts/gfs.py validate` before you call the work done.
The person makes the calls: record rulings in their own words.
```

## Dojo Genesis practice skills

The Dojo Genesis library holds the practice skills; this repository holds the contract their output lands in. Install the library from the Dojo Genesis marketplace (`/plugin marketplace add DojoGenesis/plugins`), then write each skill's output into the matching folder with `gfs.py new`, so it follows the contract.

| Phase | Skills |
|---|---|
| Explore | `strategic-thinking:strategic-scout`, `strategic-thinking:iterative-scouting`, `strategic-thinking:product-positioning`, `continuous-learning:research-modes`, `continuous-learning:project-exploration` |
| Decide | `dojo-settle:decision-gate`, `dojo-craft:adr-writer` |
| Specify | `specification-driven-development:specification-writer`, `specification-driven-development:codebase-audit-grounding`, `specification-driven-development:context-ingestion`, `specification-driven-development:frontend-from-backend` |
| Commission | `specification-driven-development:implementation-prompt`, `specification-driven-development:pre-implementation-checklist`, `specification-driven-development:parallel-tracks` |
| Track | `system-health:status-writing`, `system-health:repo-status`, `system-health:convergence-gate` |
| Learn | `continuous-learning:retrospective`, `wisdom-garden:seed-extraction`, `wisdom-garden:seed-library` |

## Dojo Genesis MCP server (L3)

The MCP server is optional. Its decision tool writes dated decision records into the folder its `DOJO_ADR_PATH` setting names (see that server's README). Point it at the workspace's `decisions/` folder: the contract accepts dated names in `decisions/`, takes the date from the name, and reads a missing Status as Proposed. This was checked against the tool's source, not run end to end. `gfs.py validate` warns about the sections such a record lacks — options, ruling, revisit triggers, verification — and `/decide` adds them once the person rules.

## OpenClaw

The Dojo Genesis OpenClaw plugin (`openclaw plugins install @trespies-source/dojo-genesis-plugin`) has its own `/dojo` commands for scouting, specs, commissions, and retros, and keeps their output in per-project folders. Most folder names match this contract; where it keeps implementation prompts separately, those correspond to commissions. To keep one record, save that output into the workspace and run `gfs.py validate`. This mapping has not been tested end to end.
