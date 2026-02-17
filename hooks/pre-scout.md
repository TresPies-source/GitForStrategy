# Hook: Pre-Scout

**Runs before:** `/scout` command
**Purpose:** Ensure the scout starts from a real tension, not a premature solution.

## Checks

1. **Is this a tension or a solution?**
   - Good: "We need to balance speed and quality"
   - Bad: "We should use React"
   - If it's a solution, help the user find the underlying tension

2. **Has this tension been scouted before?**
   - Check `scouts/` for existing scouts on similar topics
   - If yes, suggest iterative-scouting instead of a fresh scout

3. **Is there enough context?**
   - Check if relevant files, specs, or research exist
   - Suggest `/explore` first if the domain is unfamiliar

## Actions

- If tension is actually a solution → reframe before proceeding
- If previously scouted → load prior scout and use iterative-scouting
- If context is thin → suggest `/explore` first
- Otherwise → proceed with scout
