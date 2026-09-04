#!/usr/bin/env python3
"""Refresh public GitHub metadata for the curated WorkBuddy ecosystem."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPOSITORIES = ROOT / "data" / "ecosystem-repos.txt"
OUTPUT = ROOT / "ECOSYSTEM.md"


def parse_repositories(text: str) -> list[str]:
    repositories = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.startswith("#")
    ]
    normalized = [repository.casefold() for repository in repositories]
    if len(normalized) != len(set(normalized)):
        duplicates = sorted(
            repository
            for repository in set(normalized)
            if normalized.count(repository) > 1
        )
        raise ValueError(f"duplicate ecosystem repositories: {', '.join(duplicates)}")
    return repositories


def repositories() -> list[str]:
    return parse_repositories(REPOSITORIES.read_text(encoding="utf-8"))


def fetch(repository: str) -> dict[str, object]:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-workbuddy-ecosystem-updater",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def render(items: list[dict[str, object]], updated: str) -> str:
    rows = []
    for item in sorted(items, key=lambda value: int(value["stargazers_count"]), reverse=True):
        name = str(item["full_name"])
        url = str(item["html_url"])
        stars = int(item["stargazers_count"])
        pushed = str(item["pushed_at"])[:10]
        language = str(item.get("language") or "-").replace("|", "\\|")
        rows.append(f"| [{name}]({url}) | {stars:,} | {language} | {pushed} |")

    return "\n".join(
        [
            "# WorkBuddy Open-source Ecosystem",
            "",
            "> GitHub metadata for repositories curated in `data/ecosystem-repos.txt`.",
            "> Inclusion is not an endorsement. Review source code, licenses, permissions, and account terms before use.",
            "",
            f"Last refreshed: **{updated} UTC**",
            "",
            "| Repository | Stars | Language | Last push |",
            "| --- | ---: | --- | --- |",
            *rows,
            "",
            "Want to add a project? Read [CONTRIBUTING.md](CONTRIBUTING.md) and open a pull request.",
            "",
        ]
    )


def main() -> int:
    items = []
    for repository in repositories():
        try:
            items.append(fetch(repository))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            print(f"Failed to fetch {repository}: {error}", file=sys.stderr)
            return 1

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    OUTPUT.write_text(render(items, updated), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
