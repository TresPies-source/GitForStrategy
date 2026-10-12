"""Tests for scripts/gfs.py and hooks/session_start.py. Standard library only.

Run from the repository root: python3 -m unittest discover -s tests
"""

import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GFS = ROOT / "scripts" / "gfs.py"
HOOK = ROOT / "hooks" / "session_start.py"
TYPES = ["scout", "decision", "spec", "contract", "commission", "research",
         "runbook", "audit", "draft", "retro", "session", "seed"]


def run(*args, cwd=None, env=None):
    return subprocess.run([sys.executable, str(GFS), *args], cwd=cwd, env=env,
                          capture_output=True, text=True)


class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.ws = Path(self._tmp.name) / "ws"
        result = run("init", "--root", str(self.ws), "--name", "test")
        self.assertEqual(result.returncode, 0, result.stderr)

    def tearDown(self):
        self._tmp.cleanup()

    def new(self, kind, title, date="2026-10-01"):
        result = run("new", kind, title, "--root", str(self.ws), "--date", date)
        self.assertEqual(result.returncode, 0, result.stderr)
        return Path(result.stdout.strip())

    def validate(self, *extra):
        return run("validate", "--root", str(self.ws), *extra)

    def write(self, rel, text):
        path = self.ws / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")
        return path

    def replace(self, path, old, new):
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")


class InitAndNew(WorkspaceTest):
    def test_init_creates_workspace(self):
        for name in ["STRATEGY.md", "STATUS.md", "scouts", "decisions", "specs", "commissions", "retros"]:
            self.assertTrue((self.ws / name).exists(), name)

    def test_init_keeps_existing_files(self):
        (self.ws / "STRATEGY.md").write_text("# mine\n", encoding="utf-8")
        result = run("init", "--root", str(self.ws))
        self.assertEqual(result.returncode, 0)
        self.assertIn("kept", result.stdout)
        self.assertEqual((self.ws / "STRATEGY.md").read_text(encoding="utf-8"), "# mine\n")

    def test_every_template_validates(self):
        for kind in TYPES:
            self.new(kind, f"Example {kind}")
        report = json.loads(self.validate("--json").stdout)
        self.assertEqual(report["errors"], [])
        # A fresh commission has no spec to link yet; that is the only warning a blank template earns.
        self.assertEqual([w["message"] for w in report["warnings"]],
                         ["links no spec — a commission should link the spec it implements"])

    def test_names_follow_the_contract(self):
        self.assertEqual(self.new("scout", "Native or web?").name, "2026-10-01_native-or-web.md")
        self.assertEqual(self.new("spec", "Offline Sync").name, "offline-sync.md")
        self.assertEqual(self.new("decision", "First").name, "001-first.md")
        self.assertEqual(self.new("decision", "Second").name, "002-second.md")

    def test_new_refuses_to_overwrite(self):
        self.new("spec", "Same")
        result = run("new", "spec", "Same", "--root", str(self.ws))
        self.assertNotEqual(result.returncode, 0)

    def test_new_without_workspace_fails_clearly(self):
        with tempfile.TemporaryDirectory() as empty:
            result = run("new", "scout", "x", cwd=empty)
        self.assertEqual(result.returncode, 2)
        self.assertIn("no workspace", result.stderr)


