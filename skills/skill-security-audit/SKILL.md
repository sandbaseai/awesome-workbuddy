---
name: skill-security-audit
description: Audit a third-party Agent Skill, MCP server, connector, or desktop extension before installation by tracing instructions, executable code, dependencies, permissions, credentials, data flow, and irreversible actions.
---

# Skill Security Audit

Assess the supplied project using repository contents and primary documentation. The default audit is read-only: do not install dependencies, execute project code, sign in, provide credentials, or connect the project to a real Agent or account.

## Audit

1. Record the exact repository, revision or release, license, archive status, latest meaningful update, and files reviewed. If the audited revision is unclear, state that limitation.
2. Read the complete `SKILL.md` or equivalent instructions and every file it directly invokes. Follow references to scripts, hooks, manifests, package install steps, binaries, remote URLs, environment variables, and bundled assets.
3. Build a capability inventory: local file access, command execution, network access, browser control, account actions, publishing, messaging, deletion, payment, credential access, persistence, and self-update behavior.
4. Trace sensitive data from its source to every local store, subprocess, log, model, API, MCP server, analytics service, or other network destination. Missing documentation is an unresolved question, not proof that data stays local.
5. Inspect dependency manifests, lockfiles, install scripts and release provenance. Note unpinned remote execution, opaque binaries, broad transitive dependencies, or mismatches between source and distributed artifacts.
6. Apply the [risk signals and severity model](references/risk-signals.md). A risky capability can be legitimate when it is necessary, disclosed, narrowly scoped, reversible, and confirmation-gated.
7. Separate confirmed findings from contextual risks and unanswered questions. Cite file paths, lines, configuration fields, commands, or primary documentation for every material claim.

## Output

Begin with the audited identity and one verdict:

- **Lower observed risk**: no material concern was found in the reviewed scope, but this is not a guarantee.
- **Review required**: important behavior, provenance, permissions, or data flow remains unclear.
- **High observed risk**: confirmed behavior could expose sensitive data, weaken account or device security, cause irreversible action, or bypass informed control.

Provide these sections:

1. Scope and limitations.
2. Capability and permission table.
3. Data-flow table.
4. Findings ordered by severity, each with evidence, impact, and mitigation.
5. Unanswered questions.
6. A minimal-permission test plan using disposable data or accounts.

Do not label a project safe, malicious, official, or compliant without evidence sufficient for that specific claim. Static review cannot prove runtime behavior or the contents of an opaque remote service.
