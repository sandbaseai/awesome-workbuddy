---
name: curate-workbuddy-resource
description: Review a public repository, document, Skill, MCP integration, workflow, or guide for a WorkBuddy resource directory and recommend include, hold, or exclude using traceable relevance, quality, maintenance, license, provenance, and safety evidence. Use when triaging or re-checking a candidate; not for installing or executing the candidate.
---

# Curate WorkBuddy Resource

Produce a decision another maintainer can verify without trusting the candidate's
marketing copy. Preserve the directory's stated scope and standards. Do not lower
the threshold because a project is popular, and do not reject a useful niche
resource only because it has few stars.

## Establish the candidate

Resolve the canonical public URL, owner, title, resource type, and relationship
to Tencent WorkBuddy. Distinguish the Tencent product from unrelated projects
that happen to use “workbuddy” as a name. If direct relevance cannot be shown
from accessible content, stop with **exclude — out of scope**.

Open the actual source and primary documentation. Search snippets, repository
descriptions, badges, and generated summaries are discovery clues, not sufficient
evidence. Record the review date because maintenance, pricing, compatibility,
terms, and permissions change.

## Review

Read [review-rubric.md](references/review-rubric.md) and apply every gate relevant
to the resource type. Inspect executable instructions and code in proportion to
their risk. For a Skill or integration, trace entrypoints, dependencies,
network destinations, file access, credentials, external mutations, and cleanup.
For a guide, verify a meaningful sample of its claims and links against current
primary sources.

Treat an absent or unclear license as a material reuse limitation, not proof that
the content is malicious. Separate the license covering the repository's own
code from licenses or rights applying to copied, archived, reverse-engineered,
or generated material.

Compare the candidate with existing entries by purpose and evidence, not title.
A duplicate may still qualify only when it adds a distinct audience, workflow,
implementation, or maintained source of truth.

Do not execute installers, sign in, expose credentials, accept terms, or grant
permissions merely to complete the review. Use non-sensitive test data only when
the user has separately authorized execution.

## Decide

Use exactly one disposition:

- **Include** — directly relevant, accessible, distinctly useful, and no
  unresolved blocking concern. State the narrowest category and any warning
  that must accompany the listing.
- **Hold** — promising, but a named fact or risk still needs evidence, access,
  maintenance, licensing clarification, or safer instructions. State what would
  resolve the hold.
- **Exclude** — out of scope, deceptive, harmful, inaccessible, substantially
  duplicative without added value, or blocked by a concrete safety/legal issue.
  State the evidence; do not speculate about intent.

A warning can disclose bounded risk, but it cannot cure malicious behavior,
credential theft, undisclosed destructive actions, or a license that does not
permit the proposed redistribution.

## Deliver

Lead with disposition and confidence, followed by:

1. canonical URL, type, license, last meaningful update, and review date;
2. direct WorkBuddy evidence and distinct value;
3. safety, permissions, provenance, and maintenance findings;
4. unresolved facts and the exact next check, if any;
5. a neutral one-sentence listing in the requested language when the result is
   **Include**, including the essential warning rather than hiding it elsewhere.

Link each consequential finding to the file or primary page that supports it.
Label inference and unknowns. Never claim that passing this review means Tencent
endorses, certifies, or guarantees the resource.

This Skill authorizes read-only research and a recommendation only. Do not add
the listing, open an Issue or Pull Request, contact maintainers, fork a project,
or publish the review unless the user separately requests that action.
