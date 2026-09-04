import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import update_readme_stats  # noqa: E402


class UpdateReadmeStatsTests(unittest.TestCase):
    def test_counts_authoritative_repository_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "data").mkdir()
            (root / "data" / "ecosystem-repos.txt").write_text(
                "# curated\nowner/one\n\nowner/two\n", encoding="utf-8"
            )
            (root / "skills" / "one").mkdir(parents=True)
            (root / "skills" / "one" / "SKILL.md").write_text("skill\n", encoding="utf-8")
            (root / "skills" / "notes").mkdir()
            (root / "DISCOVERIES.md").write_text(
                "| Repository | Stars |\n| --- | ---: |\n| [a/b](https://example.com) | 1 |\n",
                encoding="utf-8",
            )
            self.assertEqual(
                update_readme_stats.snapshot(root),
                "**2 curated repositories · 1 original Skills · 1 discovery candidates · weekly validation**",
            )

    def test_replaces_only_the_bounded_snapshot(self) -> None:
        original = "before\n<!-- REPOSITORY-SNAPSHOT:START -->\nold\n<!-- REPOSITORY-SNAPSHOT:END -->\nafter\n"
        updated = update_readme_stats.replace_snapshot(original, "new")
        self.assertEqual(
            updated,
            "before\n<!-- REPOSITORY-SNAPSHOT:START -->\nnew\n<!-- REPOSITORY-SNAPSHOT:END -->\nafter\n",
        )

    def test_requires_exactly_one_marker(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly one"):
            update_readme_stats.replace_snapshot("no marker", "new")


if __name__ == "__main__":
    unittest.main()
