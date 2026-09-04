# Resource review rubric

Use only the rows that apply, and mark missing evidence as `unknown` rather than assuming a favorable answer.

| Area | Questions | Evidence to capture |
| --- | --- | --- |
| Identity and scope | What is the canonical repository or document, revision, and intended audience? | URL, commit/release, review date, README or landing page |
| Direct relevance | Does it work with or teach Tencent WorkBuddy, and is that relationship explicit? | installation instructions, compatibility statement, examples, official references |
| Distinct value | What concrete problem does it solve that the current directory does not already cover? | capabilities, examples, comparison with existing entries |
| Maintenance | Is there meaningful recent activity, a usable release, tests, issue handling, or a clear maintenance path? | commit/release dates, CI, tests, issue tracker, changelog |
| License and provenance | Can users legally inspect and reuse it, and are bundled or adapted materials attributed? | license file, manifest, notices, source links, release provenance |
| Permissions | What can it read, write, execute, delete, publish, or control? | scripts, hooks, manifests, install commands, platform permissions |
| Credentials and accounts | Does it request tokens, cookies, passwords, OAuth, QR login, or account binding? | environment variables, auth code, prompts, credential storage and scope |
| Data flow | What local or user-provided data enters files, subprocesses, models, APIs, analytics, or remote services? | source and destination paths, URLs, payload construction, logs, retention claims |
| Network and updates | Does it call external endpoints, download code, self-update, or use unpinned dependencies? | URLs, package manifests, lockfiles, installer and update scripts |
| Irreversible actions | Can it mutate databases, overwrite files, send messages, publish content, spend money, or alter accounts? | commands, confirmation gates, backups, rollback, dry-run behavior |

## Decision thresholds

- **Include:** no unresolved material risk in the reviewed scope; any remaining contextual risk is stated in the directory entry.
- **Hold:** useful and plausibly relevant, but one or more material areas lack enough evidence or need an upstream clarification.
- **Exclude:** the candidate fails scope or value requirements, or confirmed behavior conflicts with the directory's safety or provenance requirements.

These thresholds describe curation confidence, not a security certification. Static inspection cannot establish the behavior of opaque binaries, remote services, or code paths that were not reviewed.
