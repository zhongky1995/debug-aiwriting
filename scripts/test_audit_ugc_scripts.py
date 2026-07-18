#!/usr/bin/env python3
"""Regression tests for the deterministic UGC script audit."""

from __future__ import annotations

import unittest

from audit_ugc_scripts import audit


def sample_script(*cells: str, empty_slots: int = 0) -> dict[str, object]:
    return {
        "title": "示例脚本",
        "persona": "普通家庭成员",
        "voice": "自然口播",
        "speech_cells": list(cells),
        "speech_slot_count": len(cells) + empty_slots,
        "empty_speech_slot_count": empty_slots,
        "speech": "\n".join(cells),
    }


class AuditUgcScriptsTest(unittest.TestCase):
    def test_finds_implicit_thesis_and_awkward_collocation(self) -> None:
        report = audit(
            [
                sample_script(
                    "路线由我安排，座位让他自己挑。",
                    "以前总是临时协调，现在先把兴趣问清。",
                )
            ]
        )

        self.assertGreater(report["pattern_totals"]["hidden_author_thesis"], 0)
        self.assertGreater(report["pattern_totals"]["unnatural_collocation"], 0)

    def test_finds_compressed_slogan_and_tidy_resolution(self) -> None:
        report = audit(
            [
                sample_script(
                    "分两天，座位舒服，聊天从容。",
                    "他听得尽兴，走起来也不累，这次安排就对了。",
                )
            ]
        )

        self.assertGreater(report["pattern_totals"]["compressed_slogan"], 0)
        self.assertEqual(report["ending_counts"]["tidy_resolution"], 1)

    def test_reports_slot_pressure(self) -> None:
        report = audit(
            [
                sample_script("第一句。", "第二句。"),
                sample_script("保留一句。", empty_slots=1),
            ]
        )

        self.assertEqual(report["speech_slot_count"], 4)
        self.assertEqual(report["empty_speech_slot_count"], 1)
        self.assertEqual(report["fully_filled_script_count"], 1)


if __name__ == "__main__":
    unittest.main()
