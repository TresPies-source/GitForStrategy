# Git for Strategy — Methodology

## The Core Idea

Git tracks code changes. Git for Strategy tracks decision changes.

Where software teams use branching to explore code alternatives, strategic teams can branch to explore competing hypotheses. Where commits preserve code history, decision commits preserve reasoning. Where diffs show what changed, strategy diffs show what shifted and why.

## The Problem

Most strategic work disappears. Decisions live in conversations, slide decks, and memory. When a decision needs revisiting three months later, the context is gone. When new team members join, they inherit conclusions without reasoning. When AI agents participate in strategic work, their contributions evaporate after the session ends.

This creates three failures:
1. **Repeated exploration** — Teams re-scout the same tensions because nobody recorded the first scout
2. **Context-free decisions** — People follow decisions they don't understand, leading to drift
3. **No compounding** — Each project starts from zero instead of building on previous learnings

## The Solution: Planning with Files

The fix is deceptively simple: **make persistent files the source of truth for strategic work.**

Not conversations. Not slide decks. Not memory. Files.

Files can be versioned. Files can be diffed. Files can be searched. Files persist across sessions, across team changes, across AI context windows. Files compound.

## The Five-Phase Pipeline

### Phase 1: Explore

Begin with a tension, not a solution. A tension is a genuine pull between competing goods — "move fast" vs. "maintain quality" — not a problem with an obvious answer.

Scout 3-5 routes through the tension. For each route, name the tradeoffs. Identify patterns that appear across routes. Save everything to `scouts/`.

### Phase 2: Decide

Commit to a direction by writing a specification. A spec is a contract — specific enough to implement, grounded enough to survive contact with reality.

Good specs include: problem statement, scope (in AND out), technical design, dependencies, success criteria, risks. Save to `specs/`.

### Phase 3: Execute

Transform specifications into implementation prompts. Run a pre-flight checklist to catch drift between spec and reality. Split large work into parallel tracks. Hand off cleanly with full context. Save to `commissions/`.

### Phase 4: Learn

After shipping, run a structured retrospective. What went well, what was hard, what to change. Extract reusable patterns as seeds. Compress session context for future reference. Save to `retros/`.

### Phase 5 (Meta): Apply Patterns

Seeds are the standard library. Each seed has a trigger (when to apply), steps (how), and evidence (where it worked). Seeds compound — every retrospective potentially produces new seeds that make the next project better.

## The Pipeline Loop

```
EXPLORE  →  DECIDE  →  EXECUTE  →  LEARN
  ↑                                   │
  └───────────── seeds ───────────────┘
```

Learning feeds back into exploration. Seeds from past projects inform future scouts. The system gets better with use.

## Measured Outcomes

These aren't theoretical. From 25 releases of real software using this methodology:

- **40-50% timeline reduction** through structured decision-making
- **77 hours saved** through pre-flight verification (catching issues before implementation)
- **60% fewer revision cycles** on specs grounded in deep research
- **Seeds from early projects** directly improved later project outcomes

## Philosophical Foundations

**Pace of Understanding:** Work at the speed of comprehension, not expectation. Time spent understanding isn't overhead — it IS the work.

**Governance Multiplies Velocity:** Structure isn't bureaucracy. The right constraints (scout before deciding, spec before building, retro before starting over) make you faster, not slower.

**Knowledge as Commons:** Every seed, template, and skill is open. The methodology improves when more people use it and contribute back.

---

*From the methodology paper: "Git for Strategy: Operationalizing Agentic Orchestration through Protocol Plugins and Planning with Files"*
