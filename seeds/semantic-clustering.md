# Seed: Semantic Clustering

**Confidence:** High — validated in codebase analysis

## Trigger
When you need to understand what a system does. When file structure doesn't reveal behavior.

## Pattern
Map system capabilities using action-verb clusters that group components by what they DO, not where they live. "Authenticates users" is a cluster that might span 5 directories. This reveals capabilities, gaps, and architectural confusion that file trees hide.

## Steps
1. List every action the system performs (use verbs)
2. Group actions into clusters (authentication, data processing, etc.)
3. Map files to clusters (a file can belong to multiple clusters)
4. Identify gaps (clusters with no files) and confusion (files in wrong clusters)

## Evidence
Semantic clustering of a 83,000-line codebase revealed 3 capability gaps invisible in the file tree.

## Anti-Pattern
File-tree thinking — assuming directory structure = system architecture. It often doesn't.
