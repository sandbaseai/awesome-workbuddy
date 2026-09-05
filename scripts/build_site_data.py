#!/usr/bin/env python3
"""Build the bilingual data file used by the static resource directory."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"^- \[([^]]+)]\((https?://[^)]+)\) - (.+)$")


def parse_readme(path: Path) -> list[dict[str, str]]:
    section = ""
    category = ""
    resources: list[dict[str, str]] = []

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            category = section
            continue
        if line.startswith("### "):
            category = line[4:].strip()
            continue
        match = LINK.match(line)
        if not match:
            continue
        if section in {"精选资源", "Featured resources"}:
            continue
        title, url, description = match.groups()
        resources.append(
            {
                "title": title,
                "url": url,
                "description": description.rstrip("."),
                "section": section,
                "category": category,
            }
        )
    return resources


def build(root: Path) -> list[dict[str, str]]:
    english = parse_readme(root / "README.en.md")
    chinese = {item["url"]: item for item in parse_readme(root / "README.md")}
    result: list[dict[str, str]] = []
    seen: set[str] = set()

    for item in english:
        if item["url"] in seen:
            continue
        seen.add(item["url"])
        translated = chinese.get(item["url"], {})
        result.append(
            {
                **item,
                "titleZh": translated.get("title", ""),
                "descriptionZh": translated.get("description", ""),
                "categoryZh": translated.get("category", ""),
            }
        )
    return result


def main() -> None:
    output = ROOT / "site" / "resources.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(
        json.dumps(build(ROOT), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
