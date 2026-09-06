# Changelog

## v0.10.32 — 2026-09-06

- Curated the MIT-licensed `Luckycat133/skills-repo` Agent Context Migrator with WorkBuddy MCP/Skill import boundaries and default exclusion of keys, OAuth, credentials, and chat history.
- Added beginner troubleshooting guidance for Skill triggers, MCP connections, file-scope mistakes, and result verification in both onboarding tutorials.
- Removed the unavailable `markbignews/paper-mode` entry after link verification returned 404, and moved it back to the discovery workflow.
- Added limited retries to the external link checker for transient failures.

## Unreleased

- Prioritized discovery results by explicit WorkBuddy/CodeBuddy relevance before Star count, so broad README matches do not hide directly compatible candidates.
- Expanded automated discovery to search repository READMEs for WorkBuddy and CodeBuddy references, while keeping matches in the unvetted queue until relevance, licensing, provenance, and permissions are reviewed.
- Curated the MIT-licensed `KHWD0922/workbuddy-skill-x-media-downloader` with CSV filtering, archive deduplication, and explicit cookies, proxy, copyright, and platform-term boundaries.
- Simplified and expanded the bilingual README and getting-started tutorials with a three-step first-task path, copyable task template, Skill/MCP/Automation guidance, and troubleshooting.
- Added a short bilingual community-resource installation path covering Skill ZIPs, Skills directories, MCP connectors, and reusable workflow documents.
- Curated the MIT-licensed `soia-team/soia-open-env-skills` collection with explicit WorkBuddy installation guidance, read-only defaults, and authorization boundaries for environment changes.
- Curated the MIT-licensed `lovejiaowu-hue/pm-to-dev-delivery` with its explicit WorkBuddy adapter and executable delivery-package validation workflow.
- Curated the MIT-licensed `OpenSenseNova/SenseNova-Skills` collection with a limited WorkBuddy compatibility note for its PPT workbench Skill and manual-install verification caveat.
- Clarified the WorkDaddy entry with its AGPL-3.0 license, installer channels, local CDP injection, OAuth/account-backup handling, and background-process boundary.
- Refreshed verified Star snapshots for WorkBuddyGuide, Skill Buddy, and Devnors Data MCP, and recorded the tutorial update in the public resource-submission issue.
- Curated the MIT-licensed `YuLaiZ/token-usage`, `genapohub/ux-design-guide`, `genapohub/team-orchestrator`, and `SuperLaos/drug-label-structurizer` resources with local-data, staged-orchestration, design-workflow, and medical-review boundaries.
- Refreshed the synchronized resource JSON, ecosystem metadata, and discovery queue for the new entries.
- Updated the public RSS feed and machine-readable entry points for the latest curation PRs and all five repository-maintained Skills.
- Added accurate Star, license, and RSS status links to the top of both README files.

## v0.10.31 — 2026-09-06

- Published the current validated directory snapshot with the latest curated resources, onboarding tutorial, ecosystem metadata, RSS feed, and machine-readable entry points.

- Curated the MIT-licensed Public Agent Suite, Poetry Resonance, and BadWeWrite resources with bilingual descriptions and usage boundaries.
- Refreshed the public RSS and `llms.txt` discovery entries for recent curation and the simplified README.
- Refreshed the ecosystem ranking with current GitHub star counts and activity dates.
- Simplified and expanded the bilingual README with goal-based starting points, resource-selection checks, and a direct resource-submission link.
- Removed duplicate entries from the bilingual resource catalog and added a regression test to prevent repeated GitHub projects within a language catalog.
- Refreshed ecosystem stars and activity metadata while keeping unvetted candidates in the discovery queue.
- Added a live GitHub Issue workflow gate that rejects discovery audits with escaped newlines or missing `Candidate`, `Audit result`, and `Decision` structure; the gate was exercised against a real audit Issue after correcting its JavaScript escaping.
- Expanded the bilingual `workbuddy-bench` entry with its four tracks, 260 tasks, Docker sandbox, Hugging Face dataset, setup Skill, and data/credential handling guidance.
- Curated the MIT-licensed `runzhi/codebuddy-statusline` with transcript, configuration-write, cache, and auto-update boundaries.
- Curated the Apache-2.0 `shajoezhu/skills_codebuddy_rpackagedev` R-package Skill collection with attribution and user-directory installation guidance.
- Curated the MIT-licensed `taikaikaikai-pixel/dsh-codebuddy-plugin` with credential, loopback bridge, external-network, and generated-file boundaries.
- Curated the MIT-licensed `MWang-TS/kindle2workbuddy` dashboard Skill with WorkBuddy database, SSH, LAN, external-weather, device, and scheduler boundaries.
- Curated the MIT-licensed `gosick233-cloud/Codex-WorkBuddy-Desktop-Bridge` MCP bridge with explicit `fullAccess`, ACP, transcript, prompt, and local-log boundaries.
- Curated the Apache-2.0 `MAXXXXXLI/workbuddy-cn-legal-skills` collection with upstream attribution and high-stakes legal-review warnings.
- Curated the MIT-licensed `Maquer/workbuddy-checkin` with credential-storage, token-refresh, multi-account, scheduling, and account-term boundaries.
- Curated the MIT-licensed `aosi526/dsh-workbuddy-xdpool` with multi-account snapshot, token-rotation, failover, billing, and loopback-bridge warnings.
- Changed ecosystem refresh to weekly/manual triggers so dynamic-metadata commits do not race curation pushes; the scheduled job continues to refresh stars, discovery, and snapshots.
- Added a standard `CITATION.cff` and bilingual citation links for the directory and v0.10.14 snapshot.
- Published v0.10.15 for the current 184-repository snapshot and updated all first-screen/citation links.
- Documented generated-file refresh commands and the weekly/manual ecosystem workflow trigger in the bilingual contribution guide.

