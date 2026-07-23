#!/usr/bin/env python3
"""Regression tests for the deterministic surface audit."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from audit_surfaces import audit


def audit_text(text: str, custom_terms: list[str] | None = None) -> dict[str, object]:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "sample.md"
        path.write_text(text, encoding="utf-8")
        return audit(path, custom_terms or [])


def categories(report: dict[str, object]) -> set[str]:
    return {
        str(hit["category"])
        for hit in report["high_risk_hits"]  # type: ignore[index]
    }


class AuditSurfacesTest(unittest.TestCase):
    def test_flags_new_semantic_surface_patterns(self) -> None:
        report = audit_text(
            """
# 挑战与未来展望

行业报告显示，这项安排标志着重要转变，这也体现了团队的长期价值。

该项目又被称为计划、方案和机制。
"""
        )

        found = categories(report)
        self.assertIn("vague_attribution", found)
        self.assertIn("inflated_significance", found)
        self.assertIn("tail_pseudo_analysis", found)
        self.assertIn("generic_outlook", found)
        self.assertIn("term_drift_review", found)

    def test_flags_copula_avoidance_and_output_residue(self) -> None:
        report = audit_text(
            """
当然可以，希望这对你有帮助。

这个页面作为团队协作的重要载体，拥有处理复杂任务的能力。

- **关键洞察：** 用户更喜欢简单。

🚀 现在开始——马上行动——不要错过。
"""
        )

        found = categories(report)
        self.assertIn("collaboration_residue", found)
        self.assertIn("copula_avoidance", found)
        self.assertIn("formatting_trace", found)

    def test_does_not_flag_plain_specific_copy(self) -> None:
        report = audit_text(
            """
# 排班工具

这是一款门店排班工具。店长可以查看本周班次，也可以调整员工的上班时间。
"""
        )

        self.assertEqual(report["high_risk_hits"], [])

    def test_keeps_custom_hard_negative_scan(self) -> None:
        report = audit_text("用户重新进入服务链路。", ["服务链路"])
        found = categories(report)

        self.assertIn("user_hard_negative", found)


if __name__ == "__main__":
    unittest.main()
