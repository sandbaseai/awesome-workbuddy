# Original Skills

These small, auditable Skills are maintained with this list. They are examples of the selection and security standards described in the repository, not official Tencent Skills.

## Install

Download a packaged Skill from the [latest release](https://github.com/sandbaseai/awesome-workbuddy/releases/latest), or copy a complete Skill directory from the repository. Place it in the user-level or project-level Skills directory shown by your current WorkBuddy version. Keep `SKILL.md` and its referenced resources together. The official UI also provides an import action; consult the current [WorkBuddy Skill documentation](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) before installation.

Review every file first. Test with non-sensitive copies and limited permissions before using a Skill in real work.

## Included

- [document-quality-review](document-quality-review/SKILL.md) - Reviews evidence, calculations, consistency, completeness, links, rendered layout, sensitive data, and operational usability before a deliverable is sent.
- [skill-security-audit](skill-security-audit/SKILL.md) - Performs a read-only, evidence-backed review of instructions, code, dependencies, permissions, credentials, data flow, and irreversible actions before installing an Agent extension.
- [source-backed-research-brief](source-backed-research-brief/SKILL.md) - Produces a decision-ready research brief with current sources, explicit uncertainty, reproducible calculations, and separated facts and inference.
- [curate-workbuddy-resource](curate-workbuddy-resource/SKILL.md) - Reviews a candidate resource and returns a traceable include, hold, or exclude decision across direct relevance, distinct value, maintenance, licensing, provenance, permissions, and data flow.

## Validate

Run the repository-level structural validator against a Skill directory:

```shell
python scripts/validate_skill.py skills/document-quality-review
python scripts/validate_skill.py skills/skill-security-audit
python scripts/validate_skill.py skills/source-backed-research-brief
python scripts/validate_skill.py skills/curate-workbuddy-resource
```

The validator catches malformed or missing frontmatter, invalid names, weak descriptions, unfinished placeholders, broken local Markdown references, and obvious embedded secrets. Passing it is not Tencent certification and does not prove that instructions or code are safe.

Release `v0.6.0` archive SHA-256 digests:

- `curate-workbuddy-resource.zip`: `eea6349db6f55077812299648e3789dd01ec1a2103e03340e4c1bfdaebe87d9a`
- `document-quality-review.zip`: `57e3080b4734de2f56ee6913ec421d81a21766f042e77c386369b40c1816262f`
- `skill-security-audit.zip`: `1a600060d7f282351d30682e20842f408c6d219b3f3faeb81423bf9e1d5dc54f`
- `source-backed-research-brief.zip`: `5006fc337872eee9b1a3b85941b483ed483987c821a3db29d525c27519714c5d`
