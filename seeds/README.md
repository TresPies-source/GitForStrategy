# Seeds

*Patterns that grew from real work, kept where the next scout can find them.*

A seed names a situation you will meet again and what to do when you meet it. Each one says where it grew from. Seeds come from experience, not theory.

Seeds here are primitives: plain files with no promotion rules, scores, or lifecycle attached. Use them, copy them, or plant your own in a workspace's `seeds/` folder.

## Using seeds

- Suggest seeds for what you are working on: `python3 scripts/gfs.py seeds suggest "we keep re-arguing the same decision"`
- In Claude Code: `/seed`
- Plant a new one from a retro: `python3 scripts/gfs.py new seed "Name of the pattern"`

## Format

YAML front matter with `name` (matching the file name), `tagline`, `group`, and `triggers` — phrases someone says when the seed applies. Then six sections: What it is, Why it matters, The pattern, Revisit when, What it refuses, Grew from.

## Index

The table below is generated from the files in this folder (`gfs.py seeds index --write --plugin`) and checked in CI (`gfs.py selfcheck`). Edit the seed files, not the table.

<!-- seeds:start -->
### Foundations

| Seed | Tagline |
|---|---|
| [Cost Consciousness](cost-consciousness.md) | Treat cost as a design constraint, not a bill to fix later. |
| [Liberation Psychology](liberation-psychology.md) | Remove the barrier, not the person. |
| [Pace of Understanding](pace-of-understanding.md) | Work at the pace of understanding, not the pace of expectation. |
| [Partnership, Not Autopilot](partnership-not-autopilot.md) | You bring the perspectives. The method brings synthesis, foresight, and next steps. |
| [Patient Learning](patient-learning.md) | Use method to keep learning from turning into a rabbit hole. |
| [Voice Before Structure](voice-before-structure.md) | Read the project's voice before you fill in its templates. |

### Structure

| Seed | Tagline |
|---|---|
| [Era Architecture](era-architecture.md) | Group releases into eras that share constraints and vocabulary. |
| [Portability Tiers](portability-tiers.md) | Classify what you build by how deep its dependencies go. |
| [Semantic Clustering](semantic-clustering.md) | Map what a system does, not where its files live. |
| [Spec-to-Prompt Pipeline](spec-to-prompt-pipeline.md) | A spec is not a build brief. Translate it, and check readiness first. |
| [Three-Tiered Governance](three-tiered-governance.md) | Principles constrain protocols. Protocols enable practices. Practices test principles. |

### Grounding

| Seed | Tagline |
|---|---|
| [Audit, Then Scout, Then Spec](audit-scout-spec.md) | Audit before you scout. Scout before you spec. |
| [The Inference Trap](inference-trap.md) | A guess that looks correct is worse than a visible failure. |
| [Never Spec from Documentation Alone](never-spec-from-docs-alone.md) | Documentation drifts. Spec against the thing itself. |

### Deciding

| Seed | Tagline |
|---|---|
| [Record Dissent and Revisit Triggers](record-dissent-and-revisit.md) | A decision that records its dissent and its revisit triggers survives challenge. |
| [Reframe Before Spec](reframe-before-spec.md) | Specs lock you in. Reframes free you up. |
| [Two-Sided Contracts](two-sided-contracts.md) | An integration contract is only as strong as its weaker side. |

### Honesty

| Seed | Tagline |
|---|---|
| [Fabricate Nothing](fabricate-nothing.md) | Say "not measured," and say how you would measure it. |
| [Measure the Corrective](measure-the-corrective.md) | When a fix works, measure what it changed. |
| [Stubs Are Lies](stubs-are-lies.md) | A visible gap is honest. A stub that looks finished is not. |

### Execution

| Seed | Tagline |
|---|---|
| [Pre-flight Hard Stop](preflight-hard-stop.md) | If any pre-flight check fails, stop and report. Don't build on partial ground. |
| [Ship Coupled Work Together](ship-coupled-work-together.md) | When two deliverables will integrate at once, ship them together. |
| [The Spec-Quality Paradox](spec-quality-paradox.md) | The better the spec, the easier it is to fake grounding. |
<!-- seeds:end -->
