#!/usr/bin/env python3
"""Validate the behavior-regression corpus and optionally check a candidate output."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ALLOWED_SCOPES = {"L1", "L2", "L3", "L4"}
REQUIRED_FIELDS = {
    "id",
    "title",
    "task_type",
    "genre",
    "scope",
    "request",
    "source",
    "required_routes",
    "must_preserve",
    "must_remove",
    "forbidden_additions",
    "behavior_checks",
}
REQUIRED_GENRES = {
    "client_deck",
    "client_proposal",
    "creative_ideation",
    "executive_report",
    "fiction",
    "internal_sop",
    "marketing_strategy",
    "ugc_script",
    "whitepaper_case",
}


def load_corpus(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_corpus(payload: dict[str, Any], skill_root: Path) -> list[str]:
    errors: list[str] = []
    cases = payload.get("cases")
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(cases, list):
        return errors + ["cases must be a list"]
    if not 20 <= len(cases) <= 30:
        errors.append(f"expected 20-30 cases, found {len(cases)}")

    ids: list[str] = []
    genres: set[str] = set()
    scopes: set[str] = set()
    route_counts: Counter[str] = Counter()

    for index, case in enumerate(cases):
        prefix = f"case[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED_FIELDS - set(case)
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(sorted(missing))}")
            continue

        case_id = str(case["id"])
        ids.append(case_id)
        prefix = case_id
        scope = str(case["scope"])
        genre = str(case["genre"])
        scopes.add(scope)
        genres.add(genre)
        if scope not in ALLOWED_SCOPES:
            errors.append(f"{prefix}: unsupported scope {scope}")

        source = str(case["source"])
        for field in ("required_routes", "must_preserve", "must_remove", "forbidden_additions", "behavior_checks"):
            value = case[field]
            if not isinstance(value, list):
                errors.append(f"{prefix}: {field} must be a list")

        for literal in case["must_preserve"]:
            if literal not in source:
                errors.append(f"{prefix}: must_preserve literal not found in source: {literal}")
        for literal in case["must_remove"]:
            if literal not in source:
                errors.append(f"{prefix}: must_remove literal not found in source: {literal}")

        overlap = set(case["must_preserve"]) & set(case["must_remove"])
        if overlap:
            errors.append(f"{prefix}: preserve/remove overlap: {sorted(overlap)}")

        for route in case["required_routes"]:
            route_counts[str(route)] += 1
            route_path = skill_root / "references" / str(route)
            if not route_path.is_file():
                errors.append(f"{prefix}: missing route file references/{route}")

    duplicates = [case_id for case_id, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate ids: {', '.join(sorted(duplicates))}")
    if scopes != ALLOWED_SCOPES:
        errors.append(f"scope coverage must be L1-L4, found {sorted(scopes)}")
    missing_genres = REQUIRED_GENRES - genres
    if missing_genres:
        errors.append(f"missing required genres: {', '.join(sorted(missing_genres))}")
    if len(genres) < 12:
        errors.append(f"expected at least 12 genres, found {len(genres)}")
    if not route_counts:
        errors.append("no reference routes declared")
    return errors


def check_output(case: dict[str, Any], output: str) -> list[str]:
    errors: list[str] = []
    for literal in case["must_preserve"]:
        if literal not in output:
            errors.append(f"missing required literal: {literal}")
    for literal in case["must_remove"]:
        if literal in output:
            errors.append(f"residual rejected literal: {literal}")
    for literal in case["forbidden_additions"]:
        if literal in output:
            errors.append(f"forbidden addition present: {literal}")
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate debug-aiwriting behavior cases.")
    parser.add_argument(
        "corpus",
        nargs="?",
        type=Path,
        default=Path("evals/behavior_cases.json"),
    )
    parser.add_argument("--skill-root", type=Path, default=Path("."))
    parser.add_argument("--case", dest="case_id")
    parser.add_argument("--output", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    payload = load_corpus(args.corpus)
    errors = validate_corpus(payload, args.skill_root)

    if args.case_id or args.output:
        if not args.case_id or not args.output:
            errors.append("--case and --output must be used together")
        else:
            selected = next(
                (case for case in payload["cases"] if case["id"] == args.case_id),
                None,
            )
            if selected is None:
                errors.append(f"unknown case id: {args.case_id}")
            elif not args.output.is_file():
                errors.append(f"missing output file: {args.output}")
            else:
                errors.extend(
                    check_output(selected, args.output.read_text(encoding="utf-8"))
                )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(
        f"Behavior corpus valid: {len(payload['cases'])} cases, "
        f"{len({case['genre'] for case in payload['cases']})} genres."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
