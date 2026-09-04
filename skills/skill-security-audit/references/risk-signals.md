# Risk Signals and Severity Model

Risk depends on capability, exposure, control, and reversibility. Do not assign severity from a keyword alone.

## Critical

Use when confirmed behavior can directly compromise accounts or devices, or cause severe irreversible harm with little user control.

- Credential, private-key, session-cookie, wallet, or authentication-token theft or exfiltration.
- Hidden remote command execution, persistence, privilege escalation, or security-control bypass.
- Destructive action against broad or unresolved targets without a reliable confirmation boundary.
- Downloaded executable content whose integrity is unchecked and whose source can change after review.

## High

Use when sensitive or consequential capability is broad, poorly disclosed, weakly gated, or difficult to reverse.

- Uploading private files, prompts, contacts, messages, or business data to an unexpected service.
- Publishing, sending messages, modifying accounts, trading, paying, deleting, or changing access without action-time confirmation.
- Reading browser profiles, application databases, credential stores, or unrelated directories beyond the stated purpose.
- Automatic update or plugin loading that can introduce unreviewed code.

## Medium

Use for meaningful risk that is limited in scope or requires additional conditions.

- Unpinned dependencies, install scripts, broad network destinations, telemetry without clear retention, or incomplete OAuth scope documentation.
- Logs or caches that can retain sensitive content locally.
- Default configuration that exposes a service beyond localhost or omits authentication.
- Ambiguous failure, rollback, retry, or duplicate-action behavior.

## Low

Use for concrete hygiene or transparency issues with limited immediate impact.

- Missing checksums, stale examples, vague version support, unclear maintenance status, or absent security reporting instructions.
- Overly broad documentation language when implementation is narrow and non-sensitive.

## Positive controls

Record controls that materially reduce risk without treating them as guarantees:

- Minimal read-only scopes and project-level isolation.
- Explicit confirmation before sensitive or irreversible actions.
- Localhost binding with authentication and origin validation.
- Versioned releases, lockfiles, checksums, reproducible builds, tests, and signed artifacts.
- Clear data destinations, retention, deletion, telemetry, and incident-reporting policies.
- Dry-run support, backups, idempotency, rollback, and bounded targets.

## Evidence rules

- Prefer implementation and current primary documentation over descriptions or badges.
- Treat screenshots and example output as demonstrations, not proof of all runtime behavior.
- Treat popularity and stars as discovery signals, never as security evidence.
- Identify files that were not reviewed, generated bundles that differ from source, and remote behavior that static analysis cannot observe.
