---
name: semantic-clustering
tagline: Map what a system does, not where its files live.
group: structure
triggers:
  - what does this system do
  - understand the codebase
  - architecture map
  - capabilities
  - where does this live
---

# Semantic Clustering

*Map what a system does, not where its files live.*

## What it is

Group a system's parts by the actions they perform — verb clusters such as "authenticates users" — instead of by directory.

## Why it matters

File trees hide behavior. One capability can span five directories; one directory can hold three unrelated capabilities. Clustering by action shows the gaps and the confusion that the tree conceals.

## The pattern

1. List every action the system performs, as verbs.
2. Group the actions into clusters.
3. Map files to clusters. A file may belong to several.
4. Note clusters with no files (gaps) and files with no clear cluster (confusion).

## Revisit when

You are about to write the current-state section of a spec. You are new to a system.

## What it refuses

Treating the directory tree as the architecture.

## Grew from

Codebase audits in the Dojo Genesis practice, done before specifying work on existing systems.
