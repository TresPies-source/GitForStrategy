---
description: "Scout a strategic tension: hold it open, map routes and tradeoffs, and save the scout as a file before anyone decides."
argument-hint: "<the tension, in your words>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*)
---

Scout this tension: $ARGUMENTS

The person you are working with holds the perspectives and makes the calls. Your part is synthesis, foresight, and next steps.

1. **Find the workspace.** Look for `STRATEGY.md` here or in `strategy/`. If there is none, ask before running `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" init`, and ask whether it should live at the root or in `strategy/`.
2. **Name the tension.** If the argument is empty or names a solution rather than a tension, ask: "What two goods are pulling against each other here?" Write it as "The tension is between A and B," in the person's own words.
3. **Check for prior work.** Search `scouts/`, `decisions/`, and `research/` for this tension. If it was scouted or decided before, say so and link it rather than starting over.
4. **Create the file.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" new scout "<short title>"` and fill in the file it prints.
5. **Map the routes.** First ask which routes the person already sees. Then add routes only where theirs leave ground uncovered, and mark those as yours. Three to five distinct routes in all, each with what you gain, what you give up, risk, and rough size. Present every route before naming any default.
6. **Cross-route patterns and open questions.** What holds on every route? What must be answered before deciding? If three or more open questions need evidence, suggest a research dossier (`gfs.py new research`).
7. **Default.** Name one only if every piece of evidence it rests on is in hand. Otherwise write "No default yet. This is what would decide it:" and list the missing evidence.
8. **Verification.** Say what you checked against the real repository or sources while writing, and what you did not.
9. **Check your work.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gfs.py" validate` and fix any error in the file you wrote before reporting.

Leave the scout's Status at Open. Offer next moves: scout again with a reframed question, gather evidence, or `/decide` once the person is ready to rule.

If the Dojo Genesis `strategic-thinking` plugin is installed, its `strategic-scout` and `iterative-scouting` skills go deeper on technique. This command keeps the file contract either way.
