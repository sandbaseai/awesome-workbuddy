import unittest
from pathlib import Path


class AuditTemplateTests(unittest.TestCase):
    def test_discovery_audit_template_preserves_issue_format(self) -> None:
        root = Path(__file__).resolve().parents[1]
        template = (root / ".github/ISSUE_TEMPLATE/discovery-audit.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("\nCandidate\n\n- Repository:", template)
        self.assertIn("\n## Audit result\n\n", template)
        self.assertIn("\n## Decision\n\n", template)
        self.assertIn(
            "state the concrete evidence needed for the next decision. --> This issue is an audit record, not an endorsement.",
            template,
        )
        self.assertNotIn("## Candidate", template)
        self.assertNotIn("\\\\n", template)
