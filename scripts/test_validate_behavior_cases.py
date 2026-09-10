#!/usr/bin/env python3
"""Regression tests for behavior-corpus validation."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from validate_behavior_cases import check_output, validate_corpus


ROOT = Path(__file__).resolve().parents[1]
CORPUS = json.loads((ROOT / "evals/behavior_cases.json").read_text(encoding="utf-8"))


class ValidateBehaviorCasesTest(unittest.TestCase):
    def test_repository_corpus_is_valid(self) -> None:
        self.assertEqual(validate_corpus(CORPUS, ROOT), [])

    def test_output_checker_enforces_literal_invariants(self) -> None:
        case = {
            "must_preserve": ["30天"],
            "must_remove": ["赋能增长"],
            "forbidden_additions": ["自动续费"],
        }
        self.assertEqual(check_output(case, "会员有效期为30天。"), [])
        errors = check_output(case, "自动续费可以赋能增长。")
        self.assertEqual(len(errors), 3)

    def test_cli_does_not_claim_semantic_validation(self) -> None:
        case = next(c for c in CORPUS["cases"] if c["id"] == "paragraph-thesis-return")
        # All literal requirements pass, but the rejected rhetorical function remains.
        candidate = "剪辑软件里的返修时长尚不明确，我们没有试用。核心永远在于人的眼光。人的眼光决定一切。"
        self.assertEqual(check_output(case, candidate), [])
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "candidate.txt"
            output.write_text(candidate, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / "scripts/validate_behavior_cases.py"),
                 str(ROOT / "evals/behavior_cases.json"), "--skill-root", str(ROOT),
                 "--case", case["id"], "--output", str(output)],
                text=True, capture_output=True, check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Semantic behavior_checks and style fit were not evaluated", result.stdout)


if __name__ == "__main__":
    unittest.main()
