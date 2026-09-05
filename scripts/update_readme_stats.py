#!/usr/bin/env python3
"""Update the bounded repository snapshot in the bilingual READMEs."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- REPOSITORY-SNAPSHOT:START -->"
END = "<!-- REPOSITORY-SNAPSHOT:END -->"


def count_curated(root: Path) -> int:
    lines = (root / "data" / "ecosystem-repos.txt").read_text(encoding="utf-8").splitlines()
    return sum(1 for line in lines if line.strip() and not line.startswith("#"))


def count_skills(root: Path) -> int:
    return sum(1 for path in (root / "skills").glob("*/SKILL.md") if path.is_file())


def count_candidates(root: Path) -> int:
    lines = (root / "DISCOVERIES.md").read_text(encoding="utf-8").splitlines()
    return sum(1 for line in lines if line.startswith("| ["))


def snapshot(root: Path) -> str:
    return (
        f"**{count_curated(root)} curated repositories · "
        f"{count_skills(root)} original Skills · "
        f"{count_candidates(root)} discovery candidates · weekly validation**"
    )


def replace_snapshot(readme: str, value: str) -> str:
    pattern = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)
    replacement = f"{START}\n{value}\n{END}"
    updated, count = pattern.subn(replacement, readme)
    if count != 1:
        raise ValueError(f"expected exactly one repository snapshot marker, found {count}")
    return updated


def main() -> None:
    value = snapshot(ROOT)
    for filename in ("README.md", "README.en.md"):
        readme_path = ROOT / filename
        readme = readme_path.read_text(encoding="utf-8")
        readme_path.write_text(replace_snapshot(readme, value), encoding="utf-8")


if __name__ == "__main__":
    main()
