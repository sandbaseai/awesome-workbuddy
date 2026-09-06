#!/usr/bin/env python3
"""Build a review queue of active GitHub repositories related to WorkBuddy."""

from __future__ import annotations

import html
import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "data" / "ecosystem-repos.txt"
OUTPUT = ROOT / "DISCOVERIES.md"
REPOSITORY_ROW = re.compile(r"^\| \[([^]]+)]\(https://github\.com/[^)]+\) \|")
SEARCH_QUERIES = (
    "workbuddy in:name,description",
    "codebuddy in:name,description",
    "topic:workbuddy",
    "topic:workbuddy-skill",
    "topic:workbuddy-skills",
)


def curated_repositories() -> set[str]:
    return {
        line.strip().casefold()
        for line in CURATED.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def listed_repositories(text: str) -> set[str]:
    return {
        match.group(1).casefold()
        for line in text.splitlines()
        if (match := REPOSITORY_ROW.match(line))
    }


def fetch_candidates() -> list[dict[str, object]]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=180)).date().isoformat()
    token = os.environ.get("GITHUB_TOKEN")
    repositories: dict[str, dict[str, object]] = {}
    for base_query in SEARCH_QUERIES:
        # Keep name/description matches focused; topic queries add projects
        # whose WorkBuddy support is documented through repository metadata.
        query = f"{base_query} stars:>=10 pushed:>={cutoff}"
        params = urllib.parse.urlencode(
            {"q": query, "sort": "stars", "order": "desc", "per_page": 100}
        )
        request = urllib.request.Request(
            f"https://api.github.com/search/repositories?{params}",
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "awesome-workbuddy-discovery",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        if token:
            request.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(request, timeout=30) as response:
            for item in json.load(response)["items"]:
                repositories[str(item["full_name"]).casefold()] = item
    return sorted(
        repositories.values(),
        key=lambda item: int(item["stargazers_count"]),
        reverse=True,
    )


def clean(value: object) -> str:
    text = " ".join(str(value or "-").split())
    return html.escape(text, quote=False).replace("|", "\\|")


def license_label(license_info: object) -> str:
    """Return a review-oriented label for GitHub's license metadata."""
    if not isinstance(license_info, dict) or not license_info:
        return "Not declared"
    spdx_id = str(license_info.get("spdx_id") or "").strip()
    if not spdx_id or spdx_id.upper() == "NOASSERTION":
        return "Non-standard / unrecognized"
    return spdx_id


def render(items: list[dict[str, object]], updated: str) -> str:
    curated = curated_repositories()
    candidates = [
        item
        for item in items
        if str(item["full_name"]).casefold() not in curated
        and not item["archived"]
        and not item["fork"]
    ][:40]

    rows = [
        "# WorkBuddy Discovery Queue",
        "",
        "> Automatically discovered GitHub repositories that are **not yet vetted or endorsed**.",
        "> Check relevance, source, license, permissions, and account terms before moving any entry into the curated list.",
        "",
        f"Last refreshed: **{updated} UTC**",
        "",
        "| Repository | Stars | Last push | License | Description |",
        "| --- | ---: | --- | --- | --- |",
    ]
    for item in candidates:
        name = clean(item["full_name"])
        url = item["html_url"]
        stars = int(item["stargazers_count"])
        pushed = str(item["pushed_at"])[:10]
        license_name = clean(license_label(item.get("license")))
        description = clean(item.get("description"))
        rows.append(f"| [{name}]({url}) | {stars:,} | {pushed} | {license_name} | {description} |")
    rows.extend(
        [
            "",
            "To curate a candidate, verify it and add `owner/repository` to `data/ecosystem-repos.txt` plus the most precise README category.",
            "",
        ]
    )
    return "\n".join(rows)


def main() -> None:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    OUTPUT.write_text(render(fetch_candidates(), updated), encoding="utf-8")


if __name__ == "__main__":
    main()
