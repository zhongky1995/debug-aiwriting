#!/usr/bin/env python3
"""Audit Chinese UGC/persona script banks stored in DOCX tables.

The script is deterministic and diagnostic. It does not rewrite copy.
"""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{%s}" % NS["w"]


def text_of(element: ET.Element) -> str:
    parts: list[str] = []
    for node in element.iter():
        if node.tag == W + "t" and node.text:
            parts.append(node.text)
        elif node.tag == W + "tab":
            parts.append("\t")
        elif node.tag in {W + "br", W + "cr"}:
            parts.append("\n")
    return re.sub(r"[ \t]+", " ", "".join(parts)).strip()


def cell_text(cell: ET.Element) -> str:
    return "\n".join(
        part
        for part in (text_of(p) for p in cell.findall(".//w:p", NS))
        if part
    ).strip()


def table_rows(table: ET.Element) -> list[list[str]]:
    return [
        [cell_text(cell) for cell in row.findall("./w:tc", NS)]
        for row in table.findall("./w:tr", NS)
    ]


def title_candidate(text: str) -> bool:
    return bool(re.match(r"^\d{1,3}[.、]\s*\S", text)) and len(text) <= 100


def extract_scripts(docx: Path) -> list[dict[str, object]]:
    with zipfile.ZipFile(docx) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    body = root.find("w:body", NS)
    if body is None:
        raise RuntimeError("word/document.xml has no body")

    scripts: list[dict[str, object]] = []
    current_title = ""
    current_persona = ""
    current_voice = ""

    for child in list(body):
        if child.tag == W + "p":
            text = text_of(child)
            if title_candidate(text):
                current_title = text
                current_persona = ""
                current_voice = ""
            elif text.startswith("网感人设："):
                current_persona = text.removeprefix("网感人设：").strip()
            elif text.startswith("配音音色："):
                current_voice = text.removeprefix("配音音色：").strip()
            continue
        if child.tag != W + "tbl":
            continue
        rows = table_rows(child)
        speech_column = None
        header_index = 0
        for index, row in enumerate(rows[:5]):
            for column, value in enumerate(row):
                if any(label in value for label in ("口播", "字幕", "花字")):
                    speech_column = column
                    header_index = index
                    break
            if speech_column is not None:
                break
        if speech_column is None:
            continue
        slots = [
            row[speech_column].strip() if speech_column < len(row) else ""
            for row in rows[header_index + 1 :]
            if any(value.strip() for value in row)
        ]
        cells = [value for value in slots if value]
        if cells:
            trailing_empty_count = 0
            for value in reversed(slots):
                if value:
                    break
                trailing_empty_count += 1
            scripts.append(
                {
                    "title": current_title,
                    "persona": current_persona,
                    "voice": current_voice,
                    "speech_cells": cells,
                    "speech_slots": slots,
                    "speech_slot_count": len(slots),
                    "empty_speech_slot_count": sum(not value for value in slots),
                    "literal_final_speech_cell": slots[-1] if slots else "",
                    "trailing_empty_speech_slot_count": trailing_empty_count,
                    "speech": "\n".join(cells),
                }
            )
    return scripts


PATTERNS = {
    "first_person": r"我",
    "reveal_formula": r"我(?:才|终于|后来)?(?:发现|明白|意识到|懂得)",
    "lesson_formula": r"对我来说|最重要的是|真正的.{0,10}是|这才是|这就是|说到底",
    "comparison_judgment": r"比.{0,24}(?:更重要|更有意义|更有分量|更值得)",
    "forced_contrast": r"不是.{0,36}而是|不仅.{0,36}(?:而且|更)",
    "audience_question": r"你(?:家|们|会|觉得|最|通常|一般).{0,32}[？?]",
    "tts_mechanical": r"机械音|网红音|TTS",
    "hidden_author_thesis": (
        r"没替.{0,12}做主|不让.{0,24}变成|"
        r"(?:路线|行程|时间).{0,8}(?:由我|我来)安排|"
        r"(?:座位|选择).{0,8}让.{0,8}自己(?:挑|选|决定)|"
        r"谁都不用|两边.{0,16}都能|这次安排(?:就|才)?对了|"
        r"兴致才能|聊天从容"
    ),
    "unnatural_collocation": (
        r"把兴趣问清|遇到现场演出|只扶手肘|"
        r"订一顿(?:安静)?(?:午餐|晚餐)|变成顺路"
    ),
    "compressed_slogan": (
        r"(?:^|[。！？])[^，,。！？\n]{2,12}[，,]"
        r"[^，,。！？\n]{2,12}[，,][^，,。！？\n]{2,12}(?:[。！？]|$)"
    ),
    "report_checklist": (
        r"(?:提前)?(?:确认|负责|安排|准备|检查|问清).{0,12}"
        r"(?:、[^。；\n]{1,14}){2,}"
    ),
}

RISK_EXAMPLE_LIMIT = 20


