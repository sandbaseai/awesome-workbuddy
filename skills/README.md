# Original Skills

These small, auditable Skills are maintained with this list. They are examples of the selection and security standards described in the repository, not official Tencent Skills.

## Install

Download [document-quality-review.zip](https://github.com/sandbaseai/awesome-workbuddy/releases/latest/download/document-quality-review.zip) or [skill-security-audit.zip](https://github.com/sandbaseai/awesome-workbuddy/releases/latest/download/skill-security-audit.zip), or copy a complete Skill directory from the repository. Place it in the user-level or project-level Skills directory shown by your current WorkBuddy version. Keep `SKILL.md` and its referenced resources together. The official UI also provides an import action; consult the current [WorkBuddy Skill documentation](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) before installation.

Review every file first. Test with non-sensitive copies and limited permissions before using a Skill in real work.

## Included

- [document-quality-review](document-quality-review/SKILL.md) - Reviews evidence, calculations, consistency, completeness, links, rendered layout, sensitive data, and operational usability before a deliverable is sent.
- [skill-security-audit](skill-security-audit/SKILL.md) - Performs a read-only, evidence-backed review of instructions, code, dependencies, permissions, credentials, data flow, and irreversible actions before installing an Agent extension.

## Validate

Run the repository-level structural validator against a Skill directory:

```shell
python scripts/validate_skill.py skills/document-quality-review
python scripts/validate_skill.py skills/skill-security-audit
```

The validator catches malformed or missing frontmatter, invalid names, weak descriptions, unfinished placeholders, broken local Markdown references, and obvious embedded secrets. Passing it is not Tencent certification and does not prove that instructions or code are safe.

Release `v0.3.1` archive SHA-256 digests:

- `document-quality-review.zip`: `4341833ac859b5ccf3d5f23d5da399ee61fb51aa2882485e826ab5a5ca9a99fd`
- `skill-security-audit.zip`: `11ee0269db855b781cf2b2c4364a9501f0236f9bbb3e2e8ce9c478e323eb9bf2`
