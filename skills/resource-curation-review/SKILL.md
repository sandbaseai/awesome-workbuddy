---
name: resource-curation-review
description: Review a WorkBuddy resource submission and produce an evidence-backed include, hold, or exclude decision covering relevance, value, maintenance, provenance, permissions, credentials, and data flow without installing or submitting anything.
---

# Resource Curation Review

Assess a candidate repository, document, Skill, MCP integration, workflow, or guide for inclusion in a curated WorkBuddy directory. The default review is read-only: inspect public material, but do not install dependencies, execute candidate code, sign in, provide credentials, submit external content, or open a pull request on the candidate's behalf.

## Review workflow

1. Identify the exact candidate URL and, when possible, revision or release. Record the review date and the files or pages inspected.
2. Gather primary evidence from the candidate's README, manifest, license, release metadata, and directly invoked scripts. Treat claims not supported by inspected evidence as unverified.
3. Apply the [review rubric](references/review-rubric.md). Cover direct WorkBuddy relevance, distinct user value, maintenance signals, license and provenance, permissions, credentials, data sources and destinations, network behavior, and irreversible actions.
4. Classify the result as **include**, **hold**, or **exclude**. An include decision still needs a concise usage or safety note when permissions, account access, external services, or personal data are involved.
5. Write a compact evidence record: identity, scope, decision, findings with file paths or URLs, unanswered questions, and the smallest safe next step. Keep the candidate outside the current repository until a separately authorized curation change is made.

## Decision rules

- **Include** only when relevance and distinct value are evidenced, provenance is clear enough to cite, and material permissions or data flows are disclosed with a proportionate warning.
- **Hold** when the project may be useful but revision, license, maintenance, executable behavior, or data flow remains too unclear to recommend.
- **Exclude** when it is unrelated, duplicative without additional value, inaccessible, clearly unsafe for the intended directory, or incompatible with the directory's scope.
- Do not treat stars, recent commits, a clean README, or a declared license as proof of safe runtime behavior.
- Do not call a project official, safe, malicious, compliant, or endorsed without evidence sufficient for that claim.

## Output

Begin with the candidate identity and one verdict: **include**, **hold**, or **exclude**. Then provide:

1. Scope and limitations.
2. Evidence summary for relevance, value, maintenance, and provenance.
3. Capability and permission findings, including credential and data-flow paths.
4. Confirmed findings and unanswered questions, ordered by impact.
5. Recommended directory wording or the smallest safe follow-up.

Use precise locations—file paths, line ranges, manifest fields, commands, release URLs, or documentation links—for material claims. Separate observed behavior from inference. Never copy secrets, tokens, private data, or unredacted diagnostic output into the report.
