from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CommunityHealthTests(unittest.TestCase):
    def test_community_entry_points_are_linked(self) -> None:
        for filename in ("README.md", "README.en.md"):
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn(
                "https://github.com/sandbaseai/awesome-workbuddy/discussions",
                content,
            )
            self.assertIn("CODE_OF_CONDUCT.md", content)

    def test_code_of_conduct_has_reporting_path(self) -> None:
        content = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
        self.assertIn("## Reporting", content)
        self.assertIn("https://support.github.com/", content)
        self.assertNotIn("[INSERT", content)

    def test_contribution_entry_points_are_bilingual(self) -> None:
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("Thank you for improving Awesome WorkBuddy", contributing)
        self.assertIn("Report a broken or unsafe link", contributing)
        for filename in ("resource.yml", "broken-link.yml"):
            content = (ROOT / ".github" / "ISSUE_TEMPLATE" / filename).read_text(encoding="utf-8")
            self.assertIn("/", content)
            self.assertIn("description:", content)
