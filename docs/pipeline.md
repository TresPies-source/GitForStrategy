# Git for Strategy — Pipeline Reference

## Overview

The pipeline is a 5-phase cycle. Each phase has skills, commands, templates, and artifacts.

```
EXPLORE → DECIDE → EXECUTE → TRACK → LEARN → (back to EXPLORE)
                                         ↑
                              seeds ──────┘
```

## Phase Details

### EXPLORE — Understand Before Deciding

**Purpose:** Map the landscape of possibility. Hold questions open.

| Resource | Location |
|----------|----------|
| Skills | `skills/explore/` (5 skills) |
| Command | `/scout`, `/explore` |
| Template | `templates/scout_template.md` |
| Artifacts | `scouts/` directory |

**Skills:**
- `strategic-scout` — Frame tensions, scout 3-5 routes
- `iterative-scouting` — Re-scout when first pass raises deeper questions
- `product-positioning` — Reframe binary decisions
- `research-modes` — Deep research (find answers) and wide research (find questions)
- `project-exploration` — Explore a new project before committing

**Entry criteria:** A genuine tension or question worth exploring
**Exit criteria:** Scouted routes with tradeoffs, recommendation for a direction

---

### DECIDE — Commit to a Direction

**Purpose:** Transform exploration into a specification. Ground decisions in reality.

| Resource | Location |
|----------|----------|
| Skills | `skills/decide/` (4 skills) |
| Command | `/spec` |
| Template | `templates/spec_template.md` |
| Artifacts | `specs/` directory |

**Skills:**
- `specification-writer` — Production-ready specs
- `context-ingestion` — Plans grounded in uploaded files
- `frontend-from-backend` — Frontend specs grounded in existing backend
- `planning-with-files` — File-based persistent planning

**Entry criteria:** A scouted direction with clear rationale
**Exit criteria:** Versioned specification with scope, criteria, and risks

---

### EXECUTE — Disciplined Implementation

**Purpose:** Transform specs into implementation-ready commissions. Verify before building.

| Resource | Location |
|----------|----------|
| Skills | `skills/execute/` (4 skills) |
| Command | `/commission` |
| Templates | `templates/commission_template.md`, `templates/checklist_template.md` |
| Artifacts | `commissions/` directory |

**Skills:**
- `implementation-prompt` — Structured prompts for autonomous agents
- `parallel-tracks` — Split into 2-4 independent tracks
- `pre-implementation-checklist` — Quality gate before commissioning
- `handoff-protocol` — Clean context-preserving handoffs

**Entry criteria:** Completed specification, passed pre-flight checklist
**Exit criteria:** Self-contained implementation prompts ready for agents

---

### TRACK — Know Where You Are

**Purpose:** Maintain visibility into pipeline state. Identify stale items and bottlenecks.

| Resource | Location |
|----------|----------|
| Skills | `skills/track/` (3 skills) |
| Command | `/status` |
| Template | `templates/status_template.md` |
| Artifacts | `STATUS.md` at project root |

**Skills:**
- `status-writing` — Write and update STATUS.md
- `status-template` — Comprehensive status documents
- `repo-status` — Codebase overview and health assessment

**Entry criteria:** Any time (run regularly)
**Exit criteria:** Updated STATUS.md reflecting current pipeline state

---

### LEARN — Harvest and Compound

**Purpose:** Reflect on completed work. Extract patterns. Compress context.

| Resource | Location |
|----------|----------|
| Skills | `skills/learn/` (4 skills) |
| Command | `/retro` |
| Templates | `templates/retro_template.md`, `templates/seed_template.md` |
| Artifacts | `retros/` directory, `seeds/` directory |

**Skills:**
- `retrospective` — Structured reflection: well, hard, change
- `seed-extraction` — Extract reusable patterns
- `memory-garden` — Structured memory entries
- `compression-ritual` — Distill sessions into memory artifacts

**Entry criteria:** Completed implementation (shipped or abandoned)
**Exit criteria:** Retrospective document, extracted seeds, compressed context

---

### PATTERNS — The Standard Library

**Purpose:** Apply reusable thinking patterns to current context.

| Resource | Location |
|----------|----------|
| Skills | `skills/patterns/` (1 skill) |
| Command | `/seed` |
| Template | `templates/seed_template.md` |
| Artifacts | `seeds/` directory (13 pre-loaded) |

**Skill:**
- `seed-library` — Suggest and apply relevant seed patches

**Available anytime.** Seeds compound — every retrospective can produce new seeds.

## Pipeline Health

Run `scripts/validate-pipeline.sh` or `/status` to check health.

| State | Meaning | Action |
|-------|---------|--------|
| 🟢 Green | Phase has recent artifacts, pipeline flowing | Continue |
| 🟡 Yellow | Artifacts getting stale (>7 days without progression) | Check blockers |
| 🔴 Red | Phase overdue (>14 days) or pipeline stuck | Investigate |
| ⚪ Empty | No artifacts yet | Expected for new phases |
