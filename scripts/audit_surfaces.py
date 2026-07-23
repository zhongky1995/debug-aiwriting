#!/usr/bin/env python3
"""Inventory text surfaces and flag residual high-risk Chinese writing patterns.

This is a coverage backstop for Markdown, plain text, XML, and HTML sources. It
does not decide whether a phrase is wrong in context; the writing agent must
still apply the selected scene register and evidence rules.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


RISK_PATTERNS = {
    "abstract_action": [
        "赋能增长",
        "激活心智",
        "撬动势能",
        "沉淀资产",
        "释放价值",
        "构建闭环",
        "完成转化前置",
        "实现心智占位",
        "完成用户教育",
        "实现转化闭环",
    ],
    "unnatural_collocation": [
        "重新接回",
        "接住用户关系",
        "接住经营动作",
        "内容完成用户教育",
        "场景释放产品价值",
        "打通触点",
        "打通复购",
        "沉淀用户",
        "沉淀方法论",
        "激活关系",
        "撬动复购",
        "拉动心智",
        "进入沟通节奏",
        "沉淀回访名单",
        "搭建内容承接",
    ],
    "template_scaffold": [
        "首先，",
        "其次，",
        "最后，",
        "综上所述",
        "总的来说",
        "值得注意的是",
        "我们不难发现",
        "这背后其实是",
    ],
    "inflated_significance": [
        "标志着重要转变",
        "成为时代缩影",
        "彰显其深远意义",
        "反映更广泛趋势",
        "奠定坚实基础",
        "不可磨灭的印记",
        "不断演变的格局",
    ],
    "vague_attribution": [
        "行业报告显示",
        "有研究表明",
        "专家认为",
        "业内人士指出",
        "观察者指出",
        "相关数据显示",
        "多项研究显示",
    ],
    "tail_pseudo_analysis": [
        "从而确保",
        "进而推动",
        "进一步彰显",
        "这也体现了",
        "这也意味着",
        "有效促进",
    ],
    "generic_outlook": [
        "挑战与未来展望",
        "未来依然可期",
        "这只是一个开始",
        "迈出了坚实一步",
        "释放更大价值",
    ],
    "collaboration_residue": [
        "当然可以",
        "希望这对你有帮助",
        "希望这对您有帮助",
        "如果你需要，我还可以",
        "如果您需要，我还可以",
        "请告诉我是否需要调整",
        "你说得完全正确",
        "您说得完全正确",
    ],
    "model_disclaimer": [
        "根据我最后的训练数据",
        "截至我的知识更新时间",
        "基于现有有限信息",
    ],
}

RISK_REGEX_PATTERNS = {
    "copula_avoidance": [
        (
            re.compile(
                r"(?:作为|充当)[^，。；！？\n]{0,20}"
                r"(?:载体|空间|平台|抓手|证明|体现|象征)"
            ),
            "作为/充当……载体、空间、平台或证明",
        ),
        (
            re.compile(r"拥有[^，。；！？\n]{0,16}(?:能力|可能性)"),
            "拥有……能力/可能性",
        ),
    ],
    "formatting_trace": [
        (
            re.compile(r"^(?:[-*+]\s+)?\*\*[^*]{1,24}[：:]\*\*"),
            "粗体小标题加冒号",
        ),
        (
            re.compile(r"(?:—[^—\n]*){2,}"),
            "单个文本面内重复使用破折号",
        ),
        (
            re.compile(r"[🚀✅💡🔥🎯📌📍✨🌟⚡]"),
            "装饰性表情符号",
        ),
    ],
}

TERM_DRIFT_GROUPS = {
    "项目称谓": ["项目", "计划", "方案", "机制", "体系"],
    "用户称谓": ["用户", "消费者", "客群", "人群", "受众"],
    "组织称谓": ["公司", "企业", "品牌", "组织"],
}


@dataclass(frozen=True)
class Surface:
    kind: str
    location: str
    text: str


class MarkupSurfaceParser(HTMLParser):
    TAG_KIND = {
        "title": "title",
        "h1": "heading",
        "h2": "heading",
        "h3": "heading",
        "h4": "heading",
        "h5": "heading",
        "h6": "heading",
        "th": "table_cell",
        "td": "table_cell",
        "caption": "caption",
        "figcaption": "caption",
        "li": "list_item",
        "blockquote": "body",
        "p": "body",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.surfaces: list[Surface] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag.lower())

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "img":
            alt = dict(attrs).get("alt")
            if alt and alt.strip():
                line, _ = self.getpos()
                self.surfaces.append(Surface("caption", f"line:{line}", alt.strip()))

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self.stack:
            reverse_index = self.stack[::-1].index(tag)
            del self.stack[len(self.stack) - reverse_index - 1 :]

    def handle_data(self, data: str) -> None:
        text = normalize_space(data)
        if not text or not self.stack:
            return
        tag = next((item for item in reversed(self.stack) if item in self.TAG_KIND), None)
        if not tag:
            return
        line, _ = self.getpos()
        self.surfaces.append(Surface(self.TAG_KIND[tag], f"line:{line}", text))


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_markdown(text: str) -> list[Surface]:
    surfaces: list[Surface] = []
    in_fence = False
    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            surfaces.append(Surface("heading", f"line:{number}", heading.group(2).strip()))
            continue

        for alt in re.findall(r"!\[([^\]]*)\]\([^)]*\)", stripped):
            if alt.strip():
                surfaces.append(Surface("caption", f"line:{number}", alt.strip()))

        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [normalize_space(cell) for cell in stripped.strip("|").split("|")]
            if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            for index, cell in enumerate(cells, start=1):
                if cell:
                    surfaces.append(
                        Surface("table_cell", f"line:{number}:cell:{index}", cell)
                    )
            continue

        if re.match(r"^\[\^[^\]]+\]:", stripped):
            surfaces.append(Surface("footnote", f"line:{number}", stripped))
        elif re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", stripped):
            surfaces.append(Surface("list_item", f"line:{number}", stripped))
        elif re.match(r"^(?:图|表)\s*\d*[:：]", stripped):
            surfaces.append(Surface("caption", f"line:{number}", stripped))
        else:
            surfaces.append(Surface("body", f"line:{number}", stripped))
    return surfaces


def parse_markup(text: str) -> list[Surface]:
    parser = MarkupSurfaceParser()
    try:
        parser.feed(text)
        parser.close()
    except Exception:
        return parse_plain(text)
    return parser.surfaces or parse_plain(re.sub(r"<[^>]+>", " ", text))


def parse_plain(text: str) -> list[Surface]:
    return [
        Surface("body", f"line:{number}", normalize_space(raw))
        for number, raw in enumerate(text.splitlines(), start=1)
        if normalize_space(raw)
    ]


def extract_surfaces(path: Path, text: str) -> list[Surface]:
    suffix = path.suffix.lower()
    if suffix in {".md", ".markdown"}:
        return parse_markdown(text)
    if suffix in {".xml", ".html", ".htm", ".xhtml"}:
        return parse_markup(text)
    return parse_plain(text)


def normalized_duplicate_key(text: str) -> str:
    text = re.sub(r"[\s，。；：、,.!?！？:;()（）\[\]【】\"'“”‘’]+", "", text)
    return text.lower()


def find_hits(surfaces: Iterable[Surface], custom_terms: list[str]) -> list[dict[str, str]]:
    patterns = {**RISK_PATTERNS}
    if custom_terms:
        patterns["user_hard_negative"] = custom_terms

    hits: list[dict[str, str]] = []
    for surface in surfaces:
        for category, terms in patterns.items():
            for term in terms:
                if term and term in surface.text:
                    hits.append(
                        {
                            "category": category,
                            "pattern": term,
                            "surface_kind": surface.kind,
                            "location": surface.location,
                            "text": surface.text,
                        }
                    )
        for category, regex_patterns in RISK_REGEX_PATTERNS.items():
            for regex, label in regex_patterns:
                if regex.search(surface.text):
                    hits.append(
                        {
                            "category": category,
                            "pattern": label,
                            "surface_kind": surface.kind,
                            "location": surface.location,
                            "text": surface.text,
                        }
                    )
        for group_name, terms in TERM_DRIFT_GROUPS.items():
            matched_terms = [term for term in terms if term in surface.text]
            if len(matched_terms) >= 3:
                hits.append(
                    {
                        "category": "term_drift_review",
                        "pattern": f"{group_name}: {'/'.join(matched_terms)}",
                        "surface_kind": surface.kind,
                        "location": surface.location,
                        "text": surface.text,
                    }
                )
    return hits


def audit(path: Path, custom_terms: list[str]) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace")
    surfaces = extract_surfaces(path, text)
    counts = Counter(surface.kind for surface in surfaces)

    duplicate_groups: dict[str, list[Surface]] = {}
    for surface in surfaces:
        key = normalized_duplicate_key(surface.text)
        if len(key) >= 12:
            duplicate_groups.setdefault(key, []).append(surface)

    repeated = []
    for group in duplicate_groups.values():
        if len(group) < 2:
            continue
        repeated.append(
            {
                "count": len(group),
                "text": group[0].text,
                "locations": [item.location for item in group[:10]],
            }
        )
    repeated.sort(key=lambda item: (-int(item["count"]), str(item["text"])))

    return {
        "file": str(path.resolve()),
        "format": path.suffix.lower().lstrip(".") or "plain",
        "surface_counts": dict(sorted(counts.items())),
        "total_surfaces": len(surfaces),
        "high_risk_hits": find_hits(surfaces, custom_terms),
        "repeated_surfaces": repeated[:20],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inventory writing surfaces and flag high-risk Chinese wording."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--term",
        action="append",
        default=[],
        help="User-rejected phrase to scan as a hard negative; repeat as needed.",
    )
    parser.add_argument("--output", type=Path, help="Write JSON to this file.")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    missing = [str(path) for path in args.paths if not path.is_file()]
    if missing:
        print(f"Missing input file(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    results = [audit(path, args.term) for path in args.paths]
    payload: object = results[0] if len(results) == 1 else results
    rendered = json.dumps(
        payload,
        ensure_ascii=False,
        indent=None if args.compact else 2,
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
