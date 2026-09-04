---
name: document-quality-review
description: Review Markdown, Word, PDF, spreadsheet, or presentation deliverables for factual support, internal consistency, completeness, usability, and visible quality before delivery.
---

# Document Quality Review

Review the deliverable and its available source material without changing the original files. Identify issues that would prevent a reader from trusting, understanding, or using the result.

## Review

1. Establish the intended audience, purpose, required format, and acceptance criteria from the request and nearby project files. Do not invent requirements that are not supported by the available context.
2. Inspect the final rendered form when layout matters. Source text alone cannot establish that a Word document, PDF, spreadsheet, or presentation renders correctly.
3. Trace important claims, numbers, quotations, and conclusions to the supplied sources. Mark unsupported claims as unverified rather than filling gaps from memory.
4. Check calculations, units, dates, names, links, terminology, headings, cross-references, and repeated values for consistency.
5. Apply the relevant sections of the [review checklist](references/review-checklist.md). Skip sections that do not apply instead of producing empty boilerplate.
6. Report issues in descending severity. For each issue include its location, observed evidence, impact, and a concrete correction. Distinguish confirmed defects from questions or missing evidence.

## Output

Start with one of these verdicts:

- **Ready**: no material issue blocks delivery.
- **Ready with minor fixes**: only low-impact corrections remain.
- **Not ready**: at least one issue could mislead the reader, break use, or violate an explicit requirement.

Then provide a compact table with `Severity`, `Location`, `Finding`, `Evidence`, and `Suggested fix`. End with the checks performed and any checks that could not be completed.

Do not silently edit, publish, send, delete, or overwrite files. If the user asks for corrections, preserve the original unless they explicitly authorize replacement.
