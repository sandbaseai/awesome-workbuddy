import re
import unittest
from pathlib import Path


GITHUB_BULLET = re.compile(r"^- \[[^]]+\]\(https://github\.com/([^/)]+/[^/)]+)")


class ResourceCatalogTests(unittest.TestCase):
    def test_bilingual_resource_bullets_have_unique_repositories(self) -> None:
        root = Path(__file__).resolve().parents[1]
        catalogs = {}
        for filename in ("RESOURCES.md", "RESOURCES.en.md"):
            repositories = []
            for line in (root / filename).read_text(encoding="utf-8").splitlines():
                match = GITHUB_BULLET.match(line)
                if match:
                    repositories.append(match.group(1).lower())
            catalogs[filename] = set(repositories)
            duplicates = sorted(
                repository
                for repository in set(repositories)
                if repositories.count(repository) > 1
            )
            self.assertEqual(duplicates, [], msg=f"duplicate entries in {filename}")
        self.assertEqual(catalogs["RESOURCES.md"], catalogs["RESOURCES.en.md"])


if __name__ == "__main__":
    unittest.main()
