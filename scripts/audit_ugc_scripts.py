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
        cells = [
            row[speech_column].strip()
            for row in rows[header_index + 1 :]
            if speech_column < len(row) and row[speech_column].strip()
        ]
        if cells:
            scripts.append(
                {
                    "title": current_title,
                    "persona": current_persona,
                    "voice": current_voice,
                    "speech_cells": cells,
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
}


def audit(scripts: list[dict[str, object]]) -> dict[str, object]:
    totals: Counter[str] = Counter()
    scripts_with: Counter[str] = Counter()
    endings = Counter()
    ending_examples: list[dict[str, str]] = []

    for script in scripts:
        speech = str(script["speech"])
        for name, pattern in PATTERNS.items():
            hits = re.findall(pattern, speech, flags=re.S)
            if hits:
                totals[name] += len(hits)
                scripts_with[name] += 1
        final_cell = str(script["speech_cells"][-1])
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
        "ending_counts": endings,
        "ending_examples": ending_examples,
        "scripts": scripts,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = audit(extract_scripts(args.docx))
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