## v0.10.16 — 2026-09-05

- Curated the MIT-licensed DSH Agent Preset Recommender for bounded, local-only WorkBuddy/CodeBuddy activity recommendations.
- Curated the MIT-licensed `agentsw` provider switcher with dry-run, backup, credential, and multi-file configuration guidance.
- Added audit records for OAuth/account-pool/check-in automation and broad-permission CodeBuddy bridging, keeping high-risk candidates out of the curated list pending deeper review.
- Refreshed the synchronized directory snapshot to 186 curated repositories and 24 discovery candidates.

## v0.10.12 — 2026-09-05

- Curated the BSD-3-Clause `wnddd839/codebuddyapi-proxy` self-hosted CodeBuddy gateway with explicit credential, account-rotation, network-boundary, and release-verification warnings.
- Added audit records for CodeBuddy2api, Cockpit Tools, and the system-prompt archive; high-star projects remain unendorsed until provenance, licensing, and data boundaries are verifiable.
- Refreshed the synchronized directory snapshot to 176 curated repositories and 24 discovery candidates.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.11 — 2026-09-05

- Added CodeBuddy2API, OpenCode CodeBuddy Auth, the WeChat Mini Program Virtual Payment Skill/reference, and the unofficial CodeBuddy IDE CN for Linux packaging adapter.
- Documented credential, API, payment, binary, EULA, supply-chain, and local-build boundaries for the new resources.
- Normalized historical discovery audit Issue bodies and fixed automatic `audit` labeling for both space-separated and colon-separated Discovery titles.
- Refreshed the synchronized directory snapshot to 175 curated repositories and 25 discovery candidates.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.9 — 2026-09-05

- Added TencentDB Agent Memory, an MIT-licensed, Tencent-maintained WorkBuddy Proxy integration for shared Chat Memory, Skills, LLM Wiki, and CodeGraph workflows.
- Documented model-key, local-port, user-authentication, retention, team-sharing, and external-deployment boundaries.
- Refreshed the synchronized directory snapshot to 162 curated repositories and 34 discovery candidates.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.8 — 2026-09-05

- Added MIT-licensed OpenMAIC, a WorkBuddy-compatible classroom Skill for multi-agent lessons, slides, quizzes, interactive HTML, PBL activities, and TTS.
- Added Apache-2.0 memU and MIT-licensed AgentsView for WorkBuddy session memory/Skill extraction and local session search/analytics.
- Documented upload, external-service, credential, transcript, scheduled-task, daemon, remote-sync, and write-scope warnings for the new integrations.
- Refreshed the synchronized directory snapshot to 161 curated repositories and 34 discovery candidates.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.7 — 2026-09-05

- Added the MIT-licensed cross-platform WorkBuddy Auto Check-in Skill with macOS/Windows installers, one-instance locking, sanitized logs, legacy-job backup, and tests.
- Added a maintainer-facing discovery audit Issue template that fixes the `Candidate` / `Audit result` / `Decision` structure and prompts for licensing, provenance, permissions, data flow, and account-term evidence.
- Refreshed the synchronized directory snapshot to 158 curated repositories and 34 discovery candidates.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.6 — 2026-09-05

