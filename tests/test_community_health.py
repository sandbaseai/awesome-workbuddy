from pathlib import Path
from xml.etree import ElementTree
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CommunityHealthTests(unittest.TestCase):
    def test_public_feed_is_valid_and_has_recent_updates(self) -> None:
        feed = ElementTree.parse(ROOT / "site" / "feed.xml")
        channel = feed.getroot().find("channel")
        self.assertIsNotNone(channel)
        items = channel.findall("item") if channel is not None else []
        self.assertGreaterEqual(len(items), 2)
        self.assertTrue(all(item.findtext("link", "").startswith("https://") for item in items))

    def test_llms_entry_points_are_current(self) -> None:
        content = (ROOT / "site" / "llms.txt").read_text(encoding="utf-8")
        for url in (
            "https://sandbaseai.github.io/awesome-workbuddy/",
            "https://sandbaseai.github.io/awesome-workbuddy/resources.json",
            "https://sandbaseai.github.io/awesome-workbuddy/feed.xml",
            "https://github.com/sandbaseai/awesome-workbuddy/issues/775",
        ):
            self.assertIn(url, content)
        self.assertNotIn("selection standards", content)

    def test_public_readmes_focus_on_resource_content(self) -> None:
        for filename in ("README.md", "README.en.md"):
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("START_HERE.md", content)
            self.assertNotIn("100 genuine stars", content)
            self.assertNotIn("100 个真实 Star", content)
            self.assertNotIn("Selection Standard", content)
            self.assertNotIn("Contributing", content)

    def test_code_of_conduct_has_reporting_path(self) -> None:
        content = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
        self.assertIn("## Reporting", content)
        self.assertIn("https://support.github.com/", content)
        self.assertNotIn("[INSERT", content)

    def test_citation_metadata_is_complete_and_linked(self) -> None:
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        for field in (
            "cff-version: 1.2.0",
            "type: software",
            'title: "Awesome WorkBuddy"',
            "authors:",
            'repository-code: "https://github.com/sandbaseai/awesome-workbuddy"',
            'license: CC0-1.0',
            "version: 0.10.30",
            "date-released: 2026-09-05",
        ):
            self.assertIn(field, citation)
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

        resource_form = (
            ROOT / ".github" / "ISSUE_TEMPLATE" / "resource.yml"
        ).read_text(encoding="utf-8")
        for field_id in (
            "resource_type",
            "license",
            "provenance",
            "permissions",
            "reviewed_at",
        ):
            self.assertIn(f"id: {field_id}", resource_form)
        self.assertIn("not declared", resource_form)
        self.assertIn("YYYY-MM-DD", resource_form)

    def test_ecosystem_refresh_is_scheduled_and_manual(self) -> None:
        workflow = (
            ROOT / ".github" / "workflows" / "update-ecosystem.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("schedule:", workflow)
        self.assertIn('cron: "31 3 * * 1"', workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("  push:", workflow)
        self.assertIn("scripts/update_ecosystem.py", workflow)
        self.assertIn("scripts/discover_repos.py", workflow)
        self.assertIn("group: update-ecosystem-main", workflow)
        self.assertIn("cancel-in-progress: true", workflow)
        self.assertIn("git pull --ff-only origin main", workflow)
        self.assertIn("for attempt in 1 2 3; do", workflow)
        self.assertIn("git rebase origin/main", workflow)

    def test_pages_workflow_uses_node24_actions(self) -> None:
        workflow = (
            ROOT / ".github" / "workflows" / "pages.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("actions/configure-pages@v6", workflow)
        self.assertIn("actions/upload-pages-artifact@v5", workflow)
        self.assertIn("actions/deploy-pages@v5", workflow)

    def test_pages_has_search_discovery_files(self) -> None:
        robots = (ROOT / "site" / "robots.txt").read_text(encoding="utf-8")
        sitemap = (ROOT / "site" / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("Sitemap: https://sandbaseai.github.io/awesome-workbuddy/sitemap.xml", robots)
        self.assertIn("https://sandbaseai.github.io/awesome-workbuddy/", sitemap)
