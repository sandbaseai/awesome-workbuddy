---
name: source-backed-research-brief
description: Produce a concise, decision-ready research brief with traceable sources, explicit uncertainty, and separated facts, calculations, and inference. Use for product, market, policy, vendor, or technical-choice questions when evidence quality and freshness matter; do not use as a substitute for qualified legal, medical, or financial advice.
---

# Source-backed Research Brief

Turn a clear research question into a compact brief that a reader can audit. Preserve the user's scope, audience, decision deadline, geography, and budget; ask one focused clarification only when a missing constraint would change the conclusion.

## Workflow

1. Define the decision, evaluation criteria, time window, and what would count as sufficient evidence. Separate facts needed to answer the question from useful context.
2. Gather primary or authoritative sources first. For each source, record its exact title, publisher, publication date (or `not stated`), access date, URL, and the claim it supports. Prefer stable pages or documents over search-result snippets.
3. Extract claims before writing the recommendation. Tag each material statement as **Sourced fact**, **Calculation**, or **Analyst inference**. Never present an inference or an uncited recollection as a sourced fact.
4. Check freshness for time-sensitive claims such as prices, availability, policies, releases, rankings, and regulations. State the “as of” date and flag evidence that may have changed.
5. Compare sources on the same claim. If they disagree, show the disagreement, explain differences in scope/date/definition where the evidence supports that explanation, and avoid silently choosing the more convenient value.
6. Report evidence gaps, inaccessible sources, conflicting definitions, and assumptions. Lower confidence or give conditional options instead of inventing precision.
7. Write the brief using the output contract below. Keep supporting detail proportional to the decision; put the full source ledger after the conclusion.

Read [references/evidence-quality.md](references/evidence-quality.md) when assessing source strength, reconciling conflicts, or formatting the source ledger.

## Output contract

Use these sections unless the user requests another format:

1. **Decision question and scope** — one paragraph, including the evidence cutoff date.
2. **Bottom line** — a direct recommendation or conditional answer, with confidence (`High`, `Medium`, or `Low`) and its reason.
3. **Key findings** — concise bullets; label each as `Sourced fact`, `Calculation`, or `Analyst inference` and attach a source ID where applicable.
4. **Options and trade-offs** — compare only criteria relevant to the decision; show unknowns explicitly.
5. **Conflicts and caveats** — list unresolved disagreements, assumptions, freshness limits, and evidence gaps.
6. **Source ledger** — include every material source using the required fields from the reference.

Do not perform external publication, account mutation, purchases, sign-ins, or changes to third-party systems. Do not expose credentials or personal data in the brief. For high-stakes domains, make the need for qualified human review prominent.

## Example

**Question:** Which of two vendors should a 20-person team choose for a July 2026 launch, given a monthly budget of $500?

**Bottom line:** Choose Vendor A for the launch if the published team limit remains 25 seats; confidence **Medium**. Vendor A's official pricing page lists $18/user/month (Source S1), while an independent review lists $20/user/month (Source S2). The difference may reflect a date or plan definition that neither page fully explains, so confirm the quote before purchase.

- **Sourced fact [S1]:** Vendor A's pricing page lists the team plan at $18/user/month, accessed 2026-09-05.
- **Sourced fact [S2]:** Review B reports $20/user/month and was published 2026-06-14.
- **Calculation [S1]:** 20 × $18 = $360/month, leaving $140 under the stated budget; this excludes taxes and add-ons.
- **Analyst inference [S1, S2]:** Vendor A is the safer fit for the stated budget, but the conflicting prices prevent a high-confidence purchase recommendation.

The brief must not turn the conflict into “Vendor A costs $18” without preserving S2 and the unresolved explanation.
