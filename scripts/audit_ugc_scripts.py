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


def ending_mode(value: str) -> str:
    """Classify the visible shape of an ending without judging its quality."""
    text = value.strip()
    if re.search(r"[？?]\s*$", text):
        return "question"
    if re.search(r"[“\"]|(?:说|问|回了句|念叨)[：:]?", text):
        return "quote_or_dialogue"
    if re.search(
        r"我(?:才|终于|后来)?(?:发现|明白|意识到|懂得|觉得|认为)|"
        r"对我来说|最重要的是|真正的.{0,10}是|这才是|这就是",
        text,
    ):
        return "first_person_judgment"
    if re.search(
        r"以后|下次|这次.{0,12}(?:对了|值了|值得)|才算|就够了|就行了",
        text,
    ):
        return "tidy_resolution"
    if re.match(
        r"^(?:先|再|等|回去|回家|到家|临走|出门|下次|明天|改天|"
        r"我(?:先|再|去|把|准备|打算|还得))",
        text,
    ):
        return "next_action"
    if re.search(
        r"(?:他|她|爸|妈|孩子|老人|外婆|外公).{0,10}"
        r"(?:笑|点头|摇头|停下|回头|坐下|走|看|拿|放|问|说)",
        text,
    ):
        return "observed_action_or_reaction"
    return "other"


def ending_lead(value: str) -> str:
    """Return a compact opening fragment for spotting repeated ending syntax."""
    text = re.sub(r"^[\s，。！？；：、“”\"']+", "", value)
    if not text:
        return ""
    first_clause = re.split(r"[，,。！？!?；;：:\n]", text, maxsplit=1)[0]
    return first_clause[:10]


ENDING_TAIL_PATTERNS = {
    "unfinished_continuation": (
        r"还没|还在|等着|继续|又(?:翻|问|看|说|走|拿|坐|聊|等)"
    ),
    "routine_logistics": (
        r"(?:往|走向|走到|回到|到了?|去).{0,10}"
        r"(?:停车区|停车场|车里|出口|门口|电梯|休息区|书店)|"
        r"(?:散场|结束|看完|逛完|人少).{0,20}"
        r"(?:离场|回去|回家|上车|停车区|走)|"
        r"(?:收拾|打包|拿好|装好).{0,12}(?:离开|回去|回家|上车)?"
    ),
}


def ending_tail_flags(value: str) -> list[str]:
    """Return warning-only signals that the final line may trail past the payoff."""
    return [
        name
        for name, pattern in ENDING_TAIL_PATTERNS.items()
        if re.search(pattern, value)
    ]


def metadata_report(scripts: list[dict[str, object]]) -> dict[str, object]:
    titles = [str(item.get("title", "")).strip() for item in scripts]
    personas = [str(item.get("persona", "")).strip() for item in scripts]
    voices = [str(item.get("voice", "")).strip() for item in scripts]
    title_counts = Counter(value for value in titles if value)
    persona_counts = Counter(value for value in personas if value)

    repeated_titles = [
        {"title": title, "count": count}
        for title, count in title_counts.most_common()
        if count > 1
    ]
    dominant_persona, dominant_persona_count = (
        persona_counts.most_common(1)[0] if persona_counts else ("", 0)
    )
    return {
        "missing_title_count": sum(not value for value in titles),
        "missing_persona_count": sum(not value for value in personas),
        "missing_voice_instruction_count": sum(not value for value in voices),
        "unique_title_count": len(title_counts),
        "repeated_title_group_count": len(repeated_titles),
        "repeated_title_examples": repeated_titles[:RISK_EXAMPLE_LIMIT],
        "unique_persona_count": len(persona_counts),
        "dominant_persona": dominant_persona,
        "dominant_persona_count": dominant_persona_count,
        "dominant_persona_share": round(
            dominant_persona_count / len([value for value in personas if value]), 4
        )
        if persona_counts
        else 0,
    }


def normalize_duplicate_text(value: str) -> str:
    """Ignore layout whitespace while keeping wording and punctuation exact."""
    return re.sub(r"\s+", "", value).strip()


