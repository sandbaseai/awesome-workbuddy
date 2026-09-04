import json
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import build_site_data  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]


class BuildSiteDataTests(unittest.TestCase):
    def test_builds_bilingual_deduplicated_resources(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.en.md").write_text(
                "## Resources\n### Guides\n"
                "- [One](https://example.com/one) - English value.\n"
                "- [One again](https://example.com/one) - Duplicate.\n",
                encoding="utf-8",
            )
            (root / "README.md").write_text(
                "## 资源\n### 指南\n"
                "- [一](https://example.com/one) - 中文价值。\n",
                encoding="utf-8",
            )

            self.assertEqual(
                build_site_data.build(root),
                [
                    {
                        "title": "One",
                        "url": "https://example.com/one",
                        "description": "English value",
                        "section": "Resources",
                        "category": "Guides",
                        "titleZh": "一",
                        "descriptionZh": "中文价值。",
                        "categoryZh": "指南",
                    }
                ],
            )

    def test_parse_ignores_internal_and_unstructured_links(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            readme = Path(temporary) / "README.md"
            readme.write_text(
                "## Resources\n"
                "- [Internal](LOCAL.md) - Skip.\n"
                "- [No description](https://example.com)\n",
                encoding="utf-8",
            )
            self.assertEqual(build_site_data.parse_readme(readme), [])

    def test_curated_resource_urls_are_unique(self) -> None:
        for filename in ("README.md", "README.en.md"):
            resources = build_site_data.parse_readme(ROOT / filename)
            urls = [resource["url"] for resource in resources]
            self.assertEqual(len(urls), len(set(urls)), filename)

        resources = json.loads(
            (ROOT / "site" / "resources.json").read_text(encoding="utf-8")
        )
        urls = [resource["url"] for resource in resources]
        self.assertEqual(len(urls), len(set(urls)), "site/resources.json")


if __name__ == "__main__":
    unittest.main()
