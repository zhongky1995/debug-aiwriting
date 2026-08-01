#!/usr/bin/env python3
"""Regression tests for the deterministic surface audit."""

from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from audit_surfaces import audit


def audit_text(text: str, custom_terms: list[str] | None = None) -> dict[str, object]:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "sample.md"
        path.write_text(text, encoding="utf-8")
        return audit(path, custom_terms or [])


def audit_archive(extension: str, parts: dict[str, str]) -> dict[str, object]:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / f"sample.{extension}"
        with zipfile.ZipFile(path, "w") as archive:
            for name, content in parts.items():
                archive.writestr(name, content)
        return audit(path, [])


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

    def test_extracts_docx_headings_tables_and_footnotes(self) -> None:
        report = audit_archive(
            "docx",
            {
                "word/document.xml": """
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>行业报告显示</w:t></w:r>
    </w:p>
    <w:tbl><w:tr><w:tc><w:p><w:r><w:t>赋能增长</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
  </w:body>
</w:document>
""",
                "word/footnotes.xml": """
<w:footnotes xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:footnote w:id="1"><w:p><w:r><w:t>当然可以</w:t></w:r></w:p></w:footnote>
</w:footnotes>
""",
            },
        )

        self.assertEqual(report["format"], "docx")
        self.assertEqual(report["surface_counts"]["heading"], 1)  # type: ignore[index]
        self.assertEqual(report["surface_counts"]["table_cell"], 1)  # type: ignore[index]
        self.assertEqual(report["surface_counts"]["footnote"], 1)  # type: ignore[index]
        found = categories(report)
        self.assertIn("vague_attribution", found)
        self.assertIn("abstract_action", found)
        self.assertIn("collaboration_residue", found)

    def test_extracts_pptx_titles_tables_notes_alt_text_and_charts(self) -> None:
        report = audit_archive(
            "pptx",
            {
                "ppt/slides/slide1.xml": """
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
       xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:cSld><p:spTree>
    <p:sp>
      <p:nvSpPr><p:cNvPr id="2" name="标题" descr="进一步彰显"/><p:nvPr><p:ph type="title"/></p:nvPr></p:nvSpPr>
      <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:t>挑战与未来展望</a:t></a:r></a:p></p:txBody>
    </p:sp>
    <p:graphicFrame><a:tbl><a:tr><a:tc><a:txBody><a:p><a:r><a:t>专家认为</a:t></a:r></a:p></a:txBody></a:tc></a:tr></a:tbl></p:graphicFrame>
  </p:spTree></p:cSld>
</p:sld>
""",
                "ppt/notesSlides/notesSlide1.xml": """
<p:notes xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
         xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:cSld><p:spTree><p:sp><p:txBody><a:p><a:r><a:t>希望这对你有帮助</a:t></a:r></a:p></p:txBody></p:sp></p:spTree></p:cSld>
</p:notes>
""",
                "ppt/charts/chart1.xml": """
<c:chartSpace xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart">
  <c:chart><c:title><c:tx><c:rich><a:p xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:r><a:t>相关数据显示</a:t></a:r></a:p></c:rich></c:tx></c:title></c:chart>
</c:chartSpace>
""",
            },
        )

        self.assertEqual(report["format"], "pptx")
        counts = report["surface_counts"]  # type: ignore[assignment]
        self.assertEqual(counts["heading"], 1)
        self.assertEqual(counts["table_cell"], 1)
        self.assertEqual(counts["note"], 1)
        self.assertEqual(counts["caption"], 1)
        self.assertEqual(counts["chart_text"], 1)
        found = categories(report)
        self.assertIn("generic_outlook", found)
        self.assertIn("vague_attribution", found)
        self.assertIn("tail_pseudo_analysis", found)
        self.assertIn("collaboration_residue", found)

    def test_rejects_invalid_ooxml_archives(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.docx"
            path.write_text("not a zip", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Invalid DOCX"):
                audit(path, [])


if __name__ == "__main__":
    unittest.main()
