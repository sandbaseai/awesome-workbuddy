# WorkBuddy Resource Review Rubric

Use this rubric as evidence prompts, not a points system. A severe failure can
block inclusion even when every other signal is positive.

## Scope gate

- What exact file, page, screenshot, package metadata, or reproducible behavior
  shows direct support for, documentation of, or evaluation of Tencent WorkBuddy?
- Is “WorkBuddy” only a keyword, analogy, generated tag, or unrelated product name?
- Is the proposed category more precise than a broad “tools” or “resources” label?

## Access and identity

- Resolve redirects and prefer the canonical HTTPS URL without tracking fields.
- Confirm the resource is publicly accessible without joining a group, scanning
  a QR code, or providing personal details.
- Record the maintainer/publisher, disclosed commercial relationship, archive or
  fork status, and whether the description matches the actual contents.

## Distinct value and quality

- Identify the concrete task, audience, and deliverable.
- Check that instructions are usable, claims are specific, and examples or tests
  support the promised behavior.
- Compare against existing entries. Name the distinct value rather than calling
  something “comprehensive,” “best,” or “official” without evidence.
- Reject pure promotion, copied aggregation without provenance, and thin pages
  that add no verifiable information.

## Maintenance

- Record the last meaningful content or code update, not merely an automated
  metadata refresh.
- Inspect unresolved breakage, archived status, stale product paths, abandoned
  dependencies, and whether the documented WorkBuddy version is clear.
- Verify changing product facts against a current official source and label
  version-specific guidance.

## License and provenance

- Record the SPDX license when one is declared and read any scope exceptions.
- Trace copied Skills, prompts, templates, screenshots, datasets, binaries, and
  bundled dependencies to their sources and applicable terms.
- “Publicly downloadable” is not equivalent to permission to redistribute.
- For no-license material, browsing and linking may still be possible, but do not
  describe it as open source or recommend copying/repackaging it.

## Safety and permissions

For executable resources, inspect:

- installation and update commands, including remote scripts and package hooks;
- file reads/writes, deletion, persistence, shell execution, and privilege use;
- network hosts, telemetry, uploads, downloads, and dynamic code loading;
- API keys, OAuth scopes, cookies, tokens, local databases, logs, and whether
  output can reveal secrets or personal/company information;
- external actions such as posting, messaging, trading, publishing, or changing
  accounts, plus confirmation and rollback behavior;
- pinned dependencies, checksums, signatures, tests, and uninstall instructions.

For documents, check unsafe commands, unofficial download links, credential
requests, unsupported legal/medical/financial claims, and instructions that
conflict with current product or account terms.

## Evidence record

Capture a compact record:

| Field | Required evidence |
| --- | --- |
| Canonical resource | Direct URL and owner/publisher |
| WorkBuddy relevance | Specific supporting file or primary page |
| Type and audience | What it is and who it helps |
| Distinct value | Comparison with the closest existing entry |
| Maintenance | Last meaningful update and version context |
| License/provenance | License scope and origins of bundled material |
| Permissions/data flow | Files, credentials, network, and external actions |
| Blocking concerns | Evidence, impact, and possible resolution |
| Disposition | Include, hold, or exclude with confidence |

If a field is not applicable, say why. If evidence is unavailable, mark it
unknown rather than filling it from assumptions.
