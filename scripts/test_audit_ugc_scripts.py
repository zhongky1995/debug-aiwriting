#!/usr/bin/env python3
"""Regression tests for the deterministic UGC script audit."""

from __future__ import annotations

import unittest

from audit_ugc_scripts import audit


def sample_script(
    *cells: str,
    empty_slots: int = 0,
    title: str = "示例脚本",
    persona: str = "普通家庭成员",
    voice: str = "自然口播",
) -> dict[str, object]:
    return {
        "title": title,
        "persona": persona,
        "voice": voice,
        "speech_cells": list(cells),
        "literal_final_speech_cell": cells[-1] if cells and not empty_slots else "",
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

    def test_reports_voice_concentration(self) -> None:
        report = audit(
            [
                sample_script("这是第一条足够长的口播内容。"),
                sample_script("这是第二条足够长的口播内容。"),
                sample_script("这是第三条足够长的口播内容。"),
            ]
        )

        self.assertEqual(report["voice_stats"]["unique_voice_instruction_count"], 1)
        self.assertEqual(report["voice_stats"]["dominant_voice_instruction_share"], 1.0)

    def test_reports_exact_duplicate_scripts_and_cells(self) -> None:
        repeated = "这是一段长度足够、会被完整复制到不同编号脚本里的口播内容。"
        report = audit(
            [
                sample_script(repeated, "第二格也保持完全一致，用于检查整段重复。"),
                sample_script(repeated, "第二格也保持完全一致，用于检查整段重复。"),
            ]
        )

        self.assertEqual(
            report["duplicate_stats"]["exact_duplicate_script_group_count"], 1
        )
        self.assertGreaterEqual(
            report["duplicate_stats"]["repeated_speech_cell_group_count"], 2
        )

    def test_reports_metadata_gaps_and_repeated_titles(self) -> None:
        report = audit(
            [
                sample_script("第一条。", title="同名脚本"),
                sample_script("第二条。", title="同名脚本", persona="", voice=""),
                sample_script("第三条。", title=""),
            ]
        )

        stats = report["metadata_stats"]
        self.assertEqual(stats["missing_title_count"], 1)
        self.assertEqual(stats["missing_persona_count"], 1)
        self.assertEqual(stats["missing_voice_instruction_count"], 1)
        self.assertEqual(stats["repeated_title_group_count"], 1)

    def test_reports_ending_shape_concentration(self) -> None:
        report = audit(
            [
                sample_script("我终于明白，安排得周全才最重要。"),
                sample_script("我觉得，家里人舒服最重要。"),
                sample_script("回家以后，我先把票根收好。"),
            ]
        )

        stats = report["ending_style_stats"]
        self.assertEqual(stats["dominant_ending_mode"], "first_person_judgment")
        self.assertEqual(stats["dominant_ending_mode_count"], 2)
        self.assertEqual(stats["dominant_ending_mode_share"], 0.6667)

    def test_reports_unfinished_and_logistical_ending_tails(self) -> None:
        report = audit(
            [
                sample_script(
                    "散场后他只说了一句：现场还是不一样。",
                    "人少一点以后，我们才慢慢往停车区走。",
                ),
                sample_script(
                    "一个讲笔触，一个讲自己看见了什么。",
                    "走到书店，孩子还没问完。外公又翻了几页，我们就在旁边等着。",
                ),
            ]
        )

        risks = report["ending_style_stats"]["ending_tail_risk_counts"]
        self.assertEqual(risks["routine_logistics"], 2)
        self.assertEqual(risks["unfinished_continuation"], 1)


if __name__ == "__main__":
    unittest.main()