- Added the MIT-licensed Travel Planner Skill with WorkBuddy/CodeBuddy installation, requirement confirmation, external research, and responsive HTML itinerary generation.
- Documented optional Xiaohongshu session, personal itinerary, freshness, booking-channel, and manual-verification boundaries.
- Refreshed the synchronized directory snapshot to 157 curated repositories.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.5 — 2026-09-05

- Added the MIT-licensed LibTV Video Agent Skill with WorkBuddy/Codex/Claude entry points for storyboard, generation, TTS, subtitle, and local FFmpeg workflows.
- Documented official-login, local-credential, external-service, media-rights, cost, upload-scope, and human-review boundaries.
- Refreshed the synchronized directory snapshot to 156 curated repositories.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.4 — 2026-09-05

- Added the MIT-licensed WorkBuddy Check-in Skill with explicit local-token, official-endpoint, scheduled-execution, and account-terms warnings.
- Refreshed the bilingual searchable directory, ecosystem metadata, and discovery queue to 155 curated repositories.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.3 — 2026-09-05

- Added an MIT-licensed WorkBuddy MCP OAuth 2.1/PKCE troubleshooting guide with redirect-URI allowlists, authorization checks, redacted examples, and unit tests.
- Refreshed the generated ecosystem metadata for the new reference.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.2 — 2026-09-05

- Added Tencent's MIT-licensed LoopForge workflow for confirmable, reviewable, testable, and resumable multi-agent delivery.
- Added the MIT-licensed AI Project Workflow with explicit CodeBuddy support, stage contracts, state gates, artifact requirements, and CLI adapters.
- Broadened the discovery job to cover both WorkBuddy and CodeBuddy repositories while keeping candidates in a review-only queue.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.1 — 2026-09-05

- Added the WorkBuddy Experts study archive, covering 246 expert prompts, seven Nunjucks templates, two built-in Skills, and a reverse-engineering report.
- Clarified the archive's split licensing and copyright boundaries: MIT applies to the curation/index/report, while expert prompts and Tencent-customized templates retain upstream or Tencent terms and are limited to personal study.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.10.0 — 2026-09-05

- Expanded the bilingual directory to 150 curated repositories and refreshed the searchable Pages catalog, ecosystem metadata, and discovery queue.
- Added WorkBuddy Harness, ZZZ Plain-language AI Guide, WorkBuddy2API (Tom6814), and FyAgent, covering Agent runtime/evaluation, beginner learning, protocol compatibility, and local model/Skill/MCP configuration.
- Added explicit disclosures for source-available or undeclared licensing, local configuration writes, API keys and sign-in tokens, undocumented endpoints, optional cloud backups, executable Hooks, and high-stakes data boundaries.
- Documented discovery holds for candidates whose MCP transport or dataset provenance is not yet consistent, keeping the queue auditable without treating unverified projects as endorsements.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.8.0 — 2026-09-05

- Expanded the bilingual directory from 62 to 91 curated repositories while reducing the unreviewed discovery queue to 23 candidates.
- Added first-party WorkBuddy guides for Explore, remote assistants, Lexiang knowledge bases, and default versus Full Access permission modes.
- Curated high-adoption and practical integrations including Beav, the WorkBuddy WeChat OpenClaw channel, Session Fork, Workbuddian, DSH Memory Palace, DSH Agent Selector, and M5Stack Core2 Buddy.
- Added focused Skills and workflows for PDF extraction, agent analytics, research, learning, content production, prompt management, local session inspection, and professional data work.
- Strengthened entries with evidence-backed disclosures for non-commercial or missing licenses, OAuth and token storage, local databases and transcripts, browser/social content, external services, destructive fixes, and binary/source version gaps.
- Upgraded GitHub Pages Actions to Node 24-compatible releases and made overlapping ecosystem refreshes cancel stale runs so the latest generated indexes win.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's current license, source or binary provenance, credentials, permissions, data flows, and account terms before use.

## v0.7.0 — 2026-09-05

- Curated 62 WorkBuddy-related repositories with bilingual descriptions, license notes, and permission/data-boundary cautions.
- Added OpenBuddy, Tonghuasun Agent, BossMate, WorkBuddy Wiki, WorkBuddy2API, and the WorkBuddy CLIProxy provider after upstream review.
- Expanded the searchable bilingual Pages directory and machine-readable `site/llms.txt` index.
- Added consistency checks so the curated repository source, ecosystem ranking, resource directory, snapshot count, and discovery queue remain aligned.
- Refreshed the discovery queue and ecosystem metadata from GitHub.

This release is a documentation and curation update. Indexed projects are independent of this repository; review each project's license, source, credentials, permissions, and account terms before use.
