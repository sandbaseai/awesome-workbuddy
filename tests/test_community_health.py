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

    def test_contribution_flow_is_bilingual(self) -> None:
        guide = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("## English", guide)
        self.assertIn("## 简体中文", guide)
        self.assertIn("SECURITY.md", guide)

        for filename in ("broken-link.yml", "resource.yml"):
            form = (
                ROOT / ".github" / "ISSUE_TEMPLATE" / filename
            ).read_text(encoding="utf-8")
            self.assertIn(" / ", form, filename)
            self.assertIn("Resource URL", form, filename)
