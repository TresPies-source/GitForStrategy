# Git for Strategy

**Your AI agent can execute tasks. Can it think strategically?**

AI agents are great at implementation. Give them a spec, they'll write the code. But strategic work — exploring tensions, weighing tradeoffs, making decisions that hold up three months later — they're terrible at it. They skip exploration, collapse nuance, and produce plans that sound smart but don't survive contact with reality.

Git for Strategy fixes this. **21 skills organized into a 5-phase pipeline** that gives your agent the discipline to explore before deciding, decide before building, track where it is, and learn from what it ships.

**Measured outcomes from 25 real releases: 40-50% shorter timelines. 77 hours saved through pre-flight verification alone.**

---

## Install (30 seconds)

### Claude Code / Cowork
```bash
git clone https://github.com/TresPies-source/GitForStrategy.git
# Add the path to your plugins configuration
```

### Cursor / VS Code / Windsurf
```bash
git clone https://github.com/TresPies-source/GitForStrategy.git
cp -r GitForStrategy/skills/ ~/.your-editor/skills/
```

> Full setup guides for [Claude Code](setup/claude-code.md) · [Cowork](setup/cowork.md) · [Cursor](setup/cursor.md) · [Windsurf](setup/windsurf.md) · [VS Code](setup/vscode.md) · [Gemini CLI](setup/gemini-cli.md)

### Initialize a workspace
```bash
bash scripts/init-strategy.sh "my-project"
```

---

## The Pipeline

```
EXPLORE  →  DECIDE  →  EXECUTE  →  TRACK  →  LEARN
  ↑                                              │
  └──────────────── seeds ────────────────────────┘
```

**Explore:** Scout tensions, research deeply, explore before committing. `/scout`

**Decide:** Write specs grounded in reality, plan from files not memory. `/spec`

**Execute:** Commission autonomous agents with structured prompts, run parallel tracks, verify before shipping. `/commission`

**Track:** Know where you are in the pipeline, spot stale work, maintain visibility. `/status`

**Learn:** Run retrospectives, extract seeds, compress context for next time. `/retro`

**Seeds:** 13 reusable thinking patterns extracted from 25 real releases. The standard library for strategic thinking. `/seed`

---

## Quick Example

```
You: /scout
Agent: What tension are you exploring?
You: We need to decide between building a native app or a web app.
Agent: [Generates a structured scout with 3-5 routes, tradeoffs,
        cross-route patterns, and open questions — saved to scouts/]

You: /spec
Agent: [Takes the scouted direction and writes a production-ready
        specification — saved to specs/]

You: /commission
Agent: [Transforms the spec into implementation prompts ready for
        autonomous execution — saved to commissions/]

You: /status
Agent: Pipeline: Explore ✅ → Decide ✅ → Execute ✅ → Learn ⏳
       Commission shipped 2 days ago. Retrospective due.

You: /retro
Agent: [Runs a structured retrospective, extracts seeds for next time
        — saved to retros/ and seeds/]
```

---

## What's Inside

### 21 Skills Across 6 Layers

| Phase | Skills | What You Get |
|-------|--------|--------------|
| **Explore** | 5 | Strategic scouting, iterative reframing, product positioning, deep/wide research, project exploration |
| **Decide** | 4 | Specification writing, context ingestion, frontend-from-backend grounding, file-based planning |
| **Execute** | 4 | Implementation prompts, parallel tracks, pre-flight checklists, agent handoffs |
| **Track** | 3 | Status writing, status templates, repo-level status and health |
| **Learn** | 4 | Retrospectives, seed extraction, memory garden, context compression |
| **Patterns** | 1 | 13 seed patches — the standard library for strategic thinking |

### Plus

- **7 commands:** `/scout`, `/spec`, `/commission`, `/retro`, `/seed`, `/status`, `/explore`
- **8 templates:** Scout, spec, commission, retro, seed, status, handoff, checklist
- **4 scripts:** Workspace initialization, pipeline validation, seed suggestion, context compression
- **13 seed patches:** Reusable thinking patterns with triggers, steps, and evidence
- **6 platform guides:** Claude Code, Cowork, Cursor, Windsurf, VS Code, Gemini CLI
- **3 hooks:** Pre-scout validation, post-spec pipeline update, pre-commission quality gate

---

## The 13 Seeds

Seeds are reusable thinking patterns. Each has a trigger, steps, and evidence from real use.

| Seed | When To Use It |
|------|---------------|
| Three-Tiered Governance | Adding structure to a project or team |
| Pace of Understanding | Pressure to deliver before understanding |
| Cost Consciousness | Resource constraints feel limiting |
| Voice Before Structure | Creating artifacts for a project |
| Liberation Psychology | Barriers prevent contribution |
| Patient Learning | Learning something new under pressure |
| Era Architecture | Planning multiple releases |
| Semantic Clustering | Mapping what a system does |
| Context Iceberg | Organizing knowledge for retrieval |
| Spec-to-Prompt Pipeline | Moving from spec to implementation |
| Portability Tiers | Classifying by dependency depth |
| Agent Workspace | Coordinating across agents |
| Handoff Protocol | Passing work between agents |

> Full seed documentation: [seeds/](seeds/)

---

## Why Not Just Use Planning-with-Files?

[Planning-with-files](https://github.com/OthmanAdi/planning-with-files) is excellent. It gives your agent memory — three markdown files that persist context across sessions. We recommend it.

Git for Strategy is the next layer. Memory tells your agent *what* it's working on. Strategy tells it *why*, *how to explore alternatives*, *when to commit*, and *what to learn from what it ships*. They're complementary, not competitive.

| | Planning-with-Files | Git for Strategy |
|---|---|---|
| **Problem solved** | Agents forget context | Agents can't think strategically |
| **Skills** | ~3 | 21 |
| **Commands** | 2 | 7 |
| **Templates** | 3 | 8 |
| **Seeds/Patterns** | — | 13 |
| **Measured outcomes** | — | 40-50% timeline reduction |

---

## Philosophy

**Begin with a tension, not a solution.** The quality of your strategic thinking is determined by the quality of your questions, not the speed of your answers.

**Knowledge should compound, not evaporate.** Every retrospective produces seeds. Every seed makes the next project better. The system improves with use.

**Governance multiplies velocity.** Structure isn't bureaucracy. Scout before deciding, spec before building, retro before starting over. The right constraints make you faster, not slower.

---

## Documentation

| Doc | What It Covers |
|-----|---------------|
| [Methodology](docs/methodology.md) | The full Git for Strategy methodology |
| [Pipeline Reference](docs/pipeline.md) | Detailed phase-by-phase reference |
| [Measured Outcomes](docs/measured-outcomes.md) | Evidence from 25 real releases |
| [Seeds Reference](docs/seeds-reference.md) | Quick reference for all 13 patterns |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute skills, seeds, and platform guides.

## License

MIT

---

*Built from 25 releases of real software. A [Tres Pies Design](https://github.com/TresPies-source) project.*
