import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import build_site_data  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
