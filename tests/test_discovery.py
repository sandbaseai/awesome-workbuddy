import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import discover_repos  # noqa: E402
import update_ecosystem  # noqa: E402


class DiscoveryTests(unittest.TestCase):
    def test_clean_escapes_table_markup_and_html(self) -> None:
        self.assertEqual(discover_repos.clean("a | <b>\n c"), "a \\| &lt;b&gt; c")

    def test_render_excludes_curated_archived_and_forked_repositories(self) -> None:
        items = [
            {
                "full_name": "AlephAITech/WorkBuddyGuide",
                "html_url": "https://github.com/AlephAITech/WorkBuddyGuide",
                "stargazers_count": 100,
                "pushed_at": "2026-09-01T00:00:00Z",
                "description": "curated",
                "archived": False,
                "fork": False,
            },
            {
                "full_name": "example/archived",
                "html_url": "https://github.com/example/archived",
                "stargazers_count": 90,
                "pushed_at": "2026-09-01T00:00:00Z",
                "description": "archived",
                "archived": True,
                "fork": False,
            },
            {
                "full_name": "example/candidate",
                "html_url": "https://github.com/example/candidate",
                "stargazers_count": 80,
                "pushed_at": "2026-09-01T00:00:00Z",
                "description": "new | useful",
                "archived": False,
                "fork": False,
            },
        ]
        output = discover_repos.render(items, "2026-09-04")
        self.assertNotIn("WorkBuddyGuide", output)
        self.assertNotIn("example/archived", output)
        self.assertIn("[example/candidate]", output)
        self.assertIn("new \\| useful", output)


class EcosystemTests(unittest.TestCase):
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