def duplicate_script_report(scripts: list[dict[str, object]]) -> dict[str, object]:
    full_script_members: dict[str, list[dict[str, object]]] = {}
    speech_cell_members: dict[str, list[dict[str, object]]] = {}

    for script_index, script in enumerate(scripts, start=1):
        speech = str(script.get("speech", ""))
        normalized_script = normalize_duplicate_text(speech)
        if len(normalized_script) >= 40:
            full_script_members.setdefault(normalized_script, []).append(
                {
                    "script_index": script_index,
                    "title": str(script.get("title", "")),
                    "persona": str(script.get("persona", "")),
                }
            )

        for cell_index, cell in enumerate(script.get("speech_cells", []), start=1):
            cell_value = str(cell)
            normalized_cell = normalize_duplicate_text(cell_value)
            if len(normalized_cell) < 16:
                continue
            speech_cell_members.setdefault(normalized_cell, []).append(
                {
                    "script_index": script_index,
                    "cell_index": cell_index,
                    "title": str(script.get("title", "")),
                    "persona": str(script.get("persona", "")),
                }
            )

    full_groups = []
    for normalized, members in full_script_members.items():
        if len(members) < 2:
            continue
        full_groups.append(
            {
                "count": len(members),
                "character_count": len(normalized),
                "unique_persona_count": len({item["persona"] for item in members}),
                "members": members,
            }
        )
    full_groups.sort(key=lambda item: (-int(item["count"]), -int(item["character_count"])))

    cell_groups = []
    for normalized, members in speech_cell_members.items():
        if len(members) < 2:
            continue
        cell_groups.append(
            {
                "count": len(members),
                "text": normalized,
                "unique_persona_count": len({item["persona"] for item in members}),
                "members": members,
            }
        )
    cell_groups.sort(key=lambda item: (-int(item["count"]), -len(str(item["text"]))))

    return {
        "exact_duplicate_script_group_count": len(full_groups),
        "exact_duplicate_script_excess_count": sum(
            int(group["count"]) - 1 for group in full_groups
        ),
        "exact_duplicate_script_groups": full_groups[:RISK_EXAMPLE_LIMIT],
        "repeated_speech_cell_group_count": len(cell_groups),
        "repeated_speech_cell_excess_count": sum(
            int(group["count"]) - 1 for group in cell_groups
        ),
        "repeated_speech_cell_groups": cell_groups[:RISK_EXAMPLE_LIMIT],
    }


def audit(scripts: list[dict[str, object]]) -> dict[str, object]:
    totals: Counter[str] = Counter()
    scripts_with: Counter[str] = Counter()
    endings = Counter()
    ending_examples: list[dict[str, str]] = []
    blank_final_slot_examples: list[dict[str, object]] = []
    ending_modes: Counter[str] = Counter()
    ending_leads: Counter[str] = Counter()
    ending_tail_counts: Counter[str] = Counter()
    ending_tail_examples: list[dict[str, object]] = []
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
        ending_modes[ending_mode(final_cell)] += 1
        lead = ending_lead(final_cell)
        if lead:
            ending_leads[lead] += 1
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
        tail_flags = ending_tail_flags(final_cell)
        for tail_flag in tail_flags:
            ending_tail_counts[tail_flag] += 1
        if tail_flags and len(ending_tail_examples) < RISK_EXAMPLE_LIMIT:
            speech_cells = [str(value) for value in script["speech_cells"]]
            ending_tail_examples.append(
                {
                    "title": str(script["title"]),
                    "previous_speech_cell": speech_cells[-2]
                    if len(speech_cells) > 1
                    else "",
                    "ending": final_cell,
                    "flags": tail_flags,
                }
            )
        flags = [f"tail:{tail_flag}" for tail_flag in tail_flags]
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
    voice_counts = Counter(voices)
    dominant_voice, dominant_voice_count = (
        voice_counts.most_common(1)[0] if voice_counts else ("", 0)
    )
    duplicate_report = duplicate_script_report(scripts)
    dominant_ending_mode, dominant_ending_mode_count = (
        ending_modes.most_common(1)[0] if ending_modes else ("", 0)
    )
    repeated_ending_leads = [
        {"lead": lead, "count": count}
        for lead, count in ending_leads.most_common()
        if count > 1
    ]
    return {
        "script_count": len(scripts),
        "script_character_count": sum(len(str(item["speech"])) for item in scripts),
        "persona_count": len(personas),
        "unique_persona_count": len(set(personas)),
        "voice_counts": voice_counts,
        "voice_stats": {
            "script_count": len(scripts),
            "voice_instruction_count": len(voices),
            "missing_voice_instruction_count": len(scripts) - len(voices),
            "unique_voice_instruction_count": len(voice_counts),
            "dominant_voice_instruction": dominant_voice,
            "dominant_voice_instruction_count": dominant_voice_count,
            "dominant_voice_instruction_share": round(
                dominant_voice_count / len(voices), 4
            )
            if voices
            else 0,
        },
        "metadata_stats": metadata_report(scripts),
        "duplicate_stats": duplicate_report,
        "pattern_totals": totals,
        "scripts_with_pattern": scripts_with,
        "risk_examples": risk_examples,
        "ending_counts": endings,
        "ending_style_stats": {
            "ending_mode_counts": ending_modes,
            "dominant_ending_mode": dominant_ending_mode,
            "dominant_ending_mode_count": dominant_ending_mode_count,
            "dominant_ending_mode_share": round(
                dominant_ending_mode_count / len(scripts), 4
            )
            if scripts
            else 0,
            "unique_ending_lead_count": len(ending_leads),
            "repeated_ending_lead_group_count": len(repeated_ending_leads),
            "repeated_ending_lead_examples": repeated_ending_leads[
                :RISK_EXAMPLE_LIMIT
            ],
            "ending_tail_risk_counts": ending_tail_counts,
            "ending_tail_risk_examples": ending_tail_examples,
        },
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
