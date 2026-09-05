import unittest
from pathlib import Path


class AuditTemplateTests(unittest.TestCase):
    def test_discovery_issue_workflow_applies_audit_label(self) -> None:
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/label-discovery-audits.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("types: [opened, edited, reopened]", workflow)
        self.assertIn("startsWith(github.event.issue.title, 'Discovery')", workflow)
        self.assertIn("issues: write", workflow)
        self.assertIn("--add-label audit", workflow)

    def test_discovery_audit_template_preserves_issue_format(self) -> None:
        root = Path(__file__).resolve().parents[1]
        template = (root / ".github/ISSUE_TEMPLATE/discovery-audit.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("\nCandidate\n\n- Repository:", template)
        self.assertTrue(template.startswith("---\n"))
        self.assertIn("\n\nCandidate\n\n- Repository:", template)
        self.assertLess(template.index("\nCandidate\n"), template.index("\n## Audit result\n"))
        self.assertLess(template.index("\n## Audit result\n"), template.index("\n## Decision\n"))
        self.assertIn("\n## Audit result\n\n", template)
        self.assertIn("\n## Decision\n\n", template)
        self.assertIn(
            "Hold, curate, or exclude; state the concrete evidence needed for the next decision. This issue is an audit record, not an endorsement.",
            template,
        )
        self.assertIn("https://github.com/owner/repository", template)
        self.assertIn("- Describe the published contents", template)

        contributing = (root / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("gh issue create --body-file", contributing)
        self.assertIn("literal `\\\\n`", contributing)
        self.assertNotIn("<!--", template)
        self.assertNotIn("-->", template)
        self.assertNotIn("## Candidate", template)
        self.assertNotIn("\\\\n", template)
