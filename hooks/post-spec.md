# Hook: Post-Spec

**Runs after:** `/spec` command completes
**Purpose:** Update pipeline state and suggest next steps.

## Actions

1. **Update STATUS.md**
   - Set current phase to "Decide → Complete"
   - Record the spec name and version
   - Update the pipeline state table

2. **Suggest next steps**
   - Primary: `/commission` to generate implementation prompts
   - Alternative: Review with stakeholders before commissioning
   - Reminder: Run `/status` to verify pipeline health

3. **Check for completeness**
   - Does the spec have success criteria?
   - Are dependencies listed?
   - Is scope explicitly bounded (in AND out)?
   - Flag any missing sections
