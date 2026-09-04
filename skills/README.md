# Original Skills

These small, auditable Skills are maintained with this list. They are examples of the selection and security standards described in the repository, not official Tencent Skills.

## Install

Download the latest [document-quality-review.zip](https://github.com/sandbaseai/awesome-workbuddy/releases/latest/download/document-quality-review.zip), or copy the complete Skill directory from the repository. Place it in the user-level or project-level Skills directory shown by your current WorkBuddy version. Keep `SKILL.md` and its referenced resources together. The official UI also provides an import action; consult the current [WorkBuddy Skill documentation](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) before installation.

Review every file first. Test with non-sensitive copies and limited permissions before using a Skill in real work.

## Included

- [document-quality-review](document-quality-review/SKILL.md) - Reviews evidence, calculations, consistency, completeness, links, rendered layout, sensitive data, and operational usability before a deliverable is sent.

## Validate

Run the repository-level structural validator against a Skill directory:

```shell
python scripts/validate_skill.py skills/document-quality-review
```

The validator catches malformed or missing frontmatter, invalid names, weak descriptions, unfinished placeholders, broken local Markdown references, and obvious embedded secrets. Passing it is not Tencent certification and does not prove that instructions or code are safe.

Release `v0.1.0` archive SHA-256: `ffe5a22e23c9c037e7e798a157385e30c3659ea0923f7df982aea3668a36f890`.
