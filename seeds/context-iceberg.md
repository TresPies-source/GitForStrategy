# Seed: Context Iceberg

**Confidence:** High — validated in memory systems

## Trigger
When organizing knowledge for efficient retrieval. When context windows feel too small.

## Pattern
Structure information in four tiers, like an iceberg:

1. **Tip (always visible):** One-sentence summary, current status
2. **Waterline (on request):** Key decisions, active work, blockers
3. **Below surface (searchable):** Full reasoning, alternatives considered, evidence
4. **Deep archive (rare access):** Raw data, conversation transcripts, exploration notes

Each tier compresses the one below it. Most retrieval only needs tiers 1-2.

## Steps
1. Write the tip first (force compression)
2. Each lower tier should be 3-5x more detailed than the one above
3. Tag everything with metadata for search
4. Compress regularly (move stale waterline items to below-surface)

## Evidence
4-tier memory system reduced context retrieval time by 70% compared to flat document storage.

## Anti-Pattern
Flat storage — everything at the same depth. Either too much context (overwhelm) or too little (missed information).
