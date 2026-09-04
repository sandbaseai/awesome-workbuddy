import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://sandbaseai.github.io/awesome-workbuddy/"


class SiteMetadataTests(unittest.TestCase):
    def test_sitemap_contains_canonical_page(self) -> None:
        root = ET.parse(ROOT / "site" / "sitemap.xml").getroot()
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        self.assertEqual(
            [element.text for element in root.findall("sm:url/sm:loc", namespace)],
            [SITE_URL],
        )

    def test_robots_allows_crawling_and_points_to_sitemap(self) -> None:
        robots = (ROOT / "site" / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("User-agent: *\nAllow: /", robots)
        self.assertIn(f"Sitemap: {SITE_URL}sitemap.xml", robots)

    def test_page_has_matching_canonical_and_collection_schema(self) -> None:
        html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
        self.assertIn(f'<link rel="canonical" href="{SITE_URL}">', html)
        start = html.index('<script type="application/ld+json">')
        start = html.index("{", start)
        end = html.index("</script>", start)
        schema = json.loads(html[start:end])
        self.assertEqual(schema["@type"], "CollectionPage")
        self.assertEqual(schema["url"], SITE_URL)

    def test_page_has_persistent_bilingual_directory_state(self) -> None:
        html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="language"', html)
        self.assertIn("awesome-workbuddy-locale", html)
        self.assertIn("new URLSearchParams(location.search).get('lang')", html)
        self.assertIn("item.titleZh", html)
        self.assertIn('data-i18n="heroTitle"', html)

    def test_page_has_shareable_filter_state(self) -> None:
        html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="share"', html)
        self.assertIn("get('q')", html)
        self.assertIn("get('category')", html)
        self.assertIn("history.replaceState", html)
        self.assertIn("navigator.clipboard.writeText", html)
        self.assertIn("navigator.share", html)
        self.assertIn("shareCopied", html)


if __name__ == "__main__":
    unittest.main()
