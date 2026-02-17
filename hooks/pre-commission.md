# Hook: Pre-Commission

**Runs before:** `/commission` command
**Purpose:** Quality gate — verify the spec is ready for implementation.

## Mandatory Checks

1. **Pre-flight checklist**
   - Run `skills/execute/pre-implementation-checklist/SKILL.md`
   - If checklist FAILS → block commission, show issues
   - If checklist PASSES → proceed

2. **Spec freshness**
   - Check spec age — if older than 14 days, flag for review
   - Context may have changed since the spec was written

3. **Dependency check**
   - Are all listed dependencies still available?
   - Has anything changed since the spec was written?

## Actions

- If pre-flight fails → show issues, do NOT proceed to commission
- If spec is stale → warn user, suggest updating spec first
- If dependencies changed → warn user, suggest updating spec
- If all clear → proceed with commission

## Why This Exists

This hook prevents the most expensive mistake in the pipeline: commissioning implementation from a spec that doesn't match reality. The 77 hours saved metric comes primarily from this check.
