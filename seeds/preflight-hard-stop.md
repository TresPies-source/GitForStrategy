---
name: preflight-hard-stop
tagline: If any pre-flight check fails, stop and report. Don't build on partial ground.
group: execution
triggers:
  - start the build
  - commission
  - missing file
  - kick off implementation
  - hand it off
---

# Pre-flight Hard Stop

*If any pre-flight check fails, stop and report. Don't build on partial ground.*

## What it is

A commission opens with checks the builder runs before writing anything: the files exist and have been read, the dependencies are present, the spec passed its gate. Any failure stops the work.

## Why it matters

The gap between "here is the spec" and "start building" is where builds go wrong. One missing file creates a cascade of plausible mistakes.

## The pattern

1. List every file the build depends on.
2. List the checks, each with a command to run or a place to look.
3. State the stop rule: if any check fails, stop and report.
4. Make it verifiable. The builder confirms each item.

## Revisit when

You write any commission.

## What it refuses

Proceeding on partial infrastructure because most of it is there.

## Grew from

Build briefs in the Dojo Genesis practice, February 2026: "If any check fails, STOP and report the failure. Do not proceed with partial infrastructure."
