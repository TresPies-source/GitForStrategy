# Git for Strategy — pipeline contract

**Spec:** 1.0 · **Status:** Accepted · **License:** Apache-2.0

*Decisions are files. Files can be diffed.*

A small contract for keeping strategic work in plain files inside a repository: the tensions you scouted, the calls you made, the specs you wrote, and what you learned. A person and any agent read the same record.

This file is the source of truth. The commands, templates, and `scripts/gfs.py` implement it. Where they disagree with this file, they are wrong.

## The problem

Agents have made building fast. The reasoning above the code — why this direction, what was ruled out, who decided, what was learned — still lives in chat threads that end with the session. The next session re-derives it, or guesses. A guess that looks correct is worse than a visible failure.

## The human-agency contract

You bring the perspectives and you make the calls. The agent drafts, gathers evidence, synthesizes, and names what comes next. It never records its own lean as your ruling.

## Invariants

What makes a workspace a Git for Strategy workspace. An implementation that breaks one of these is not conformant, however good its output looks.

1. **Tension before solution.** Exploration starts from a named tension — two goods pulling against each other — not from a preferred answer. A scout presents every route before it names any default.
2. **Files are the record.** Scouts, decisions, specs, and retros live as files in the repository. A decision that exists only in a conversation has not been made.
3. **The person decides.** A decision's ruling is written in the decider's own words, with who and when. An agent names a default only when every piece of evidence it rests on is in hand; otherwise it names the missing evidence.
4. **Decide before you build.** A commission links to the spec it implements, and the spec links to an accepted decision. Work with no decision behind it is exploration, and is labeled that way.
5. **Claims carry their checks.** A count, path, version, or outcome in any artifact is either re-derivable from the repository or marked *not measured*. Scouts end with a `## Verification` section that says what was checked and what was not, and so do decisions written by this contract's tools.
6. **Supersede, don't rewrite.** An accepted decision is never edited to say something else. A new decision supersedes it, and both stay in the record.
7. **Close the loop.** Shipped or abandoned work gets a retro. A seed says where it grew from.

## The artifact contract

### Workspace

A workspace is a directory holding `STRATEGY.md`, the nexus. It is either the root of a repository kept for strategy, or a `strategy/` folder inside a code repository. Tools look for `./STRATEGY.md`, then `./strategy/STRATEGY.md`, in the current directory and then in each parent.

### Names

- Point-in-time artifacts are dated: `YYYY-MM-DD_slug.md`.
- Living documents are undated: `slug.md`.
- Decisions are numbered: `NNN-slug.md`, three digits, zero-padded, never renumbered. Dated names (`YYYY-MM-DD_slug.md`) are also accepted in `decisions/`, so tools that write dated records stay conformant.
- Slugs use lowercase letters, digits, and hyphens.

### Header

Every artifact except a seed — `STATUS.md` and `STRATEGY.md` included — opens with an H1 title, then bold header fields, one per line:

```markdown
# Scout: Native app or web app

**Date:** 2026-10-12
**Status:** Open
**Related:** [Decision 004](../decisions/004-web-first.md)
```

- `Date` is required. Living documents may add `Updated`; tools use the later of the two.
- `Status` is required where the type table lists status values, and must be exactly one of them. Only `Superseded` may be followed by more: what superseded it.
- `Related` holds relative links. Every relative link in an artifact must resolve. Links that start with `/` are not checked, because their root depends on where the file is viewed.

Files are UTF-8. Fenced code blocks and HTML comments do not count: links, checkboxes, and rulings inside them are ignored.

In `decisions/`, a dated file name stands in for a missing `Date`, and a missing `Status` is read as Proposed — so a decision written by a simpler tool is still a conformant record of a call nobody has ruled on yet.

Seeds open with YAML front matter instead: `name` (matches the file name), `tagline`, and `triggers` (a list of phrases).

### Types

| Type | Where | Name | Required sections | Status values |
|---|---|---|---|---|
| scout | `scouts/` | dated | Tension · Routes · Open questions · Verification | Open, Decided, Parked |
| decision | `decisions/` | numbered | Context · Decision · Consequences | Proposed, Accepted, Superseded, Rejected |
| spec | `specs/` | living | Problem · Current state · Scope · Success criteria · Non-goals · Risks | Draft, Ready, In build, Shipped, Retired |
| contract | `contracts/` | living | Provider · Consumer · Integration points · Open questions | Draft, Agreed, Retired |
| commission | `commissions/` | dated | Pre-flight · Context · Requirements · Success criteria · Constraints and non-goals · Done when | Draft, Ready, Out, Done |
| research | `research/` | dated | Question · Claims · Gaps | Open, Closed |
| runbook | `runbooks/` | living | TL;DR · Steps · Verify · Known debt | Current, Retired |
| audit | `audits/` | dated | Scope · Findings · Fixes | Open, Closed |
| draft | `drafts/` | living | Copy · Fact-check log | Draft, Checked, Published, Withdrawn |
| retro | `retros/` | dated | What went well · What was hard · What we would change · Seeds · Actions | Draft, Closed |
| session | `sessions/` | dated | Decided · Evidence · Open questions · Next move | — |
| seed | `seeds/` | living | What it is · Why it matters · The pattern · Revisit when · What it refuses · Grew from | — |
| status | `STATUS.md` | fixed | Where we are · Decision notes · Next | — |
| nexus | `STRATEGY.md` | fixed | Orientation · Hot facts · Router · Rules that bite here · Bookend | — |

