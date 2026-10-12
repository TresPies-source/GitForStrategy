# Changelog

## [2.0.0] — 2026-10-12

Git for Strategy becomes the pipeline contract in the Dojo Genesis family: the files that strategy work lands in, and the checks that keep them honest. It no longer ships copies of the practice skills.

### Added

- `SPEC.md`: the contract. Seven invariants; the artifact contract (types, names, headers, sections, status values); lifecycle; pipeline health; the pre-commission gate; conformance levels; non-goals.
- `scripts/gfs.py`: the reference implementation — `init`, `new`, `validate`, `status`, `gate`, `seeds`, `selfcheck`. Python 3.9 or later, standard library only.
- Invariant 3, checked: an Accepted or Rejected decision must name its decider and carry the ruling. `validate` and the gate both check it.
- Artifact types from live practice: decision records with the ruling in the decider's own words, contracts, evidence dossiers, runbooks, drift audits, drafts of public copy, session closes, and a workspace front door (`STRATEGY.md`). Scouts end with a Verification section, and so do decisions written by this contract's tools.
- `/decide` and `/close`. Commands that create artifacts write through `gfs.py` and validate what they wrote.
- A SessionStart hook that reports pipeline state, only in projects that have a workspace. Off with `GFS_OFF=1` or `DOJO_OFF=1`.
- Twelve seeds from the Dojo Genesis practice's retrospectives, decision records, and working sessions, in four groups: grounding, deciding, honesty, execution.
- The Partnership, Not Autopilot seed, grounded in Shunryu Suzuki, Thich Nhat Hanh, and Patricia Hill Collins.
- Sources for the Liberation Psychology seed: Ignacio Martín-Baró and Frantz Fanon.
- `examples/native-or-web`: an illustrative workspace carried from tension to seeds.
- `strategy/`: this repository's own workspace, holding the scout and decisions behind this release.
- `docs/adapters.md`: other agents, the Dojo Genesis library skills, the Dojo Genesis MCP server, and OpenClaw.
- CI: unit tests, `selfcheck`, and strict validation of the example and of `strategy/`.

### Changed

- License: MIT to Apache-2.0, matching the Dojo Genesis plugins.
- Author: Dojo Genesis. Homepage and repository: `DojoGenesis/git-for-strategy`.
- Seeds carry front matter and the sections What it is, Why it matters, The pattern, Revisit when, What it refuses, Grew from.
- Templates are named by type and rewritten. Status files are pointers, not snapshots.
- Phase ages read active, quiet, or dormant. What needs attention is listed separately.

### Removed

- The 21 copied practice skills. They are maintained in the Dojo Genesis library, and the commands point to the library skills for each phase. Claude Code was not loading them from this repository's nested layout.
- Outcome figures — timeline reduction, hours saved, fewer revisions. They were not measured against a baseline. See "Not measured" in the README.
- Unsourced figures in seeds.
- Runtime-architecture notes, the agent-runtime seed patches, memory-retention material, and agent-handoff material, which are outside the scope of a practice contract. The Context Iceberg, Agent Workspace, and Handoff Protocol seeds went with them.
- Hooks written as prose that never ran; the `/explore` command, which `/scout` covers; per-editor setup guides that described copying the removed skills.
- The methodology paper (`.docx`) and its companion note.

## [1.0.0] — 2026-02-17

### Added
- 21 skills across 6 phases: Explore (5), Decide (4), Execute (4), Track (3), Learn (4), Patterns (1)
- 7 commands: `/scout`, `/spec`, `/commission`, `/retro`, `/seed`, `/status`, `/explore`
- 8 templates: scout, spec, commission, retro, seed, status, handoff, checklist
- 4 scripts: init-strategy.sh, validate-pipeline.sh, suggest_seeds.py, compress_context.py
- 13 seed patches: 10 core + 3 field seeds
- 6 platform setup guides: Claude Code, Cowork, Cursor, Windsurf, VS Code, Gemini CLI
- 3 hooks: pre-scout, post-spec, pre-commission
- 4 documentation files: methodology, pipeline reference, measured outcomes, seeds reference
- Plugin manifest for Claude Code / Cowork integration

### Origin
Skills adapted from the [Dojo Genesis CoworkPlugins](https://github.com/TresPies-source/CoworkPluginsByDojoGenesis) collection, curated for the strategic thinking lifecycle.
