#!/usr/bin/env python3
"""Inventory document surfaces and flag residual Chinese writing risks.

Supports Markdown, plain text, XML/HTML, DOCX, and PPTX. Findings are a coverage
backstop, not proof that wording is wrong in its scene or genre.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable
from xml.etree import ElementTree


DEFAULT_PATTERN_FILE = (
    Path(__file__).resolve().parents[1] / "references" / "trace-patterns.json"
)


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


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def element_text(element: ElementTree.Element) -> str:
    parts: list[str] = []
    for item in element.iter():
        name = local_name(item.tag)
        if name == "t" and item.text:
            parts.append(item.text)
        elif name == "tab":
            parts.append("\t")
        elif name in {"br", "cr"}:
            parts.append("\n")
    return normalize_space("".join(parts))


def parent_map(root: ElementTree.Element) -> dict[ElementTree.Element, ElementTree.Element]:
    return {child: parent for parent in root.iter() for child in parent}


def has_ancestor(
    element: ElementTree.Element,
    parents: dict[ElementTree.Element, ElementTree.Element],
    names: set[str],
) -> bool:
    current = parents.get(element)
    while current is not None:
        if local_name(current.tag) in names:
            return True
        current = parents.get(current)
    return False


def first_descendant(
    element: ElementTree.Element, name: str
) -> ElementTree.Element | None:
    return next((item for item in element.iter() if local_name(item.tag) == name), None)


def attr_by_local_name(element: ElementTree.Element, name: str) -> str | None:
    for key, value in element.attrib.items():
        if local_name(key) == name:
            return value
    return None


def natural_part_key(name: str) -> tuple[object, ...]:
    return tuple(int(part) if part.isdigit() else part for part in re.split(r"(\d+)", name))


def read_xml_part(archive: zipfile.ZipFile, name: str) -> ElementTree.Element:
    try:
        return ElementTree.fromstring(archive.read(name))
    except (KeyError, ElementTree.ParseError) as error:
        raise ValueError(f"Cannot parse OOXML part {name}: {error}") from error


def word_paragraph_kind(
    paragraph: ElementTree.Element,
    parents: dict[ElementTree.Element, ElementTree.Element],
    part_name: str,
) -> str:
    if has_ancestor(paragraph, parents, {"tc"}):
        return "table_cell"
    if "footnote" in part_name or "endnote" in part_name:
        return "footnote"
    if "comment" in part_name:
        return "comment"
    if "header" in part_name:
        return "header"
    if "footer" in part_name:
        return "footer"

    properties = first_descendant(paragraph, "pPr")
    style = first_descendant(properties, "pStyle") if properties is not None else None
    style_value = attr_by_local_name(style, "val") if style is not None else None
    normalized_style = (style_value or "").lower()
    if normalized_style.startswith("heading") or normalized_style.startswith("标题"):
        return "heading"
    if normalized_style in {"caption", "题注"}:
        return "caption"
    return "body"


def parse_docx(path: Path) -> list[Surface]:
    surfaces: list[Surface] = []
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile as error:
        raise ValueError(f"Invalid DOCX archive: {path}") from error

    with archive:
        part_names = [
            name
            for name in archive.namelist()
            if re.fullmatch(
                r"word/(?:document|header\d+|footer\d+|footnotes|endnotes|comments)\.xml",
                name,
            )
        ]
        if "word/document.xml" not in part_names:
            raise ValueError(f"DOCX is missing word/document.xml: {path}")

        for part_name in sorted(part_names, key=natural_part_key):
            root = read_xml_part(archive, part_name)
            parents = parent_map(root)
            paragraph_index = 0
            for element in root.iter():
                if local_name(element.tag) != "p":
                    continue
                text = element_text(element)
                if not text:
                    continue
                paragraph_index += 1
                surfaces.append(
                    Surface(
                        word_paragraph_kind(element, parents, part_name),
                        f"{part_name}:p:{paragraph_index}",
                        text,
                    )
                )

            alt_index = 0
            for element in root.iter():
                if local_name(element.tag) not in {"docPr", "cNvPr"}:
                    continue
                alt = element.attrib.get("descr") or element.attrib.get("title")
                if alt and normalize_space(alt):
                    alt_index += 1
                    surfaces.append(
                        Surface(
                            "caption",
                            f"{part_name}:alt:{alt_index}",
                            normalize_space(alt),
                        )
                    )
    return surfaces


def presentation_paragraph_kind(
    paragraph: ElementTree.Element,
    parents: dict[ElementTree.Element, ElementTree.Element],
    part_name: str,
) -> str:
    if has_ancestor(paragraph, parents, {"tc"}):
        return "table_cell"
    if "/notesSlides/" in part_name:
        return "note"

    current = parents.get(paragraph)
    while current is not None:
        if local_name(current.tag) in {"sp", "graphicFrame"}:
            placeholder = first_descendant(current, "ph")
            placeholder_type = (
                attr_by_local_name(placeholder, "type") if placeholder is not None else None
            )
            if placeholder_type in {"title", "ctrTitle"}:
                return "heading"
            break
        current = parents.get(current)
    return "body"


def parse_pptx(path: Path) -> list[Surface]:
    surfaces: list[Surface] = []
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile as error:
        raise ValueError(f"Invalid PPTX archive: {path}") from error

    with archive:
        slide_parts = [
            name
            for name in archive.namelist()
            if re.fullmatch(r"ppt/(?:slides/slide\d+|notesSlides/notesSlide\d+)\.xml", name)
        ]
        if not any(name.startswith("ppt/slides/") for name in slide_parts):
            raise ValueError(f"PPTX has no slide XML: {path}")

        for part_name in sorted(slide_parts, key=natural_part_key):
            root = read_xml_part(archive, part_name)
            parents = parent_map(root)
            paragraph_index = 0
            for element in root.iter():
                if local_name(element.tag) != "p":
                    continue
                text = element_text(element)
                if not text:
                    continue
                paragraph_index += 1
                surfaces.append(
                    Surface(
                        presentation_paragraph_kind(element, parents, part_name),
                        f"{part_name}:p:{paragraph_index}",
                        text,
                    )
                )

            alt_index = 0
            for element in root.iter():
                if local_name(element.tag) != "cNvPr":
                    continue
                alt = element.attrib.get("descr") or element.attrib.get("title")
                if alt and normalize_space(alt):
                    alt_index += 1
                    surfaces.append(
                        Surface(
                            "caption",
                            f"{part_name}:alt:{alt_index}",
                            normalize_space(alt),
                        )
                    )

        chart_parts = sorted(
            (
                name
                for name in archive.namelist()
                if re.fullmatch(r"ppt/charts/chart\d+\.xml", name)
            ),
            key=natural_part_key,
        )
        for part_name in chart_parts:
            root = read_xml_part(archive, part_name)
            value_index = 0
            for element in root.iter():
                if local_name(element.tag) not in {"t", "v"} or not element.text:
                    continue
                text = normalize_space(element.text)
                if not text:
                    continue
                value_index += 1
                surfaces.append(
                    Surface("chart_text", f"{part_name}:value:{value_index}", text)
                )
    return surfaces


def extract_surfaces(path: Path, text: str) -> list[Surface]:
    suffix = path.suffix.lower()
    if suffix in {".md", ".markdown"}:
        return parse_markdown(text)
    if suffix in {".xml", ".html", ".htm", ".xhtml"}:
        return parse_markup(text)
    return parse_plain(text)


def extract_path_surfaces(path: Path) -> list[Surface]:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return parse_docx(path)
    if suffix == ".pptx":
        return parse_pptx(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    return extract_surfaces(path, text)


def normalized_duplicate_key(text: str) -> str:
    text = re.sub(r"[\s，。；：、,.!?！？:;()（）\[\]【】\"'“”‘’]+", "", text)
    return text.lower()


def load_pattern_catalog(path: Path = DEFAULT_PATTERN_FILE) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError(f"Unsupported pattern schema in {path}")
    if not isinstance(payload.get("categories"), dict):
        raise ValueError(f"Missing pattern categories in {path}")
    if not isinstance(payload.get("term_drift_groups"), dict):
        raise ValueError(f"Missing term drift groups in {path}")
    return payload


def find_hits(
    surfaces: Iterable[Surface],
    custom_terms: list[str],
    catalog: dict[str, Any],
) -> list[dict[str, str]]:
    categories = catalog["categories"]
    term_drift_groups = catalog["term_drift_groups"]

    hits: list[dict[str, str]] = []
    for surface in surfaces:
        for category, spec in categories.items():
            severity = str(spec.get("severity", "medium"))
            for term in spec.get("terms", []):
                if term and term in surface.text:
                    hits.append(
                        {
                            "category": category,
                            "severity": severity,
                            "pattern": term,
                            "surface_kind": surface.kind,
                            "location": surface.location,
                            "text": surface.text,
                        }
                    )
            for regex_spec in spec.get("regex", []):
                regex = re.compile(str(regex_spec["pattern"]))
                label = str(regex_spec["label"])
                if regex.search(surface.text):
                    hits.append(
                        {
                            "category": category,
                            "severity": severity,
                            "pattern": label,
                            "surface_kind": surface.kind,
                            "location": surface.location,
                            "text": surface.text,
                        }
                    )
        for term in custom_terms:
            if term and term in surface.text:
                hits.append(
                    {
                        "category": "user_hard_negative",
                        "severity": "high",
                        "pattern": term,
                        "surface_kind": surface.kind,
                        "location": surface.location,
                        "text": surface.text,
                    }
                )
        for group_name, terms in term_drift_groups.items():
            matched_terms = [term for term in terms if term in surface.text]
            if len(matched_terms) >= 3:
                hits.append(
                    {
                        "category": "term_drift_review",
                        "severity": "low",
                        "pattern": f"{group_name}: {'/'.join(matched_terms)}",
                        "surface_kind": surface.kind,
                        "location": surface.location,
                        "text": surface.text,
                    }
                )
    return hits


def audit(
    path: Path,
    custom_terms: list[str],
    pattern_path: Path = DEFAULT_PATTERN_FILE,
) -> dict[str, object]:
    surfaces = extract_path_surfaces(path)
    catalog = load_pattern_catalog(pattern_path)
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
        "pattern_catalog": str(pattern_path.resolve()),
        "high_risk_hits": find_hits(surfaces, custom_terms, catalog),
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
    parser.add_argument(
        "--patterns",
        type=Path,
        default=DEFAULT_PATTERN_FILE,
        help="Machine-readable pattern catalog.",
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

    try:
        results = [audit(path, args.term, args.patterns) for path in args.paths]
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Pattern catalog error: {error}", file=sys.stderr)
        return 2
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