def audit(scripts: list[dict[str, object]]) -> dict[str, object]:
    totals: Counter[str] = Counter()
    scripts_with: Counter[str] = Counter()
    endings = Counter()
    ending_examples: list[dict[str, str]] = []
    blank_final_slot_examples: list[dict[str, object]] = []
    risk_examples: dict[str, list[dict[str, object]]] = {
        name: [] for name in PATTERNS
    }

    for script in scripts:
        matched_names: set[str] = set()
        for cell_index, cell_value in enumerate(script["speech_cells"], start=1):
            cell = str(cell_value)
            for name, pattern in PATTERNS.items():
                hits = list(re.finditer(pattern, cell))
                if not hits:
                    continue
                totals[name] += len(hits)
                matched_names.add(name)
                if len(risk_examples[name]) < RISK_EXAMPLE_LIMIT:
                    risk_examples[name].append(
                        {
                            "title": str(script["title"]),
                            "cell_index": cell_index,
                            "text": cell,
                        }
                    )
        for name in matched_names:
            scripts_with[name] += 1
        final_cell = str(script["speech_cells"][-1])
        literal_final_cell = str(script.get("literal_final_speech_cell", ""))
        if not literal_final_cell:
            endings["blank_literal_final_slot"] += 1
            if len(blank_final_slot_examples) < RISK_EXAMPLE_LIMIT:
                blank_final_slot_examples.append(
                    {
                        "title": str(script["title"]),
                        "trailing_empty_speech_slot_count": int(
                            script.get("trailing_empty_speech_slot_count", 0)
                        ),
                        "last_nonempty_speech_cell": final_cell,
                    }
                )
        flags = []
        if re.search(PATTERNS["lesson_formula"], final_cell):
            endings["lesson"] += 1
            flags.append("lesson")
        if re.search(PATTERNS["comparison_judgment"], final_cell):
            endings["comparison_judgment"] += 1
            flags.append("comparison_judgment")
        if re.search(r"[？?]\s*$", final_cell):
            endings["question"] += 1
            flags.append("question")
        if re.search(
            r"以后|下次|这次.{0,12}(?:对了|值了|值得)|才算|就够了|就行了",
            final_cell,
        ):
            endings["tidy_resolution"] += 1
            flags.append("tidy_resolution")
        if flags:
            ending_examples.append(
                {
                    "title": str(script["title"]),
                    "ending": final_cell,
                    "flags": ",".join(flags),
                }
            )

    personas = [str(item["persona"]) for item in scripts if item["persona"]]
    voices = [str(item["voice"]) for item in scripts if item["voice"]]
    return {
        "script_count": len(scripts),
        "script_character_count": sum(len(str(item["speech"])) for item in scripts),
        "persona_count": len(personas),
        "unique_persona_count": len(set(personas)),
        "voice_counts": Counter(voices),
        "pattern_totals": totals,
        "scripts_with_pattern": scripts_with,
        "risk_examples": risk_examples,
        "ending_counts": endings,
        "ending_examples": ending_examples,
        "blank_final_slot_examples": blank_final_slot_examples,
        "speech_slot_count": sum(
            int(item.get("speech_slot_count", len(item["speech_cells"])))
            for item in scripts
        ),
        "empty_speech_slot_count": sum(
            int(item.get("empty_speech_slot_count", 0)) for item in scripts
        ),
        "fully_filled_script_count": sum(
            int(item.get("speech_slot_count", len(item["speech_cells"]))) > 1
            and int(item.get("empty_speech_slot_count", 0)) == 0
            for item in scripts
        ),
        "scripts": scripts,
    }


def compare_endings(
    baseline: list[dict[str, object]], revised: list[dict[str, object]]
) -> dict[str, object]:
    removed: list[dict[str, object]] = []
    for index, (old, new) in enumerate(zip(baseline, revised), start=1):
        old_final = str(old.get("literal_final_speech_cell", ""))
        new_final = str(new.get("literal_final_speech_cell", ""))
        if old_final and not new_final:
            removed.append(
                {
                    "script_index": index,
                    "title": str(new.get("title") or old.get("title") or ""),
                    "baseline_ending": old_final,
                    "revised_last_nonempty_speech_cell": str(
                        new.get("speech_cells", [""])[-1]
                    ),
                    "revised_trailing_empty_speech_slot_count": int(
                        new.get("trailing_empty_speech_slot_count", 0)
                    ),
                }
            )
    return {
        "baseline_script_count": len(baseline),
        "revised_script_count": len(revised),
        "script_count_matches": len(baseline) == len(revised),
        "removed_nonempty_final_count": len(removed),
        "removed_nonempty_final_examples": removed[:RISK_EXAMPLE_LIMIT],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--baseline",
        type=Path,
        help="Optional source DOCX used to detect non-empty endings removed by the rewrite.",
    )
    args = parser.parse_args()
    revised_scripts = extract_scripts(args.docx)
    report = audit(revised_scripts)
    if args.baseline:
        report["ending_comparison"] = compare_endings(
            extract_scripts(args.baseline), revised_scripts
        )
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
