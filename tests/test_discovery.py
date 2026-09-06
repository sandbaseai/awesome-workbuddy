import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import discover_repos  # noqa: E402
import update_ecosystem  # noqa: E402


class DiscoveryTests(unittest.TestCase):
    def test_search_queries_include_workbuddy_topics(self) -> None:
        self.assertIn("topic:workbuddy", discover_repos.SEARCH_QUERIES)
        self.assertIn("topic:workbuddy-skill", discover_repos.SEARCH_QUERIES)
        self.assertIn("topic:workbuddy-skills", discover_repos.SEARCH_QUERIES)

    def test_checked_in_queue_excludes_curated_repositories(self) -> None:
        root = Path(__file__).resolve().parents[1]
        discoveries = discover_repos.listed_repositories(
            (root / "DISCOVERIES.md").read_text(encoding="utf-8")
        )
        self.assertTrue(discoveries.isdisjoint(discover_repos.curated_repositories()))

    def test_listed_repositories_parses_rows_case_insensitively(self) -> None:
        text = "| [Owner/Project](https://github.com/Owner/Project) | 1 |\n"
        self.assertEqual(discover_repos.listed_repositories(text), {"owner/project"})

    def test_clean_escapes_table_markup_and_html(self) -> None:
        self.assertEqual(discover_repos.clean("a | <b>\n c"), "a \\| &lt;b&gt; c")

    def test_license_label_distinguishes_missing_custom_and_spdx(self) -> None:
        self.assertEqual(discover_repos.license_label(None), "Not declared")
        self.assertEqual(
            discover_repos.license_label(
                {"spdx_id": "NOASSERTION", "name": "Other"}
            ),
            "Non-standard / unrecognized",
        )
        self.assertEqual(
            discover_repos.license_label({"spdx_id": None, "name": "Custom"}),
            "Non-standard / unrecognized",
        )
        self.assertEqual(
            discover_repos.license_label(
                {"spdx_id": "Apache-2.0", "name": "Apache License 2.0"}
            ),
            "Apache-2.0",
        )

    def test_render_excludes_curated_archived_and_forked_repositories(self) -> None:
        items = [
            {
                "full_name": "AlephAITech/WorkBuddyGuide",
                "html_url": "https://github.com/AlephAITech/WorkBuddyGuide",
                "stargazers_count": 100,
                "pushed_at": "2026-09-01T00:00:00Z",
                "description": "curated",
                "license": {"spdx_id": "MIT", "name": "MIT License"},
                "archived": False,
                "fork": False,
            },
            {
                "full_name": "example/archived",
                "html_url": "https://github.com/example/archived",
                "stargazers_count": 90,
                "pushed_at": "2026-09-01T00:00:00Z",
                "description": "archived",
                "license": None,
                "archived": True,
                "fork": False,
            },
            {
                "full_name": "example/candidate",
                "html_url": "https://github.com/example/candidate",
                "stargazers_count": 80,
                "pushed_at": "2026-09-01T00:00:00Z",
                "description": "new | useful",
                "license": None,
                "archived": False,
                "fork": False,
            },
        ]
        output = discover_repos.render(items, "2026-09-04")
        self.assertNotIn("WorkBuddyGuide", output)
        self.assertNotIn("example/archived", output)
        self.assertIn("[example/candidate]", output)
        self.assertIn("new \\| useful", output)
        self.assertIn("Not declared", output)
        self.assertIn("| License |", output)


class EcosystemTests(unittest.TestCase):
    def test_checked_in_ecosystem_contains_every_source(self) -> None:
        root = Path(__file__).resolve().parents[1]
        ecosystem = (root / "ECOSYSTEM.md").read_text(encoding="utf-8")
        for repository in update_ecosystem.repositories():
            with self.subTest(repository=repository):
                self.assertIn(f"[{repository}]", ecosystem)

    def test_repository_source_rejects_case_insensitive_duplicates(self) -> None:
        with self.assertRaisesRegex(ValueError, "example/project"):
            update_ecosystem.parse_repositories(
                "# curated\nExample/Project\nexample/project\n"
            )

    def test_repository_source_ignores_comments_and_blank_lines(self) -> None:
        self.assertEqual(
            update_ecosystem.parse_repositories("# curated\n\nexample/project\n"),
            ["example/project"],
        )

    def test_render_orders_repositories_by_stars(self) -> None:
        items = [
            {
                "full_name": "example/smaller",
                "html_url": "https://github.com/example/smaller",
                "stargazers_count": 2,
                "pushed_at": "2026-09-01T00:00:00Z",
                "language": None,
            },
            {
                "full_name": "example/larger",
                "html_url": "https://github.com/example/larger",
                "stargazers_count": 10,
                "pushed_at": "2026-09-02T00:00:00Z",
                "language": "Python",
            },
        ]
        output = update_ecosystem.render(items, "2026-09-04")
        self.assertLess(output.index("example/larger"), output.index("example/smaller"))


if __name__ == "__main__":
    unittest.main()