A section is present when the file has a `##` heading that starts with its name. Files may carry more sections than these.

Decisions written by this contract's tools are also **expected** to carry `Options considered`, `Ruling`, `Revisit when`, and `Verification`. A validator reports a missing expected section as a warning, so decisions written by simpler tools still pass.

A decision marked Accepted or Rejected has been ruled on, so it must name its `Decider` and carry the ruling — in the decider's words — under `## Ruling`. A validator reports either one missing as an error. This is invariant 3, checked.

A commission should link the spec it implements. A validator warns when it does not.

What each type is for:

- **scout** — routes through a tension, with tradeoffs, before anyone decides.
- **decision** — one call, the options not chosen, the ruling in the decider's words, and when to look again.
- **spec** — what will be built, measured against the current state, with binary success criteria.
- **contract** — the two sides of an interface between pieces of work, agreed before either side builds. A contract is only as strong as its weaker side.
- **commission** — a self-contained brief for whoever builds, opening with a pre-flight that stops the work when anything it depends on is missing.
- **research** — an evidence dossier: claims with source, date, and confidence, so a later session verifies instead of re-deriving.
- **runbook** — an ordered procedure for a recurring operation, with a verify step that is not optional.
- **audit** — a drift audit: what the documents claim, what is true, and how much the gap matters.
- **draft** — copy meant for the public, with a log of every fact-check made before it goes out.
- **retro** — what a closed stretch of work taught, ending in seeds and actions.
- **session** — the close of a working session: what was decided, on what evidence, what is still open, and the next move.
- **seed** — a reusable pattern that grew from real work.
- **status** — where the pipeline stands right now.
- **nexus** — the front door: what this workspace is, its hot facts, a router to everything else, and the rules that bite here.

## Lifecycle

```
            research               contracts       pre-flight gate
               │                       │                 │
 tension ─▶ scout ─▶ decision ─▶ spec ─┴─▶ commission ─┴─▶ (build) ─▶ retro ─▶ seeds
               ▲                                                                 │
               └──────────────── seeds inform the next scout ────────────────────┘

 STATUS.md and sessions/ record where things stand at any point.
```

| Phase | Starts with | Ends with |
|---|---|---|
| Explore | a tension worth holding open | a scout with routes and open questions |
| Decide | a scout, or a call that has to be made | an accepted decision with the ruling in the decider's words |
| Specify | an accepted decision | a spec marked Ready, plus contracts where pieces meet |
| Commission | a Ready spec that passes the gate | a commission marked Ready |
| Build | — | happens outside this contract, with whatever tools you use |
| Learn | shipped or abandoned work | a closed retro and the seeds it grew |

## Pipeline health

`gfs.py status` reports, per phase, how many artifacts exist and the date of the newest. Ages come from header dates, not file times. A phase is *active* when its newest artifact is 7 days old or less, *quiet* after 7 days, and *dormant* after 14. A dormant phase is not a problem in itself — finished phases go quiet.

What needs attention is listed separately:

- scouts still Open after 14 days
- Ready specs older than 14 days that no commission links to
- Done commissions that no retro links to
- Accepted decisions with propagation items still open: unchecked boxes (`- [ ] ...`) under Consequences

## The pre-commission gate

`gfs.py gate <spec>` passes when the spec:

- is marked Ready
- has every required section
- states at least one success criterion as a checkbox (`- [ ]`)
- links under `Related` to an Accepted decision that names its decider and carries its ruling

A spec whose newest date is more than 14 days old passes with a warning: re-check the current state before commissioning against it.

## Conformance levels

| Level | Needs | What works |
|---|---|---|
| L0 Read | nothing | Read this file, the templates, and the seeds. Write artifacts by hand. |
| L1 Files | Python 3.9 or later | `scripts/gfs.py`: `init`, `new`, `validate`, `status`, `gate`, `seeds`. Standard library only, no network. |
| L2 Host | Claude Code | The plugin in this repository: commands for each phase and a session-start status note. |
| L3 Connected | the Dojo Genesis MCP server | Its decision tool can write records into `decisions/` when its ADR path points there. Without it, L1 does the same work. |

An adapter is conformant if it preserves the seven invariants and reads and writes the artifact contract. Adapters may add fields and sections. They may not drop required ones.

## Non-goals

- Not a runtime. It does not run agents, choose models, or schedule work.
- Not a memory system. It keeps the record; what an agent remembers is up to the agent.
- Not a coordination protocol between agents.
- Not a build gate. Enforcing build discipline belongs to other tools.
- Ships no practice skills. Those live in the Dojo Genesis library; their output belongs in these folders.
- No accounts, no server, no telemetry.

## Versioning

The spec version is `major.minor`. A minor version adds optional fields, sections, or types. A major version changes what is required. `STRATEGY.md` records the spec version a workspace was started under.
