#!/usr/bin/env python3
"""Validate the basic structure and hygiene of a SKILL.md package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|FIXME|REPLACE_ME)\b", re.IGNORECASE)
PRIVATE_KEY_PATTERN = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
ASSIGNMENT_SECRET_PATTERN = re.compile(
    r"(?i)\b(?:api[_-]?key|access[_-]?token|secret|password)\b\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{16,}"
)


def scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip("\"'")


def validate(skill_directory: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_directory / "SKILL.md"
    if not skill_file.is_file():
        return ["missing required SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return ["SKILL.md must begin with YAML frontmatter delimited by ---"]

    frontmatter = match.group(1)
    name = scalar(frontmatter, "name")
    description = scalar(frontmatter, "description")
    if not name:
        errors.append("frontmatter is missing name")
    elif not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        errors.append("name must use lowercase letters, digits, and single hyphens, with at most 64 characters")
    elif name != skill_directory.name:
        errors.append(f"name {name!r} must match directory {skill_directory.name!r}")

    if not description:
        errors.append("frontmatter is missing description")
    elif len(description) < 40:
        errors.append("description is too short to explain what the Skill does and when it applies")

    if PLACEHOLDER_PATTERN.search(text):
        errors.append("SKILL.md contains an unfinished placeholder")

    for target in LINK_PATTERN.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        relative_target = target.split("#", 1)[0]
        if not relative_target:
            continue
        resolved_target = (skill_directory / relative_target).resolve()
        if not resolved_target.is_relative_to(skill_directory.resolve()):
            errors.append(f"reference escapes Skill directory: {relative_target}")
        elif not resolved_target.is_file():
            errors.append(f"missing referenced file: {relative_target}")

    for path in skill_directory.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".sh"}:
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        if PRIVATE_KEY_PATTERN.search(content) or ASSIGNMENT_SECRET_PATTERN.search(content):
            errors.append(f"possible embedded secret in {path.relative_to(skill_directory)}")

    return errors


def main(arguments: list[str]) -> int:
    if len(arguments) != 1:
        print("usage: validate_skill.py PATH_TO_SKILL", file=sys.stderr)
        return 2
    skill_directory = Path(arguments[0]).resolve()
    errors = validate(skill_directory)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {skill_directory}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
