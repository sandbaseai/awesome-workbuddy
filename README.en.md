![Awesome WorkBuddy - Skills, MCP, Workflows and Guides](assets/awesome-workbuddy-banner.webp)

# Awesome WorkBuddy

English · [简体中文](README.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Check links](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml/badge.svg)](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml) [![GitHub stars](https://img.shields.io/github/stars/sandbaseai/awesome-workbuddy?style=social)](https://github.com/sandbaseai/awesome-workbuddy)

> A curated, verifiable collection of Tencent WorkBuddy learning resources, Skills, MCP integrations, and real-world workflows.

Want to help us reach 100 genuine stars? Use the [community roadmap issue](https://github.com/sandbaseai/awesome-workbuddy/issues/172) to suggest verifiable resources, report broken links, or share usage feedback.

New to WorkBuddy? Begin with the [one-minute chooser and quick start](START_HERE.md), or use the [searchable resource directory](https://sandbaseai.github.io/awesome-workbuddy/) to filter by keyword and category.

For a compact machine-readable overview, see [`site/llms.txt`](site/llms.txt).

WorkBuddy is Tencent's AI Agent workspace for planning and carrying out research, document, data, design, and development tasks with natural language. This list starts with official documentation and then highlights community resources that offer reproducible steps, open source, or distinct practical value.

> [!IMPORTANT]
> This is an independent community index, not a Tencent publication. Before installing any third-party Skill, MCP server, connector, or enhancement, inspect its source, permissions, and data flow. Never upload secrets, personal data, or unredacted company material without an appropriate review.

## Contents

- [Start Here](#start-here)
- [Official Resources](#official-resources)
- [Open-source Ecosystem](#open-source-ecosystem)
- [Skills, Prompts, and MCP](#skills-prompts-and-mcp)
- [Guides](#guides)
- [Use Cases](#use-cases)
- [Research and Engineering](#research-and-engineering)
- [Related Lists](#related-lists)
- [Selection Standard](#selection-standard)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Start Here

- [Product homepage](https://www.workbuddy.ai/) - Product overview, downloads, and plan information.
- [Official documentation](https://www.workbuddy.ai/docs/zh/workbuddy/) - The authoritative documentation hub.
- [Quick start](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) - From installation to a first completed task.
- [Install on macOS](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) - Official requirements, download, installation, sign-in, and update steps for Mac.
- [Install on Windows](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide) - Official requirements, download, installation, sign-in, and update steps for Windows.
- [Ten getting-started tips](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Efficient-Tips) - Practical guidance on clear tasks, iterative work, examples, backups, automation, and context management.
- [Troubleshooting FAQ](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FAQ) - Official answers for installation, sign-in, integrations, files, workspaces, and conversation recovery.
- [Changelog](https://www.workbuddy.ai/docs/zh/workbuddy/Changelog) - Product capabilities, fixes, and compatibility changes.
- [Index changelog](CHANGELOG.md) - Versioned updates to curation, indexes, quality gates, and safety disclosures.
- [Automation guide](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) - Create one-time or recurring tasks and send results to connected platforms.
- [MCP guide](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) - Connect external tools and data through visual configuration.
- [WorkBuddy Enterprise quick start](https://cloud.tencent.com/document/product/1831/134527) - Create, test, publish, and connect an enterprise Agent to messaging channels.

## Official Resources

### Core concepts

- [Create a task](https://www.workbuddy.ai/docs/zh/workbuddy/Create-Task) - Describe the goal, select a working directory, attach context, and start execution.
- [Task conversation](https://www.workbuddy.ai/docs/zh/workbuddy/Conversation) - Use interaction modes, send files and images, follow execution, interrupt, and continue.
- [Task management](https://www.workbuddy.ai/docs/zh/workbuddy/Task-Management) - Search, filter, inspect task states, organize workspaces, and resume existing tasks.
- [View results](https://www.workbuddy.ai/docs/zh/workbuddy/Results) - Inspect artifacts, table and document previews, web output, files, and changes.
- [Task bar and Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar) - Learn where to find, import, and create Skills.
- [Skills marketplace](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) - Browse, install, enable, and manage WorkBuddy Skills in one place.
- [Create a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) - Turn a natural-language workflow into a reusable Skill.
- [Explore](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Explore) - Browse official creations across seven scenario categories, preload their Prompt, Skill, and Expert setup to make your own version, and understand how Explore differs from Skills and Experts.
- [Expert Center](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Expert-Center) - Choose a specialist with its own methods and tools, or a multi-Agent team whose lead delegates parallel work.
- [Assistant (remote tasks)](https://cloud.tencent.com/document/product/1831/134392) - Trigger WorkBuddy on a desktop from Weixin, WeCom, QQ, DingTalk, or Feishu; review channel authorization, local workspace, task permissions, and returned-artifact scope before connecting.
- [Two permission modes](https://cloud.tencent.com/document/product/1831/134401) - The official guide to default permissions, workspace boundaries, confirmation prompts, and Full Access; back up important files and enable full access only briefly in a trusted, isolated, recoverable environment.
- [Connectors](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Connector) - Connect services such as QQ Mail and Tencent Docs, with first-party configuration and authorization steps.
- [Memory](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Memory) - View, edit, import, or ask WorkBuddy to forget preferences and habits extracted from conversations.
- [Model configuration](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model) - Choose automatic or built-in models, or connect a custom model and protocol.
- [Data management](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Data) - Find shared files and manage archived tasks.
- [System settings](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Setting) - Configure language, type size, display modes, safe installation behavior, and sleep prevention.
- [From model to harness](https://mp.weixin.qq.com/s/X_kaKcXH2uELcemaNaZ4iQ) - An architectural introduction to the WorkBuddy Agent product.

### Platform integrations

- [Slack integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Slack-Guide) - Create a Slack App, configure permissions, and connect it to WorkBuddy using the official steps.
- [Telegram integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Telegram-Guide) - Configure a Telegram Bot and provide its token to WorkBuddy using the documented flow.
- [Discord integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Discord-Guide) - Create a Discord application and bot, configure permissions, and add it to a server.
- [WeCom integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Wecom-Guide) - Connect the WorkBuddy assistant to WeCom and complete the organization-side setup.
- [Feishu integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Feishu-Guide) - Create a Feishu app, configure events and permissions, and connect it to WorkBuddy.
- [DingTalk integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Dingtalk-Guide) - Configure a DingTalk bot and the WorkBuddy assistant using the official flow.
- [QQ integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/QQ-Guide) - Connect the WorkBuddy assistant to QQ and complete bot configuration and authorization.
- [Weixin Assistant integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/WeixinBot-Guide) - Connect the WorkBuddy assistant to Weixin using the official configuration and QR sign-in flow.
- [YuanBaoPai integration](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/YuanBaoPai-Guide) - Connect the WorkBuddy assistant to a YuanBao bot using the official configuration flow.
- [Lexiang knowledge base](https://cloud.tencent.com/document/product/1831/134398) - Authorize WorkBuddy to search and cite team-space content and save outputs back to Lexiang; verify account authorization, knowledge-base visibility, source files, and the write-back destination first.

### Community channels

- [WorkBuddy product page](https://cloud.tencent.com/product/workbuddy) - Tencent Cloud's product information and updates.
- [Tencent Cloud developer articles](https://cloud.tencent.com/developer/search/article-WorkBuddy) - Searchable community engineering articles.

## Open-source Ecosystem

> [!NOTE]
> “Works with WorkBuddy” does not mean “endorsed by Tencent.” Projects are selected for direct relevance, documentation quality, maintenance, and community adoption. Check licenses, account terms, permissions, and credentials before using unofficial automation or API tooling.

### Learning and reference

- [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) - An open practical handbook covering tutorials, workflows, Skills, MCP, automation, and multi-agent patterns.
- [How to Use Agent](https://github.com/Lukanytsu7551/how-to-use-agent-guide) - An MIT-licensed Chinese tutorial site with a 27-chapter WorkBuddy manual, 100-case library, and Codex/Agent learning paths, plus a provenance NOTICE and security policy. Some Agent Guide adaptations use CC BY-NC-SA 4.0, the repository includes substantial media, and its AI News build calls an external public API; check the applicable license, storage, and network scope before reuse or local builds.
- [Agent Learning Guide](https://github.com/tangshiyegit/agent-guide) - A MIT-licensed guide with 19 WorkBuddy tutorials and 12 office, content, and automation case studies; verify changing third-party product details against official sources.
- [AI Coding Guide Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh) - A Chinese learning path for AI coding tools and office Agents, including WorkBuddy.
- [learn-workbuddy](https://github.com/adongwanai/learn-workbuddy) - A 24-chapter Python tutorial that builds a WorkBuddy-style desktop Agent from scratch.
- [WorkBuddy Harness Bluebook](https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness) - Explains prompts, memory, plugins, experts, Skills, and safety boundaries.
- [Undergraduate Thesis AI Workflow](https://github.com/Sqhao-O/undergraduate-thesis-ai-workflow) - A MIT-licensed six-part workflow guide covering Claude Code, Kimi, CC Switch, Pandoc, Lark-Formatter, and WorkBuddy formatting for undergraduate theses; it explicitly requires authentic research, data, and citations, so follow institutional policies and review API keys and source-material scope before use.

### Skill collections

- [WorkBuddy Wiki](https://github.com/YuanYiZheXue/workbuddy-wiki) - An Apache-2.0 WorkBuddy + Obsidian local knowledge-base system with versioned schemas, cross-workspace synchronization, source/concept/entity organization, and health diagnostics; confirm the scope of local knowledge and synchronization before use.

- [WorkBuddy Skill Hub](https://github.com/sandbaseai/workbuddy-skill) - A searchable catalog of 10,000 public Skill paths with provenance, license, security, and compatibility review fields.
- [Senmu BuildOS](https://github.com/SenMuShare/senmu-buildos) - An Apache-2.0 cross-tool Agent engineering coach and Skill collection with explicit WorkBuddy support, covering requirements, design, implementation, testing, Git, releases, evidence, and rollback; installation changes workspace rules and may perform deployment/version actions, so review instructions, host permissions, credentials, and release targets first.
- [i18n Helper Skills](https://github.com/liangdabiao/i18n-helper-skills) - A license-not-declared internationalization Skill collection for WorkBuddy/Codex and other Agents, with complementary workflows for static HTML language directories and translation functions in React/Vue/PHP/Python/Java source, plus extraction, application, and completeness-check scripts; it batch-reads and rewrites project files, so back up and review target scope and licensing first.
- [PMCockpit](https://github.com/wsdlp46/PMCockpit) - An Apache-2.0 AI product-management cockpit for WorkBuddy, Codex, and Claude that turns requirements, specs, prototypes, reviews, retrospectives, and lessons into eight executable Skills; its installer changes or symlinks workspace entry points, while testing and VitePress capabilities are opt-in, so confirm workspace, template, and external-project permissions first.
- [QingFeng Skills](https://github.com/chenwg001/qingfengskill) - An MIT-licensed WorkBuddy-first collection of 17 Skills for education and content work, covering writing, PPTs, image/video production, and platform draft publishing, with per-directory installation; publishing Skills use browser/CDP access to platform accounts and content, so confirm that credentials are not hard-coded, review approval gates, platform terms, and publishing scope first.
- [Image Skill](https://github.com/Mariposa-FLOA/image-skill) - A collection of 17 visual Skills for WorkBuddy, Codex, and compatible Agents covering poster art direction, image workflows, page-flip showcases, and layered PSD export, with bilingual usage documentation and per-asset provenance; Skills and docs are CC BY-NC 4.0, scripts are Apache-2.0, and examples are view/link only, so also confirm input-image privacy, external generation services, HyperFrames/FFmpeg/Pillow dependencies, and local output scope.
- [workbuddyskills](https://github.com/infometa/workbuddyskills) - An offline archive of WorkBuddy Skills, connectors, and experts.
- [Website Prompts and Skills](https://github.com/TencentEdgeOne/awesome-website-prompts-and-skills) - Website-generation prompts, Skills, and challenge entries maintained by Tencent EdgeOne.
- [Ray Skills](https://github.com/imraywang/rayskills) - Executable, verifiable, and recoverable workflows for content production and publishing.
- [WorkBuddy Skills](https://github.com/bitcjm/workbuddy-skills) - Skills for writing, programming, office work, and general utilities.
- [Zotero MCP WorkBuddy Guide](https://github.com/maciechen/zotero-mcp-workbuddy-guide) - A Chinese guide to connecting a local Zotero library to WorkBuddy.
- [DSH Skill Picker](https://github.com/a735624258/dsh-skill-picker) - Adds searchable, pinyin-aware, keyboard-friendly skill picking to the DeepSeek Harness Web GUI, reproducing WorkBuddy-style `/skill-name` invocation; MIT licensed. It reads user and project Skill directories and exposes a local Web route, so review its filesystem scope before installation.
- [Kunpeng Skill](https://github.com/hufeng173/kunpeng-skill) - An Apache-2.0 multi-source distillation Skill for WorkBuddy, Codex, Claude Code, and other Agents. It turns repositories, websites, UI, images, audio/video, and documents into evidence-backed reusable methods and generation specifications; install its optional local analyzers only after reviewing dependencies and file scope.
- [Skill Doctor](https://github.com/evilstar2016/skill-doctor) - A local MIT-licensed CLI for auditing Skill conflicts, duplicates, security risks, and context cost across WorkBuddy and other Agents. It reads local resources by default and binds its UI to loopback; still confirm scan scope and report contents before exporting results.
- [WorkBuddy Usage Status](https://github.com/clancy-feng/workbuddy-usage-status) - Turns WorkBuddy's local data into an offline, auditable dashboard for token/credit usage, model efficiency, and errors; MIT licensed, read-only and zero-network by default, with precise usage API access enabled only when the user explicitly supplies a token.
- [Agent Analytics Report](https://github.com/Elisabeth15501/agent-analytics-report) - An MIT-licensed, WorkBuddy-first usage-analysis Skill that reads local session/usage data to produce token, cache, model-cost, and anomaly reports in Markdown, HTML, or JSON, with 306 synthetic-fixture tests; listed prices are estimates, so confirm local read scope and redact reports before sharing.
- [UsageMonitor WorkBuddy Provider](https://github.com/masclown/usage-monitor-plugin-workbuddy) - An Apache-2.0 independently versioned UsageMonitor provider that reads WorkBuddy subscription quotas, gift packages, and request history with model, channel, and operation slicing; it uses browser login state to call official `workbuddy.cn` web endpoints and handles Cookies, so review account authorization, network requests, storage scope, and service terms first.
- [Session Digger](https://github.com/taxueseek/session-digger) - An ISC-licensed cross-agent session search and knowledge-management toolkit that natively parses `~/.workbuddy/projects`, builds an incremental SQLite FTS index, and produces self-contained local reports; it reads full transcripts and writes indexes, reports, and optional memory files that may expose prompts, paths, or project data, its environment doctor can probe external endpoints, and every target and backup should be reviewed before using mutating `apply`/`prune` commands.

### Ready-to-use Skills

- [Majia Huiyuan](https://github.com/maojiebc/majia-huiyuan) - An MIT-licensed membership-operations and data-system Skill with a WorkBuddy single-expert package, 55 simulated logical datasets, 25 ETL flows, 12 role-oriented dashboards, and RFM, retention, coupon-effectiveness, and data-quality references; no values are real business benchmarks, SQL targets Spark 3.4, historical platform JSON is not a current import package, production use requires schema mapping, metric agreement, and regression acceptance, and its build tool recreates the selected output directory and ZIP.
- [Pandadata API Skill](https://github.com/quantskills/skill-pandadata-api) - A GPL-3.0 installable financial-data Skill for WorkBuddy/Codex with local documentation for 218 APIs, search tooling, a compatibility index, and optional live calls; its runtime installs `panda_data` and data dependencies and contacts a user-configured external service, while setup may save the username and plaintext password to a mode-600 `~/.pandadata/pandadata.env` and the SDK also writes `user.json`, so protect credentials, confirm data entitlements, and do not treat outputs as investment advice.
- [Photo to Monthly Zine Postcard](https://github.com/shenchangyi/photo-to-monthly-zine-postcard) - An MIT-licensed, directly installable WorkBuddy/Codex Skill that turns a user photo into a 3:4 monthly Zine postcard and requires verified, image-matched literature and music sources; it ships no executable scripts or credential handling, but photos may contain people, locations, EXIF, or branding and its research/image-generation steps may contact external services, so confirm media privacy and network boundaries first.
- [XHS Blogger Analyzer](https://github.com/arraycto/xhs-blogger-analyzer) - An MIT-licensed WorkBuddy/Claude Skill that uses MCP to collect public Xiaohongshu creator content and generate content-strategy, topic, and structured-analysis documents; its installer downloads dependencies and a third-party MCP binary, and first use requires QR login, so review platform terms, account permissions, crawl scope, download provenance, and creator/personal-data privacy first.
- [AI 10x Learning](https://github.com/luozhilzh/ai-10x-learning) - An MIT-licensed ten-step learning-loop Skill compatible with WorkBuddy, Codex, Claude, and Cursor, combining multi-perspective research, retrieval practice, Feynman explanation, and HTML learning cards; it includes an installer, source-verification rules, and a local card validator, so confirm external facts, personal study data, and installer file scope first.
- [Book Video Generator](https://github.com/chenjun198711/book-video-generator) - An MIT-licensed book-video Skill compatible with WorkBuddy, Codex, Claude, and other Agents, covering book research, scripts, storyboards, AI images, TTS, subtitles, and ffmpeg MP4 composition; it contacts external model/voice services and may read API keys, so verify book facts, copyright and attribution, key storage, and generated-content quality first.
- [Hotspot Monitor Skill](https://github.com/jiangxu1024/hotspot-monitor-skill) - An MIT-licensed WorkBuddy trend-monitoring Skill that collects several Chinese platforms, filters by keywords, and schedules Feishu Base writes and mobile notifications; configuration involves a Feishu App Secret, Base Token, Table ID, and webhook, while crawling and pushing remain subject to platform terms and personal-data boundaries, so use secure local configuration and review permissions first.
- [Bazi-Ziwei Skill](https://github.com/mingze21/bazi-ziwei-skill) - An MIT-licensed Bazi and Ziwei-doushu Skill compatible with WorkBuddy, Codex, Claude, and Cursor, using local chart algorithms, prompts, and shareable HTML posters with a test guide and synthetic examples; birth details enter local artifacts, and divination is not scientific diagnosis and should not guide medical, legal, financial, or major life decisions.
- [Prompt Toolkit](https://github.com/xiaolouJB/prompt-toolkit) - A CC BY-NC 4.0 multi-agent distribution package with 12 general-purpose prompts, including native WorkBuddy Skills and adaptations for Claude Code, Cursor, Trae, and CodeBuddy, covering questioning, learning, fact-checking, decisions, and life design; it is adapted from Digital Life Kazik and requires attribution, source retention, and non-commercial use.
- [Paper CN Reader](https://github.com/langlibai66/paper-cn-reader) - An MIT-licensed academic-paper reading, translation, and annotation Skill for WorkBuddy that preserves PDF figures, tables, and formulas while producing HTML/PDF; it requires PyMuPDF, Playwright, and Chromium, loads MathJax from jsDelivr by default, and writes documents/assets to a user-selected directory, so review dependency and network/write scope first.
- [BossMate](https://github.com/yinren112/bossmate) - An MIT-licensed local job-search Skill for WorkBuddy that reads complete JDs in a visible browser, deduplicates opportunities, and gates messages before sending; it does not request passwords, cookies, or session tokens, but users must follow platform rules and review resume, browser-profile, and message-data scope.
- [IELTS Buddy Agent Skills](https://github.com/Jobo16/ielts-buddy) - An MIT-licensed IELTS learning Skill collection for WorkBuddy covering study plans, writing/speaking/reading/listening review, vocabulary, and mock exams, with installation and validation scripts; optional personal-learning API binding and local tokens require careful data-scope review, and passwords, cookies, and tokens should never be shared.
- [PDF Structured Extractor](https://github.com/ttww1111/pdf-structured-extractor) - An MIT-licensed PDF-extraction Skill compatible with WorkBuddy, Codex, and Claude; it uses only PyMuPDF to emit structured Markdown/CSV for text, tables, and images, detects two-column, scanned, and garbled pages, and reports quality warnings. It has no network or telemetry by default, but reads selected PDFs and writes outputs, so review file and output scope first.
- [Roundtable KG](https://github.com/xiewende424/roundtable-kg) - An MIT-licensed, WorkBuddy-compatible offline roundtable Skill that debates serious questions through position-based personas and renders argument relations as an interactive force-directed graph; it needs only Python 3.8+ with no third-party dependencies, but the graph shows discussion structure rather than proof, so verify sources and conclusions.
- [AI Weekly Report](https://github.com/Elisabeth15501/ai-weekly) - An MIT-licensed AI-industry weekly-report Skill compatible with WorkBuddy, Codex, and other Agents. It builds a searchable, filterable, dark-mode single-file HTML report from RSS and optional search data, preserving source links and fallbacks; it needs network fetching and a few Python dependencies, so verify source freshness, market figures, and external publishing targets.
- [AI Short Drama Skills](https://github.com/zkhyww/ai-short-drama-skills) - An MIT-licensed pair of Skills for WorkBuddy and other Agents that separates short-drama development and production across topic, script, table read, storyboards, assets, sound, editing, and QC, with deterministic preflight and distinct master/submission documents; media execution may use Dreamina OAuth, model services, and ffmpeg, so review credits, rights, external services, and human rehearsal/review before delivery.
- [1688 Product Reader](https://github.com/yyc424666lvy/1688-product-reader) - An MIT-licensed, read-only WorkBuddy Skill for extracting product title, price, MOQ, seller, SKU, images, and specifications from logged-in 1688 pages; the user signs in manually in an isolated browser profile, and the Skill does not place orders or manage login state, so review platform terms, page access, and information freshness first.
- [A-share Watch Copilot](https://github.com/WaterCMY/A-share-watch-copilot) - A WorkBuddy Skill for A-share/Hong Kong market monitoring with position and fund schemas, eight automation templates, reports, and an optional local dashboard; its license appends personal-learning/research restrictions after MIT text, and financial data and conclusions require human verification and must not drive automated trading or unlawful advice. Position files contain sensitive financial data, scripts contact Tencent, Eastmoney, and Sina endpoints, and the unauthenticated local server listens on `0.0.0.0:8801` and can rewrite holdings, so use it only on a trusted private network or bind it to loopback.
- [Math Concept Film](https://github.com/liangdabiao/math-concept-film) - A license-not-declared mathematics short-film Skill compatible with WorkBuddy, Codex, and Claude, using a voice-first caption timeline to drive Manim animation with a six-act teaching framework, still-frame checks, and ffmpeg composition; narration relies on Microsoft's online TTS, so review network use, source-material rights, output scope, and licensing before use.
- [Eagle Untagged Organizer](https://github.com/ChosenXu/eagle-untagged-organizer) - An MIT-licensed WorkBuddy Skill that uses eagle-mcp to name, annotate, and tag untagged design assets; it provides multimodal preflight, a dry-run manifest, batch backups, human approval, and rollback, so confirm the Eagle library, MCP permissions, and write scope before execution.
- [Rainskills](https://github.com/goodrain/rainskills) - An Apache-2.0 Skill collection compatible with WorkBuddy, Codex, Claude, and other Agents for project detection, build/deploy, log troubleshooting, page/API verification, versioning, snapshots, and rollback; it can connect to Rainbond Cloud, an existing Rainbond instance, or local/server environments, so review credentials, network, host permissions, and rollback targets first.
- [Session Fork](https://github.com/yamingmou/session-fork-core) - An MIT-licensed WorkBuddy Skill that copies a conversation into an independent branch by the prior output, request ID, or text match, with dry-run preview, automatic backup, and branch lineage; it relies on unofficial local-storage internals, reads transcripts, inserts rows into `~/.workbuddy/workbuddy.db`, writes a lineage index, and can rewrite branch files with `--fix`, while its backup covers only the source JSONL, so quit WorkBuddy and separately back up the database and sensitive sessions first.

This repository maintains four original installable Skills: [Document Quality Review](skills/document-quality-review/SKILL.md) performs read-only delivery checks, [Skill Security Audit](skills/skill-security-audit/SKILL.md) reviews third-party extensions before installation, [Source-backed Research Brief](skills/source-backed-research-brief/SKILL.md) turns web research into a verifiable brief with facts and inference kept distinct, and [Curate WorkBuddy Resource](skills/curate-workbuddy-resource/SKILL.md) gives candidates evidence-backed include, hold, or exclude decisions across relevance, quality, licensing, provenance, and safety.

- [WorkBuddy Guide](https://github.com/Neo5093/workbuddy-guide) - An installable WorkBuddy usage and troubleshooting Skill covering connectors, experts, automations, memory, interaction modes, and FAQs; MIT licensed. Its optional diagnostic script reads local `~/.workbuddy` configuration and recent logs and probes a localhost health endpoint, so inspect and redact output before sharing it.
- [E-commerce Visual Copywriting](https://github.com/feichanggege/ecommerce-visual-copywriting-skill) - A repeatable workflow for product analysis, copywriting, and commerce imagery.
- [Image Story Video Wizard](https://github.com/aaronyi97/image-story-video-wizard) - An audio-first story-video Skill for WorkBuddy and Codex with approval gates at consequential steps.
- [Social Account Doctor](https://github.com/JuneYaooo/social-account-doctor) - Diagnoses accounts and high-performing posts across major Chinese content platforms.
- [Bruce Draw.io](https://github.com/bruc3van/bruce-drawio) - Generates, validates, and exports draw.io diagrams across platforms.
- [Textbook Writer Skills](https://github.com/cabbage2000-lab/textbook-writer-skills) - Plans, writes, and reviews textbooks using Understanding by Design.
- [OfferLoop](https://github.com/riwonswain-ovo/OfferLoop) - An open job-search system built from seven Skills and a Feishu workspace.
- [Job Navigation Skill](https://github.com/AriaXXX-free/job-navigation-skill) - An evidence-based Skill that researches current roles and JDs, compares them with resume/project evidence, and prioritizes job-search actions; MIT licensed and compatible with WorkBuddy, Codex, Claude, and Cursor. It can research public job information on request, so review personal-data scope and retrieved sources before use.
- [WorkBuddy WeChat Publisher](https://github.com/cnproduct/workbuddy-wechat-publisher) - Produces copy, images, layout, and WeChat Official Account drafts.
- [CordysCRM Skills](https://github.com/1Panel-dev/CordysCRM-skills) - Agent Skills covering a CRM lead-to-cash workflow.
- [Self-media Compliance Review](https://github.com/JuneYaooo/self-media-compliance-review) - Reviews videos, covers, subtitles, sales claims, and platform risks before publishing.
- [Ontology-driven Development](https://github.com/sharptoolbox/ontology-driven-dev) - A traceable workflow from requirements and ontology modeling to application delivery.
- [Codebase Reverse](https://github.com/sharptoolbox/codebase-reverse) - Reconstructs functional, architectural, API, and data-model documentation from Java services.
- [Trade Pipeline](https://github.com/Dangooy/trade-pipeline-skill) - Generates quotations, pro forma invoices, commercial invoices, and packing lists from one order record.
- [SeaTable Production](https://github.com/Darling5/seatable-production) - An MIT-licensed WorkBuddy production-delivery Skill covering projects, planning, procurement, BOM/inventory, shipping, maintenance, and analysis; it defaults to local CSV, shows the full change set and waits for confirmation before writes, and optionally connects to SeaTable, PartDB, or an ERP, so review credentials, field mapping, external APIs, and write scope first.
- [Local Markdown Memory](https://github.com/asen-goat-mine/boujoy-local-markdown-memory) - A local-first, auditable long-term Markdown memory template for WorkBuddy and Codex.
- [Org Context](https://github.com/wangjialiang678/org-context) - An MIT-licensed context-organization Skill for WorkBuddy, Claude Code, and OpenCode that separates facts, decisions, and status to make enterprise materials easier to retrieve, with templates, a runnable example, and mechanical checks; it handles local company materials and rewrites workspace files by default, so back up and confirm scope first.
- [Delivery Razor](https://github.com/Ketian823/delivery-razor) - An MIT-licensed WorkBuddy delivery-hygiene Skill that removes cross-session memory labels, in-session residue, and defensive disclaimers, with optional compression rules for executive one-pagers; it ships install/scan scripts, so retain the original, manually review facts and tone, and do not replace final acceptance with automated cleanup.
- [WorkBuddy App Builder Skill](https://github.com/sharptoolbox/WorkBuddy-AppBuilderSkill) - An ontology-driven Skill for requirements discovery, human checkpoints, and local SQLite/API domain-app generation; review generated code and local API permissions before installation.
- [WorkBuddy Theme Skill](https://github.com/comeonzhj/WorkBuddy-theme-skill) - Creates, validates, previews, applies, and restores reversible runtime themes for WorkBuddy; it injects styles through local CDP and may restart the app and run a local guard, but does not modify app.asar, signatures, account data, or conversations, so review restart impact before use.
- [ZhiGui Second Brain Skill](https://github.com/CarlWangChina/zhigui-openclaw-ui-second-brain-skill) - A local MCP-backed planning and knowledge-graph workspace for WorkBuddy; it uses PolyForm Noncommercial 1.0.0 and reads/writes personal planning data, so review the license and permissions first.

### Tools and integrations

- [CLI2API](https://github.com/caigee-cmd/cli2api) - An MIT-licensed self-hosted local gateway that converts WorkBuddy (and Qoder/Trae) login state into OpenAI/Anthropic-compatible APIs with multi-account routing, isolated workers, Docker, and a loopback console; it defaults to `127.0.0.1` and requires an API key, but handles OAuth/PAT/credential imports, so protect exports, ports, and account-term boundaries and do not use it for shared resale.
- [WorkBuddy2API](https://github.com/ShouZhuo0413/codebuddy2api) - An MIT-licensed local protocol converter that exposes an already signed-in WorkBuddy/CodeBuddy session through OpenAI, Responses, and Anthropic-compatible APIs; it reads local auth state and forwards to `copilot.tencent.com`, so review source, credential files, exposed ports, and Tencent account terms first.
- [CodeBuddy2OpenAI](https://github.com/HanHan666666/codebuddy2openai) - An MIT-licensed single-file local protocol converter that wraps a signed-in CodeBuddy/WorkBuddy session as an OpenAI-compatible `/v1/chat/completions` endpoint, listening on `127.0.0.1` by default; it reads local auth state, refreshes tokens, and can log complete request/response bodies, and it does not work with the current Codex CLI, so review source, credential files, logs, exposed ports, and Tencent account terms first.
- [Buddy2api](https://github.com/wicm84266964/Buddy2api) - An MIT-licensed local multi-channel gateway that separately exposes WorkBuddy/CodeBuddy, QClaw, QwenWork, and TraeWork login states through OpenAI-compatible APIs, with Codex Responses, Docker, and API-key channel routing; upstream explicitly limits it to local use and says not to deploy publicly or share credentials, so review local auth files, the database, ports, and each provider's account terms first.
- [WorkBuddy CLIProxy provider](https://github.com/lovingfish/workbuddy-cliproxy) - An MIT-licensed CLIProxyAPI plugin that exposes CodeBuddy models to OpenAI/Anthropic clients with QR login and token refresh; credentials are stored in the local plugin directory and it includes upstream template-adaptation logic, so review source, account terms, and data flows before use.
- [WorkBuddy Remote](https://github.com/vergess3/workbuddy-remote) - Access a WorkBuddy instance from another device.
- [Skill Buddy](https://github.com/konnga/skill-buddy) - Manage, install, and synchronize Skills and MCP servers across AI Agents.
- [WorkBuddy for Obsidian](https://github.com/bigbay957-sudo/workbuddy-for-obsidian) - Use local WorkBuddy inside Obsidian with references, edits, and provenance.
- [Workbuddian](https://github.com/jiang198012/workbuddian) - An MIT-licensed Obsidian desktop plugin that brings local WorkBuddy/CodeBuddy CLI into a vault with streaming chat, `@` references, session forks, MCP management, per-action approval, and undoable edits; desktop-only on Windows/macOS, it can read the vault and run approved local commands/MCP servers, so review paths and permissions first.
- [Codex × WorkBuddy Token Monitor](https://github.com/tylerchen0123-sudo/CODEX-Inspection-Guidelines-for-Dosage) - An MIT-licensed local real-time Token dashboard with no third-party Python dependencies; it reads Codex and WorkBuddy session logs and uses SSE for usage, cache-hit, and active-session views. Local sessions may contain sensitive content, and derived values are not official billing records, so confirm scan scope and exposed ports first.
- [Tencent Meeting CLI](https://github.com/TencentCloud/tencentmeeting-cli) - Tencent's official CLI for meeting management and Agent integration.
- [DCC-MCP Agent Plugins](https://github.com/dcc-mcp/dcc-mcp-agent-plugins) - An MIT-licensed official-distribution suite of DCC-MCP Agent Skills and plugins compatible with WorkBuddy, Codex, Claude Code, and other hosts; it discovers digital-content tools and calls them within approval boundaries, but installation brings npm/plugin runtimes and local or external-tool permissions, so review provenance, credentials, file access, and network scope first.
- [SkillHive](https://github.com/tonycc/skillhive) - An MIT-licensed enterprise Skill hub that uses a WorkBuddy MCP connector for centralized distribution, versioning, review, feedback, and operation auditing, with auditable connector build and verification scripts; deployment requires PostgreSQL, administrator tokens, and an approved HTTPS enterprise MCP endpoint, while real-client compatibility and production approval still require human verification, and build artifacts or internal endpoints must not be exposed as public install links.
- [GitHub MCP Server Lite](https://github.com/1186247283zj-pixel/github-mcp-server-lite) - An MIT-licensed GitHub MCP server using only the Python standard library, with 24 tools for repositories, files, branches, issues, pull requests, search, and notifications; it helps WorkBuddy connect through a PAT when OAuth or npm paths fail, but configuration grants GitHub API access and `run_api` can reach arbitrary REST endpoints, so minimize token scopes, protect the token, and review every write/delete action.
- [BailingHub WorkBuddy Connector](https://github.com/bailinghub/bailinghub-workbuddy-connector) - An MIT-licensed independent WorkBuddy enterprise connector that uses browser PKCE authorization, capability checks, idempotent invocations, approvals, limits, and audit to query or operate connected business systems; real business endpoints, tenant authorization, and Client/Agent tokens remain deployment-owned, so verify the business authorization page, credential storage, capability revisions, and rollback path, and never distribute internal tokens or cookies.
- [DSH Reminder](https://github.com/Aisland-SJL/dsh-reminder) - An MIT-licensed DeepSeek Harness cross-window reminder plugin that notifies you when a task finishes or waits for human approval; it only reminds and never approves on your behalf, requires browser notification permission, and is a complementary tool for WorkBuddy/Codex-style agent workflows.
- [Devnors Data MCP](https://github.com/DevnorsAI/devnors-data-mcp) - Legal, company, content, and research data APIs for WorkBuddy; requires an external API key.
- [Beav](https://github.com/Jamailar/Beav) - A local-first workspace for creator research, assets, ideation, and production that connects to WorkBuddy through a user-scoped plugin and loopback MCP service. It uses a custom MIT-derived license that prohibits commercial use, production packages may lead the public source snapshot, and workflows can involve local workspaces, model credentials, browser/social content, and localhost services; verify versions, licensing, platform terms, and permission scope before installation.
- [wechat-openclaw-channel](https://github.com/HenryXiaoYang/wechat-openclaw-channel) - Routes WeChat messages to a local OpenClaw Agent through QClaw or WorkBuddy OAuth/Centrifuge mode. It stores WorkBuddy access and refresh tokens in `~/.openclaw/openclaw.json`, carries message content through Tencent endpoints, and has no LICENSE file despite MIT claims in its README/package metadata; protect the configuration and review source plus WeChat/Tencent account terms first.
- [DSH WorkBuddy Connect](https://github.com/corrinehu/dsh-workbuddy-connect) - Connects WorkBuddy desktop models to DeepSeek Harness across Web, Desktop, and TUI; it reads the local WorkBuddy sign-in file and stores refresh credentials in DSH's own directory, relies on unofficial endpoints, and should be reviewed against the source and account terms before installation.
- [DSH Memory Palace](https://github.com/lovezi0/dsh-memory-palace) - An MIT-licensed DeepSeek Harness memory plugin that bridges existing `.workbuddy/memory` directories, keeps editable Markdown memories/logs/summaries across sessions, and gates deletion behind confirmation; it reads and writes local memory, while smart summaries may call an LLM, so review directory scope, sensitive content, and network/cost boundaries first.
- [DSH Agent Selector](https://github.com/jiang12345-code/dsh-agent-selector) - An MIT-licensed DeepSeek Harness plugin that dispatches tasks to WorkBuddy built-in/custom models, Codex, or Claude and returns provenance receipts; its WorkBuddy channels read local model/session data, write the automations database, and depend on reverse-engineered scheduling behavior, so review credentials, task content, database backups, and account terms first.
- [Tonghuasun Agent](https://github.com/zhuyifang/tonghuasun-agent) - An AGPL-3.0 connector for the Tonghuashun Windows desktop client that exposes quotes, account, positions, and trade data to WorkBuddy and other Agents; its local API uses a token and optional trading tools, while the core unsigned Windows plugin is currently closed source, so verify binaries, privacy, brokerage permissions, and trade-confirmation safeguards before use.
- [DSH WorkBuddy Provider](https://github.com/Axiaohungry/dsh-llm-workbuddy) - Adds WorkBuddy China models to DeepSeek Harness with API-key and browser-token authentication; MIT licensed. The adapter stores credentials, opens a login page, and calls official `copilot.tencent.com` endpoints, but remains third-party software; review account terms and token storage before installation.
- [OpenWorkBuddy](https://github.com/CatCatUncle/openworkbuddy) - An open-source WorkBuddy-style local Agent workspace with Skills, MCP, desktop support, and multiple IM channels; licensed under PolyForm Noncommercial 1.0.0, with separate commercial licensing required. It can run Shell commands, control a browser, and connect external channels, so review permissions and data flows before use.
- [SailFish](https://github.com/ysyx2008/SailFish) - A WorkBuddy-style personal desktop secretary for macOS and Windows with memory, Skills, MCP, browser, terminal, and multi-IM channels; dual-licensed under AGPL v3 and a commercial license. Confirm licensing, credential handling, and local/remote-operation permissions before use.
- [OpenBuddy](https://github.com/opensymph/OpenBuddy) - An MIT-licensed Rust/Tauri WorkBuddy-style cross-platform desktop client with BYOK, multi-provider models, Skills, MCP, plan mode, sub-agents, and local automations; model credentials are stored in a local plain-text configuration file, so protect that file as documented upstream.
- [Agent Context Sync](https://github.com/westsource/agentctxsync) - Self-hosted session synchronization and backup across devices and Agents.

### Community clients and enhancements

- [WorkBuddy Auto Sign-in](https://github.com/88lin/workbuddy-auto-signin) - Dependency-free check-in and reward automation; it reads a local session token and uses reverse-engineered unofficial endpoints, so review the source and account terms first.
- [WorkDaddy](https://github.com/babygoton/WorkDaddy) - A desktop enhancement for backups, session migration, and long-running task support.
- [WorkBuddy Skin Studio](https://github.com/cdredfox/workbuddy-skin-studio) - A reversible theme manager for WorkBuddy Desktop.
- [WorkBuddy Dream Skin](https://github.com/zhouwei713/WorkBuddy-Dream-Skin) - An MIT-licensed, image-driven Windows theme system with presets, a tray controller, verification, and restore tooling. It restarts WorkBuddy with a loopback CDP port and runs unsigned PowerShell plus renderer injection, so save active work and review the scripts before enabling it.
- [M5Stack Toys / Core2 Buddy](https://github.com/sindney/m5stack_toys) - An MIT-licensed collection of M5Stack hardware projects; Core2 Buddy scans WorkBuddy tasks over USB serial, shows workspaces/tasks on a touchscreen, and announces status with TTS and LEDs. It requires Arduino, Python, serial access, and edge-tts, so confirm local WorkBuddy data scope, firmware-upload scripts, and external voice-service boundaries first.
- [LinkCode](https://github.com/arcboxlabs/linkcode) - An open desktop client supporting multiple coding Agents.
- [CodeDrobe Desktop](https://github.com/CodeDrobe/desktop) - An open-source, reversible theme manager for WorkBuddy and other AI desktop apps; review account, app-path, and download permissions before use.
- [WorkBuddy Switch](https://github.com/changexbc/workbuddy-switch) - A cross-platform WorkBuddy/CodeBuddy account switcher with usage visibility; it stores OAuth tokens, rewrites local auth files, and calls unofficial endpoints, so review the source and account terms first.
- [WorkBuddy Account Migrate](https://github.com/xiaoliuzhuan666/workbuddy-account-migrate) - Moves conversations, long-term memory, and MCP connectors after an account switch; MIT licensed, with backup, rollback, and post-migration verification. It rewrites SQLite `user_id` values and merges local data, so confirm the backup, source/target accounts, and data scope before running it.
- [Crew](https://github.com/shuishenghualalala/Ace) - An Apache-2.0 open-source WorkBuddy-style local multi-agent workbench with Desktop, Web, CLI, Skills, MCP, knowledge-base, task automation, and multi-agent collaboration; a source-preview release that can access local files and optionally control browsers, external channels, and user-provided models, so review security switches, API keys, account settings, and data boundaries before use.

### Benchmarks

- [workbuddy-bench](https://github.com/Tencent/workbuddy-bench) - Tencent's multi-domain coding-agent benchmark, tasks, and evaluation code.

See the automatically refreshed [ecosystem activity and star ranking](ECOSYSTEM.md).

## Skills, Prompts, and MCP

### Build and use Skills

- [Build a document review Skill](https://mp.weixin.qq.com/s/oFjSrlTp5VlMzPwN_iPOjg) - A complete document-review example.
- [WorkBuddy + Kingsoft Docs Skill](https://mp.weixin.qq.com/s/t2XuzNFmTWYBYMLhn762eQ) - Organize WeRead notes in Kingsoft Docs.
- [Eight prompts for internet teams](https://mp.weixin.qq.com/s/E1liM7qHAa-EbzVnmzYClA) - Prompt examples for product and operations work.

### Connect tools with MCP

- [Use an MCP server in WorkBuddy](https://developer.cloud.tencent.com/article/2698011) - MCP configuration and invocation tutorial.
- [WorkBuddy + Agent Mail](https://mp.weixin.qq.com/s/4sEZdOlEptsqbwmWSUplVQ) - An automated email-processing workflow.
- [WorkBuddy + Qichacha MCP](https://mp.weixin.qq.com/s/NRaiAMTHL6ckR9DGxUXPZA) - A company due-diligence workflow.

## Guides

### Articles

- [Six WorkBuddy tips](https://mp.weixin.qq.com/s/Gdax9JpvDnDrolXFkuG-Pw) - Quick tips for first-time users.
- [WorkBuddy from zero to productive](https://mp.weixin.qq.com/s/JZWIB3tKNdRKRiXx-87Bpg) - A Chinese getting-started tutorial.
- [Three-month field guide](https://mp.weixin.qq.com/s/Uq8v9KIw1QJchBIouNRCkA) - Long-term usage notes and workflows.
- [WorkBuddy beginner guide](https://mp.weixin.qq.com/s/Tiw2M-j05noSOS9rLbUiWg) - A beginner guide focused on Chinese office work.

### Videos

- [Why is WorkBuddy popular?](https://www.bilibili.com/video/BV1DK7K65Ex2/) - Product positioning and capability overview.
- [WorkBuddy in 35 minutes](https://www.bilibili.com/video/BV1j1JP6oEHA/) - A complete feature demonstration.
- [From beginner to advanced](https://www.bilibili.com/video/BV1ggKf6AEVY/) - A structured video tutorial.
- [Build Agent workflows by talking](https://www.bilibili.com/video/BV1ngJH6yEKH/) - A solo-company automation case study.

## Use Cases

### Knowledge management

- [WorkBuddy + IMA knowledge loop](https://mp.weixin.qq.com/s/A1RpRA240rOwqFYb8RUJmg) - A continuously maintained personal knowledge base.
- [WorkBuddy + Obsidian](https://mp.weixin.qq.com/s/VlcgqGtKt6OpESkvfBG0Zw) - Local notes and Agent collaboration.
- [CFA knowledge base](https://mp.weixin.qq.com/s/B-S2cXBtSFk15QwyOeK7iQ) - Retrieval over large professional textbooks.

### Documents, data, and professional work

- [File recognition and processing](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/File-Recognition) - Official workflow for batch renaming, meeting-note organization, and foreign-language video translation.
- [Google Calendar and Drive](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Google-Integration) - Connect Google services, describe the goal, and verify calendar or file results.
- [Build a local app without code](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Local-App) - Design, troubleshoot, and iteratively upgrade a local application with WorkBuddy.
- [Document generation and editing](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Document-Generation) - Official walkthrough for generating Word documents and creating presentations from source material and templates.
- [Data analysis and visualization](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Data-Analysis) - Official walkthrough for turning spreadsheets or collected data into charts and visual reports.
- [Create polished presentations](https://mp.weixin.qq.com/s/4v-aXrx3H3ndy0tobFJO2g) - Presentation generation and visual refinement.
- [Automated financial report analysis](https://mp.weixin.qq.com/s/QsiUU8aep-xDQpA4ikz_DA) - Analyze company reports in batches.
- [Build a 1,000-page bid](https://mp.weixin.qq.com/s/Ll6oP5J0rWhEmZ2pXdJOvw) - A long-document processing case study.
- [Commercial lawyer starter guide](https://mp.weixin.qq.com/s/9mvnhDRrkx_UO_yA94LwGw) - An introduction for legal work.
- [Organize local files](https://mp.weixin.qq.com/s/CmkC0VxwYjyK5MKTC-07MQ) - File classification and organization workflow.

### Education

- [Student learning analysis](https://mp.weixin.qq.com/s/KvPEcdJ2JUoH-F8R5E4Qww) - Process student learning data.
- [Ten classroom applications](https://mp.weixin.qq.com/s/7z_-x3Yk6fHkSMDd3NgqEQ) - A collection of teaching scenarios.
- [Personalized student diagnostics](https://mp.weixin.qq.com/s/mgLjBbcD-avXRiM9sxJn4w) - Generate individualized reports in batches.

### Content and career

- [Social-media operations](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Social-Media) - Official workflow for producing Xiaohongshu and video content.
- [AI content production pipeline](https://mp.weixin.qq.com/s/dSKr_a5lUYunDfS79oRzcA) - From topic selection through publishing.
- [Exam prep and job search](https://mp.weixin.qq.com/s/ldhLYboHnLiqrz12I5vW9Q) - Orchestrate study and job-search tasks.
- [Six time-consuming job-search tasks](https://mp.weixin.qq.com/s/mogl1CFtEEf9GCK2_BxbCg) - Practical job-search automation.

### Automation and Agent workflows

- [Automated daily briefing](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Daily-Briefing) - Connect QQ Mail, test a briefing, schedule daily delivery, and personalize the result.
- [AI self-directed execution](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/AI-Self-Driven) - Define an outcome, let WorkBuddy plan the steps, and require a self-check before delivery.

## Research and Engineering

- [Tencent WorkBuddy Bench](https://arxiv.org/abs/2607.20911) - A multi-domain coding-agent benchmark with a reproducible evaluation protocol.
- [WorkBuddy Bench website](https://workbuddybench.com/) - Official benchmark overview, tracks, results, and evaluation entry point.
- [WorkBuddy Bench dataset](https://huggingface.co/datasets/tencent/workbuddy-bench) - Official task archives for the Code, Web, Office, and Security subsets.
- [CloudBase model configuration](https://docs.cloudbase.net/ai/ai-tools/workbuddy) - Connect an OpenAI-compatible model endpoint.

## Related Lists

- [semlinker/awesome-workbuddy](https://github.com/semlinker/awesome-workbuddy) - A CC0 Chinese WorkBuddy resource list covering official material, practical cases, prompts, Skills, and MCP; complementary to this index, with each linked resource still requiring independent provenance and permission review.
- [staruhub/awesome-workbuddy](https://github.com/staruhub/awesome-workbuddy) - A Chinese-first index of Skills, prompts, tutorials, evaluations, and integrations.
- [awesome-workbuddy-skills](https://github.com/shuangying0001-beep/awesome-workbuddy-skills) - Skills for automation, data, browsers, WeChat, and content production.
- [awesome-workbuddy-use-cases](https://github.com/EvoLinkAI/awesome-workbuddy-use-cases) - A large use-case library organized by profession and task.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - A broad MCP server list; review each server separately before connecting it to WorkBuddy.
- [Awesome DeepSeek Harness Plugins](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) - A CC0 directory of installable DSH plugins, adjacent to WorkBuddy-style Skill and Agent workflows; it is not an official Tencent list, so review each plugin's source and permissions before installation.

## Selection Standard

**Relevance:** A resource must directly support, explain, or evaluate Tencent WorkBuddy rather than merely mention the term.

**Verifiability:** Official sources, open code, executable steps, tests, demonstrations, and clear inputs and outputs are preferred.

**Maintenance:** Recent commits, issue activity, archival status, and link health are checked. Stars are supporting evidence, not the selection rule.

**Safety and transparency:** Licenses, scripts, dependencies, permissions, credential handling, data flow, and commercial relationships matter.

**Distinct value:** Reposts, pure promotion, duplication, and resources without substantial detail are not accepted because of popularity alone.

Use the [Skill, MCP, and extension security checklist](SECURITY.md) before installing third-party code. Unreviewed discoveries remain in the [automated discovery queue](DISCOVERIES.md) instead of entering the main list automatically.

Want to build a Skill? See this repository's [original Skills and structural validator](skills/README.md).

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first. A strong entry:

1. is directly relevant to Tencent WorkBuddy and has a stable public link;
2. offers verifiable information, reproducible steps, or distinct practical value;
3. uses `Title - One-sentence value.` format in the most precise category; and
4. discloses payment, promotion, data collection, and high-risk permissions.

If this index saved you time, consider giving it a star. You can also [open an issue](https://github.com/sandbaseai/awesome-workbuddy/issues/new/choose) to nominate a resource you have verified. Start with the [bilingual welcome](https://github.com/sandbaseai/awesome-workbuddy/discussions/78), ask questions in [Q&A](https://github.com/sandbaseai/awesome-workbuddy/discussions/categories/q-a), and share workflows in [Show and tell](https://github.com/sandbaseai/awesome-workbuddy/discussions/categories/show-and-tell). Read the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## Acknowledgements

Initial discovery was informed by [semlinker/awesome-workbuddy](https://github.com/semlinker/awesome-workbuddy). Thanks to its maintainers and to every linked author. Copyright in linked resources remains with their respective owners.

This index is released under [CC0 1.0 Universal](LICENSE). Indexed resources retain their own licenses and terms.