class Validate(WorkspaceTest):
    def test_missing_required_section(self):
        path = self.new("scout", "Tension")
        self.replace(path, "## Verification", "## Notes")
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing required section `## Verification`", result.stdout)

    def test_bad_status(self):
        path = self.new("spec", "Thing")
        self.replace(path, "**Status:** Draft", "**Status:** Almost done")
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("is not one of", result.stdout)

    def test_superseded_status_with_pointer_is_valid(self):
        path = self.new("decision", "Old call")
        self.replace(path, "**Status:** Proposed", "**Status:** Superseded by 002")
        self.assertEqual(self.validate().returncode, 0)

    def test_broken_link(self):
        path = self.new("scout", "Linked")
        self.replace(path, "**Related:** —", "**Related:** [gone](../decisions/999-gone.md)")
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("broken link", result.stdout)

    def test_links_in_code_are_not_checked(self):
        path = self.new("scout", "Code")
        text = path.read_text(encoding="utf-8")
        text += "\nUse `[x](missing.md)` inline.\n\n```\n[y](also-missing.md)\n```\n"
        path.write_text(text, encoding="utf-8")
        self.assertEqual(self.validate().returncode, 0)

    def test_bad_file_name(self):
        self.write("scouts/Not A Good Name.md", """
            # Scout: x

            **Date:** 2026-10-01
            **Status:** Open

            ## Tension
            ## Routes
            ## Open questions
            ## Verification
            """)
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("file name should look like", result.stdout)

    def test_duplicate_decision_numbers(self):
        self.new("decision", "One")
        first = self.ws / "decisions" / "001-one.md"
        (self.ws / "decisions" / "001-other.md").write_text(first.read_text(encoding="utf-8"), encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("used twice", result.stdout)

    def test_simple_dated_decision_is_conformant_with_warnings(self):
        self.write("decisions/2026-10-01_use-postgres.md", """
            # ADR: Use Postgres

            ## Context

            We need a database.

            ## Decision

            Postgres.

            ## Consequences

            One more service to run.
            """)
        self.assertEqual(self.validate().returncode, 0)
        strict = self.validate("--strict")
        self.assertEqual(strict.returncode, 1)
        self.assertIn("read as Proposed", strict.stdout)

    def test_status_must_match_exactly(self):
        spec = self.new("spec", "Almost")
        self.replace(spec, "**Status:** Draft", "**Status:** Ready for review")
        self.assertEqual(self.validate().returncode, 1)

    def test_accepted_decision_needs_decider_and_ruling(self):
        decision = self.new("decision", "Unruled")
        self.replace(decision, "**Status:** Proposed", "**Status:** Accepted")
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("needs a **Decider:**", result.stdout)
        self.assertIn("needs the ruling", result.stdout)

    def test_ruling_in_a_comment_does_not_count(self):
        decision = self.new("decision", "Hidden")
        self.replace(decision, "**Status:** Proposed", "**Status:** Accepted")
        self.replace(decision, "**Decider:**", "**Decider:** Ana")
        self.replace(decision, "## Ruling\n", "## Ruling\n\n<!-- \"Do it.\" -->\n")
        self.assertIn("needs the ruling", self.validate().stdout)

    def test_byte_order_mark_and_bad_encoding(self):
        path = self.new("scout", "Bom")
        path.write_bytes(b"\xef\xbb\xbf" + path.read_bytes())
        self.assertEqual(self.validate().returncode, 0)
        (self.ws / "scouts" / "2026-10-01_latin.md").write_bytes("# Scout: caf\xe9\n".encode("latin-1"))
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("not valid UTF-8", result.stdout)

    def test_link_forms(self):
        path = self.new("scout", "Links")
        (self.ws / "files").mkdir()
        (self.ws / "files" / "a b.md").write_text("x", encoding="utf-8")
        text = path.read_text(encoding="utf-8")
        text += "\n[spaced](../files/a%20b.md) [angle](<../files/a b.md>) [root](/elsewhere.md)\n"
        text += "<!-- [hidden](missing.md) -->\n"
        path.write_text(text, encoding="utf-8")
        self.assertEqual(self.validate().returncode, 0, self.validate().stdout)

    def test_year_named_decision_is_not_a_number(self):
        self.write("decisions/2026-pricing.md", "# x\n")
        result = self.validate()
        self.assertIn("file name should look like", result.stdout)
        self.assertEqual(self.new("decision", "Next").name, "001-next.md")

    def test_compact_dates_are_rejected_on_every_python(self):
        path = self.new("spec", "Compact")
        self.replace(path, "**Date:** 2026-10-01", "**Date:** 20261001")
        self.assertIn("is not YYYY-MM-DD", self.validate().stdout)

    def test_fixed_files_need_title_and_date(self):
        status = self.ws / "STATUS.md"
        status.write_text(status.read_text(encoding="utf-8").replace("**Date:**", "**Dated:**"), encoding="utf-8")
        self.assertIn("**Date:** header field", self.validate().stdout)

    def test_runs_from_a_subfolder(self):
        result = run("validate", cwd=self.ws / "scouts")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_seed_name_must_match_file(self):
        path = self.new("seed", "Good seed")
        self.replace(path, "name: good-seed", "name: other-name")
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("should match file name", result.stdout)

    def test_missing_nexus_is_an_error(self):
        (self.ws / "STRATEGY.md").unlink()
        (self.ws / "strategy").mkdir()
        result = run("validate", "--root", str(self.ws))
        self.assertEqual(result.returncode, 2)

    def test_json_output(self):
        result = self.validate("--json")
        data = json.loads(result.stdout)
        self.assertEqual(data["errors"], [])


class StatusAndGate(WorkspaceTest):
    def test_open_scout_needs_attention_after_two_weeks(self):
        self.new("scout", "Old tension", date="2026-09-01")
        report = json.loads(run("status", "--root", str(self.ws), "--json", "--today", "2026-10-01").stdout)
        self.assertTrue(any("still Open" in item for item in report["attention"]))
        scout = [p for p in report["phases"] if p["phase"] == "Explore"][0]
        self.assertEqual(scout["state"], "dormant")

    def test_done_commission_needs_a_retro(self):
        commission = self.new("commission", "Build it")
        self.replace(commission, "**Status:** Draft", "**Status:** Done")
        report = json.loads(run("status", "--root", str(self.ws), "--json").stdout)
        self.assertTrue(any("no retro yet" in item for item in report["attention"]))
        retro = self.new("retro", "Look back")
        self.replace(retro, "**Related:** —", f"**Related:** [Commission](../commissions/{commission.name})")
        report = json.loads(run("status", "--root", str(self.ws), "--json").stdout)
        self.assertFalse(any("no retro yet" in item for item in report["attention"]))

    def test_open_propagation_needs_attention(self):
        decision = self.new("decision", "Ripple")
        self.rule(decision)
        self.replace(decision, "### Propagation\n", "### Propagation\n\n- [ ] Update the README\n")
        report = json.loads(run("status", "--root", str(self.ws), "--json").stdout)
        self.assertTrue(any("propagation item still open" in item for item in report["attention"]))

    def test_gate_ignores_checkboxes_in_code(self):
        spec = self.ready_spec(checkbox=False)
        self.replace(spec, "## Success criteria\n", "## Success criteria\n\n```\n- [ ] not real\n```\n")
        self.assertEqual(self.gate(spec).returncode, 1)

    def test_gate_needs_a_ruling_on_the_decision(self):
        spec = self.ready_spec(accepted=False)
        decision = next((self.ws / "decisions").glob("*.md"))
        self.replace(decision, "**Status:** Proposed", "**Status:** Accepted")
        self.assertEqual(self.gate(spec).returncode, 1)

    def test_gate_bad_today_is_a_usage_error(self):
        self.assertEqual(self.gate(self.ready_spec(), today="nope").returncode, 2)

    def test_brief_status_is_short(self):
        result = run("status", "--root", str(self.ws), "--brief")
        self.assertEqual(result.returncode, 0)
        self.assertLessEqual(len(result.stdout.strip().splitlines()), 2)

    def rule(self, decision, status="Accepted"):
        self.replace(decision, "**Status:** Proposed", f"**Status:** {status}")
        self.replace(decision, "**Decider:**", "**Decider:** Ana")
        self.replace(decision, "## Ruling\n", "## Ruling\n\n> \"Do it.\" — Ana, 2026-10-01\n")

    def ready_spec(self, accepted=True, checkbox=True):
        decision = self.new("decision", "The call")
        if accepted:
            self.rule(decision)
        spec = self.new("spec", "The build", date="2026-10-01")
        self.replace(spec, "**Status:** Draft", "**Status:** Ready")
        self.replace(spec, "**Related:** —", f"**Related:** [Decision](../decisions/{decision.name})")
        if checkbox:
            self.replace(spec, "## Success criteria\n", "## Success criteria\n\n- [ ] It works offline\n")
        return spec

    def gate(self, spec, today="2026-10-02"):
        return run("gate", str(spec), "--root", str(self.ws), "--today", today)

    def test_gate_passes_a_ready_spec(self):
        result = self.gate(self.ready_spec())
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("Gate: PASS", result.stdout)

    def test_gate_needs_an_accepted_decision(self):
        result = self.gate(self.ready_spec(accepted=False))
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL  links an Accepted decision", result.stdout)

    def test_gate_needs_a_checkbox_criterion(self):
        result = self.gate(self.ready_spec(checkbox=False))
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL  states a success criterion", result.stdout)

    def test_gate_warns_on_a_stale_spec(self):
        result = self.gate(self.ready_spec(), today="2026-11-01")
        self.assertEqual(result.returncode, 0)
        self.assertIn("WARN", result.stdout)


class SeedsAndSelfcheck(unittest.TestCase):
    def test_suggest_finds_the_human_agency_seed(self):
        result = run("seeds", "suggest", "just decide for me and make the call", cwd=tempfile.gettempdir())
        self.assertEqual(result.returncode, 0)
        self.assertIn("partnership-not-autopilot", result.stdout.splitlines()[0])

    def test_seed_index_matches_disk(self):
        self.assertEqual(run("seeds", "check").returncode, 0)

    def test_selfcheck_is_clean(self):
        result = run("selfcheck")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_example_and_own_workspace_pass_strict(self):
        for root in (ROOT / "examples" / "native-or-web", ROOT / "strategy"):
            result = run("validate", "--root", str(root), "--strict")
            self.assertEqual(result.returncode, 0, f"{root}: {result.stdout}")


class Hook(unittest.TestCase):
    def run_hook(self, cwd, **env):
        merged = {k: v for k, v in os.environ.items() if k not in ("DOJO_OFF", "GFS_OFF")}
        merged.update(env)
        return subprocess.run([sys.executable, str(HOOK)], cwd=cwd, env=merged, capture_output=True, text=True)

    def test_silent_outside_a_workspace(self):
        with tempfile.TemporaryDirectory() as empty:
            result = self.run_hook(empty)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_reports_inside_a_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            run("init", "--root", tmp)
            result = self.run_hook(tmp)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["hookSpecificOutput"]["hookEventName"], "SessionStart")
        self.assertIn("Strategy workspace", payload["hookSpecificOutput"]["additionalContext"])

    def test_off_switches(self):
        with tempfile.TemporaryDirectory() as tmp:
            run("init", "--root", tmp)
            for name in ("DOJO_OFF", "GFS_OFF"):
                result = self.run_hook(tmp, **{name: "1"})
                self.assertEqual(result.stdout, "", name)


if __name__ == "__main__":
    unittest.main()
