# Field Seed: Portability Tiers

**Confidence:** Medium — validated in one ecosystem

## Trigger
When classifying components by how portable they are across environments.

## Pattern
Classify by dependency depth:
- **Tier 1 (Fully Portable):** No external dependencies. Works anywhere.
- **Tier 2 (Needs Adapters):** Requires common tools (web search, file system). Portable with thin adapters.
- **Tier 3 (Platform-Specific):** Requires platform abstractions. Needs refactoring to port.
- **Tier 4 (Locked In):** Deep platform integration. Not portable without rewrite.

## Evidence
49 skills classified: 28 Tier 1, 12 Tier 2, 4 Tier 3, 0 Tier 4. Guided prioritization of cross-platform support.
