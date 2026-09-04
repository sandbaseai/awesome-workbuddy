# Evidence Standards

Use this reference when a brief needs a defensible evidence trail rather than a short factual answer.

## Source assessment

Evaluate a source against the claim being made:

| Dimension | Strong signal | Warning signal |
| --- | --- | --- |
| Authority | Regulator, standards body, original dataset, official documentation, or named expert in scope | Anonymous aggregation or unclear ownership |
| Proximity | Direct measurement, filing, specification, or first-party record | Several layers of quotation or summary |
| Currency | Dated and current enough for the claim's rate of change | Undated page or obsolete version |
| Method | Definitions, sample, collection method, and limitations are visible | Headline number without methodology |
| Independence | Evidence was produced separately from the claim being evaluated | Affiliate, sponsor, copied press release, or circular citation |

A source can be authoritative for one claim and weak for another. A vendor's documentation is strong for its published API syntax, but its marketing page is not independent evidence of comparative superiority.

## Evidence record

For each consequential claim, retain enough information to reconstruct it:

```text
Claim:
Status: sourced fact | calculation | inference | unknown
Source title:
Publisher or author:
Published or updated:
Accessed:
Direct URL:
Relevant scope or definition:
Limitation or conflict:
```

The final answer may compress these fields into citations or a table. Do not omit a material limitation merely to keep the presentation short.

## Conflict procedure

When two credible sources disagree:

1. restate both claims using the same units where conversion is valid;
2. compare the period, population, geography, product tier, and definitions;
3. trace whether one source depends on the other;
4. prefer the source with closer authority, clearer method, and better temporal fit;
5. preserve the unresolved range when the evidence cannot support one value.

### Example

A vendor pricing page says a plan costs $20 per user per month, while a current reseller page says $18. Do not report $19.

- The vendor page is primary for list price.
- The reseller figure may be a regional, annual, promotional, or outdated price.
- Report the vendor's dated list price and separately describe the reseller offer with its conditions.
- If billing period, taxes, or region cannot be reconciled, mark the comparison unresolved.

## Calculation checks

- Record every input with its source and unit.
- Normalize currencies, periods, and denominators before comparing.
- State exchange-rate date and provider when converting currency.
- Keep appropriate precision; do not manufacture confidence with extra decimals.
- Recompute totals independently when they drive the recommendation.

## Confidence language

Use confidence labels only when they add decision value:

- **High:** current primary evidence directly supports the conclusion and material conflicts are resolved.
- **Moderate:** evidence is credible but one meaningful limitation or inference remains.
- **Low:** sources are indirect, stale, sparse, or materially conflicting.

Confidence describes the evidence for the conclusion, not writing fluency or personal certainty.
