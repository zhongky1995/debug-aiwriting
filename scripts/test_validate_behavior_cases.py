#!/usr/bin/env python3
"""Regression tests for behavior-corpus validation."""

from __future__ import annotations

import json
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


if __name__ == "__main__":
    unittest.main()
