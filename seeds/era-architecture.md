# Seed: Era Architecture

**Confidence:** Medium — emerging pattern

## Trigger
When planning work that spans multiple releases. When individual releases feel disconnected from a larger vision.

## Pattern
Group releases into eras with shared vocabulary, architectural constraints, and design language. An era is a conceptual container that gives coherence to 3-5 releases that share a theme.

## Steps
1. Name the era (what's the unifying theme?)
2. Define architectural constraints (what's true for ALL releases in this era?)
3. Define shared vocabulary (what do terms mean in this era?)
4. Plan individual releases within the era's constraints
5. Transition explicitly between eras

## Evidence
Dojo Genesis eras: Foundation (v0.0.1-v0.0.10), Cultivation (v0.0.11-v0.0.16), Harvest (v0.0.17-v0.0.23). Each era had distinct architectural patterns that kept releases coherent.

## Anti-Pattern
Release soup — each release is an island with no shared context. Or eternal era — never transitioning, which prevents evolution.
