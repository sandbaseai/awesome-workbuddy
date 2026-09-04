import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import validate_skill  # noqa: E402


class ValidateSkillTests(unittest.TestCase):
    def make_skill(self, root: Path, name: str, content: str) -> Path:
        directory = root / name
        directory.mkdir()
        (directory / "SKILL.md").write_text(content, encoding="utf-8")
        return directory

    def test_accepts_a_well_formed_skill_with_existing_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill = self.make_skill(
                root,
                "sample-review",
                """---
name: sample-review
description: Review sample deliverables when evidence and consistency must be checked before delivery.
---

# Sample Review

Read the [checklist](references/checklist.md), then report evidence.
""",
            )
            (skill / "references").mkdir()
            (skill / "references" / "checklist.md").write_text("# Checklist\n", encoding="utf-8")
            self.assertEqual(validate_skill.validate(skill), [])

    def test_rejects_mismatched_name_placeholder_missing_reference_and_secret(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill = self.make_skill(
                root,
                "sample-review",
                """---
name: different_name
description: short
---

TODO: Read the [missing checklist](references/missing.md).
api_key = "abcdefghijklmnop1234"
""",
            )
            errors = validate_skill.validate(skill)
            self.assertTrue(any("name must" in error for error in errors))
            self.assertTrue(any("description is too short" in error for error in errors))
            self.assertTrue(any("placeholder" in error for error in errors))
            self.assertTrue(any("missing referenced file" in error for error in errors))
            self.assertTrue(any("embedded secret" in error for error in errors))

    def test_rejects_missing_skill_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            self.assertEqual(
                validate_skill.validate(Path(temporary)),
                ["missing required SKILL.md"],
            )

    def test_rejects_reference_outside_the_skill_package(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "outside.md").write_text("private context\n", encoding="utf-8")
            skill = self.make_skill(
                root,
                "sample-review",
                """---
name: sample-review
description: Review sample deliverables when evidence and consistency must be checked before delivery.
---

Read the [outside file](../outside.md).
""",
            )
            self.assertTrue(
                any("escapes Skill directory" in error for error in validate_skill.validate(skill))
            )


if __name__ == "__main__":
    unittest.main()
