# Git for Strategy

*Decisions are files. Files can be diffed.*

Agents have made building fast. Deciding what to build — and remembering why — still happens in chat threads that end with the session. Git for Strategy keeps that work in your repository: the tension you scouted, the call you made and who made it, the spec, the brief for whoever builds, and what you learned when it shipped.

It is a contract, not a runtime: a folder layout, a format for each kind of artifact, and seven rules that keep the record honest. [SPEC.md](SPEC.md) is the whole of it. The commands and the script in this repository implement it.

You bring the perspectives and make the calls. The agent drafts, gathers evidence, synthesizes, and names what comes next. It never writes its own lean down as your ruling.

## How it fits Dojo Genesis

Dojo Genesis is a protocol layer for Claude Code. Its suite of plugins aims at build discipline inside Claude Code. Its library holds the practice skills — scouting, specification, retrospectives, seeds.

Git for Strategy is where that practice lands. The library's skills produce scouts, specs, and retros; this repository gives them one place to live and one format to follow, and checks both. It ships no practice skills of its own. When a library plugin is installed, the commands here point to its skills for technique.

## Install in Claude Code

Git for Strategy is not yet listed in the Dojo Genesis marketplace. Load it from a clone:

```bash
git clone https://github.com/DojoGenesis/git-for-strategy.git
claude --plugin-dir ./git-for-strategy
```

Start a workspace in your project — at the root of a repository kept for strategy, or in a `strategy/` folder inside a code repository:

```bash
python3 git-for-strategy/scripts/gfs.py init                  # workspace at the project root
python3 git-for-strategy/scripts/gfs.py init --root strategy  # or inside strategy/
```

Then add the line `@STRATEGY.md` (or `@strategy/STRATEGY.md`) to your project's `CLAUDE.md`, so every session reads the workspace's front door.

For the practice skills the commands point to, add the Dojo Genesis marketplace and install the library plugins you want:

```text
/plugin marketplace add DojoGenesis/plugins
/plugin install strategic-thinking@dojo-genesis
```

## The pipeline

```
 tension ─▶ scout ─▶ decision ─▶ spec ─▶ commission ─▶ (build) ─▶ retro ─▶ seeds
               ▲                                                            │
               └──────────────── seeds inform the next scout ───────────────┘
```

| Phase | Command | Writes |
|---|---|---|
| Explore | `/scout` | `scouts/`, and `research/` when evidence is thin |
| Decide | `/decide` | `decisions/` — the ruling in the decider's own words |
| Specify | `/spec` | `specs/`, and `contracts/` where pieces of work meet |
| Commission | `/commission` | `commissions/`, only after the spec passes the gate |
| Learn | `/retro` | `retros/` and `seeds/` |
| Any time | `/status`, `/seed`, `/close` | `STATUS.md`, `sessions/` |

The contract also defines runbooks, drift audits, and drafts of public copy. [SPEC.md](SPEC.md) lists every type with its folder, name pattern, required sections, and status values.

## The rules

1. Tension before solution.
2. Files are the record.
3. The person decides — rulings in their own words.
4. Decide before you build.
5. Claims carry their checks.
6. Supersede, don't rewrite.
7. Close the loop.

Each is spelled out in [SPEC.md](SPEC.md#invariants).

## The script

`scripts/gfs.py` is the reference implementation: Python 3.9 or later, standard library only, no network.

| Command | Does |
|---|---|
| `init` | create a workspace: `STRATEGY.md`, `STATUS.md`, and the core folders |
| `new TYPE "title"` | create an artifact from its template, named by the contract's rules |
| `validate` | check every artifact against the contract: names, headers, sections, status values, links |
| `status` | pipeline health from header dates, and what needs attention |
| `gate SPEC` | the pre-commission gate |
| `seeds suggest "..."` | suggest seeds for a situation |

The Claude Code commands call it, so a workspace looks the same whoever wrote it.

## Without Claude Code

The files work anywhere. Point your agent's rules file — `AGENTS.md` or your tool's equivalent — at `STRATEGY.md`, and use `gfs.py` from a terminal. [docs/adapters.md](docs/adapters.md) covers other agents, the Dojo Genesis OpenClaw plugin, and the optional Dojo Genesis MCP server.

## Example

[examples/native-or-web](examples/native-or-web/STRATEGY.md) is a small illustrative workspace carried from tension to seeds. It is not a real project. CI checks that it passes `gfs.py validate --strict`.

## Seeds

Seeds are patterns that grew from real work: foundations of the practice, structure, grounding, deciding, honesty, and execution. Each says where it came from. [Browse them](seeds/README.md), or run `/seed`.

## Not measured

Earlier versions of this README led with timeline and hours-saved figures. They were not measured against a baseline, so version 2.0.0 removed them.

The effect of this method on speed, cost, or quality has not been measured. A fair measurement would compare matched pieces of work done with and without the pipeline, with the comparison and the success measure written down before the first run, and would publish the result whichever way it came out. If you run one, open an issue with your method and results, null results included.

## Lineage

Git for Strategy grew out of the Dojo Genesis practice: *begin with a tension, not a solution*. Its human-agency commitments come from the lineage that practice names for itself — beginner's mind, understanding before help, self-definition, and liberation psychology's insistence that structures re-center the people they serve. The seeds [Partnership, Not Autopilot](seeds/partnership-not-autopilot.md) and [Liberation Psychology](seeds/liberation-psychology.md) carry the sources.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes to the contract start as a scout and a decision, the same as anything else.

## License

Apache-2.0. See [LICENSE](LICENSE).

Built by Dojo Genesis at TresPies LLC. Claude Code is a product of Anthropic; Git for Strategy is an independent project, not affiliated with or endorsed by Anthropic.
