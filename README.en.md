![Awesome WorkBuddy - Skills, MCP, Workflows and Guides](assets/awesome-workbuddy-banner.webp)

# Awesome WorkBuddy

English · [简体中文](README.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Check links](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml/badge.svg)](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml) [![Latest release](https://img.shields.io/github/v/release/sandbaseai/awesome-workbuddy?label=latest%20release)](https://github.com/sandbaseai/awesome-workbuddy/releases/latest)

> A practical collection of Tencent WorkBuddy documentation, Skills, MCP integrations, and workflows.

WorkBuddy uses natural language to help with research, documents, data, design, and development. This list helps you find official guides and community resources quickly.

> [!IMPORTANT]
> This is an independent community index, not a Tencent publication. Before installing any third-party Skill, MCP server, connector, or enhancement, inspect its source, permissions, and data flow. Never upload secrets, personal data, or unredacted company material without an appropriate review.

## Start Here

- [Download WorkBuddy](https://www.workbuddy.ai/) · [Official quick start](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart)
- [One-minute chooser and quick start](START_HERE.en.md) - Start here if you are not sure what to use. 中文版：[START_HERE.md](START_HERE.md)
- [Search the resource directory](https://sandbaseai.github.io/awesome-workbuddy/) - Filter by keyword or category.

If this list helps you find something useful, consider giving it a [Star](https://github.com/sandbaseai/awesome-workbuddy). Found a missing resource or broken link? [Send feedback](https://github.com/sandbaseai/awesome-workbuddy/issues/new/choose).

<details>
<summary>More official entry points</summary>

- [Official documentation](https://www.workbuddy.ai/docs/zh/workbuddy/) - Product documentation and usage guides.
- [Install on macOS](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) - Requirements, installation, sign-in, and updates.
- [Install on Windows](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide) - Requirements, installation, sign-in, and updates.
- [Ten getting-started tips](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Efficient-Tips) - Clear tasks, iteration, backups, and context management.
- [Troubleshooting FAQ](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FAQ) - Installation, sign-in, integrations, and task recovery.
- [Changelog](https://www.workbuddy.ai/docs/zh/workbuddy/Changelog) - Capabilities, fixes, and compatibility changes.
- [Automation guide](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) - Create one-time or recurring tasks.
- [MCP guide](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) - Connect external tools and data.
- [WorkBuddy Enterprise quick start](https://cloud.tencent.com/document/product/1831/134527) - Create, test, and publish an enterprise Agent.

</details>

## Featured resources

If you are not sure where to begin, try these in order:

- [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) - A Chinese practical guide from the first task to team workflows.
- [Skill Onboarding](https://github.com/howoneai/skill-onboarding) - A 15-minute introduction to building and evaluating Skills.
- [Kunpeng Skill](https://github.com/hufeng173/kunpeng-skill) - Turn websites, code, images, and documents into reusable methods.
- [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) - Generate lessons, slides, quizzes, and interactive pages with multi-agent workflows.
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) - Team memory capabilities for WorkBuddy and other Agents.
- [AgentsView](https://github.com/kenn-io/agentsview) - Inspect and analyze Agent sessions locally.

The full catalog below is grouped into official resources, Skills, MCP, workflows, use cases, and research. For everyday browsing, use the [searchable directory](https://sandbaseai.github.io/awesome-workbuddy/).

<details>
<summary>Expand the full catalog</summary>

## Official Resources

### Core concepts

- [Create a task](https://www.workbuddy.ai/docs/zh/workbuddy/Create-Task) - Describe the goal, select a working directory, attach context, and start execution.
- [Task conversation](https://www.workbuddy.ai/docs/zh/workbuddy/Conversation) - Use interaction modes, send files and images, follow execution, interrupt, and continue.
- [Task management](https://www.workbuddy.ai/docs/zh/workbuddy/Task-Management) - Search, filter, inspect task states, organize workspaces, and resume existing tasks.
- [View results](https://www.workbuddy.ai/docs/zh/workbuddy/Results) - Inspect artifacts, table and document previews, web output, files, and changes.
- [Task bar and Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar) - Learn where to find, import, and create Skills.
- [Skills marketplace](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) - Browse, install, enable, and manage WorkBuddy Skills in one place.
- [Skills Marketplace quick start](https://open.workbuddy.cn/en/docs/skill) - Official instructions for opening the Skills Marketplace in WorkBuddy and browsing or installing Skills.
- [Create a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) - Turn a natural-language workflow into a reusable Skill.
- [Explore](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Explore) - Browse official creations across seven scenario categories, preload their Prompt, Skill, and Expert setup to make your own version, and understand how Explore differs from Skills and Experts.
- [Expert Center](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Expert-Center) - Choose a specialist with its own methods and tools, or a multi-Agent team whose lead delegates parallel work.
- [Assistant (remote tasks)](https://cloud.tencent.com/document/product/1831/134392) - Trigger WorkBuddy on a desktop from Weixin, WeCom, QQ, DingTalk, or Feishu
- [Two permission modes](https://cloud.tencent.com/document/product/1831/134401) - The official guide to default permissions, workspace boundaries, confirmation prompts, and Full Access
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
- [Lexiang knowledge base](https://cloud.tencent.com/document/product/1831/134398) - Authorize WorkBuddy to search and cite team-space content and save outputs back to Lexiang

### Community channels

- [WorkBuddy product page](https://cloud.tencent.com/product/workbuddy) - Tencent Cloud's product information and updates.
- [Tencent Cloud developer articles](https://cloud.tencent.com/developer/search/article-WorkBuddy) - Searchable community engineering articles.

## Open-source Ecosystem

> [!NOTE]
> “Works with WorkBuddy” does not mean “endorsed by Tencent.” Check licenses, account terms, permissions, and credentials before using unofficial automation or API tooling.

### Learning and reference

- [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) - An MIT-licensed practical handbook with 2,807 stars and 397 forks, organized from completing a first task to building a reusable team system across installation, Skills, connectors, APIs, automation, knowledge management, professional diagnosis, and multi-Agent cases
- [AI CLI Kickstarter](https://github.com/xiaolai/ai-cli-kickstarter) - An MIT-licensed bilingual beginner launcher and prompt library for macOS, Linux, and Windows, supporting Qwen Code, Kimi Code, and CodeBuddy CLI. Its state machine covers environment probing, pre-install confirmation, and verification, making it useful for first-time WorkBuddy/CodeBuddy CLI setup. After confirmation, the launcher downloads and directly executes provider scripts from fixed official domains, so verify each URL, inspect the script, and review provider terms before running it on a privileged or sensitive machine.
- [How to Use Agent](https://github.com/Lukanytsu7551/how-to-use-agent-guide) - An MIT-licensed Chinese tutorial site with a 27-chapter WorkBuddy manual, 100-case library, and Codex/Agent learning paths, plus a provenance NOTICE and security policy. Some Agent Guide adaptations use CC BY-NC-SA 4.0, the repository includes substantial media, and its AI News build calls an external public API
- [Agent Learning Guide](https://github.com/tangshiyegit/agent-guide) - A MIT-licensed guide with 19 WorkBuddy tutorials and 12 office, content, and automation case studies
- [Skill Onboarding](https://github.com/howoneai/skill-onboarding) - An Apache-2.0 15-minute hands-on guide to building Skills through creation, evaluation, iteration, and benchmark stages, with an explicit CodeBuddy installation path at `~/.codebuddy/skills/`
- [AI Coding Guide Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh) - A Chinese learning path for AI coding tools and office Agents, including WorkBuddy.
- [AgenticMetaEngineering](https://github.com/AiToByte/AgenticMetaEngineering) - An MIT-licensed team AI-context engineering template that version-controls `AGENTS.md`, `context/`, requirements, and `.codebuddy/commands/`, while using branches and independent checkouts to isolate parallel tasks. It needs no vector database or external service and is useful for turning WorkBuddy/CodeBuddy team rules and lessons into reviewable shared assets. Shared repositories can contain business knowledge, paths, or internal rules, so redact sensitive material, restrict repository access, and agree on the branch policy first.
- [Superpowers Chinese Adapters](https://github.com/squallopen/superpowers-zh-adapters) - An MIT-licensed Chinese adaptation layer for `obra/superpowers` with explicit CodeBuddy, Codex, Claude Code, Cline, Droid, OpenCode, and ZCode support, Chinese triggers and document output, install/update/rollback scripts, and upstream version refreshes. The CodeBuddy adapter updates a dedicated rules block
- [learn-workbuddy](https://github.com/adongwanai/learn-workbuddy) - A 24-chapter Python tutorial that builds a WorkBuddy-style desktop Agent from scratch.
- [ZZZ Plain-language AI Guide](https://github.com/mfkyddh/ZZZ-Simple-AI) - A license-not-declared beginner guide created primarily with WorkBuddy, organized into nine core chapters and 30 extensions on LLMs, Agents, context, memory, MCP, Skills, multi-Agent systems, and AI coding workflows
- [WorkBuddy Harness Bluebook](https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness) - Explains prompts, memory, plugins, experts, Skills, and safety boundaries.
- [WorkBuddy Harness](https://github.com/zhuang-HE/workbuddy-harness) - A license-not-declared nine-dimension infrastructure framework for WorkBuddy-style Agents, with 11 plugins, 21 Hooks, Hook/evaluation runtimes, a daemon, and 30 benchmark cases
- [LoopForge](https://github.com/Tencent/LoopForge) - Tencent's MIT-licensed multi-agent software-delivery workflow for requirement clarification, boundary confirmation, design, implementation, independent review, testing, and resumable handoff, with CLI/Skill installation for CodeBuddy, Codex, Cursor, and Claude Code
- [AI Project Workflow](https://github.com/AlanHuang168/AI-Project-Workflow) - An MIT-licensed cross-agent software-delivery workflow with explicit CodeBuddy support, a single source of truth, stage Skill contracts, state files, artifact gates, real verification, and CLI adapters
- [Undergraduate Thesis AI Workflow](https://github.com/Sqhao-O/undergraduate-thesis-ai-workflow) - A MIT-licensed six-part workflow guide covering Claude Code, Kimi, CC Switch, Pandoc, Lark-Formatter, and WorkBuddy formatting for undergraduate theses
- [LazyBuddy](https://github.com/elvinzhao10/LazyBuddy) - An MIT-licensed self-contained workflow harness for WorkBuddy/CodeBuddy CLI and IDE with staged planning, host-readiness verification, reversible offboarding, MCP/Skill routes, and layered tests
- [Define Product and Roadmap](https://github.com/bangogo/define-product-and-roadmap) - An MIT-licensed product-contract Skill for WorkBuddy, CodeBuddy, and Codex that aligns PRDs and experience roadmaps around evidence, user value, truth boundaries, assumptions, and acceptance criteria, with versioned templates, deterministic validators, evaluation fixtures, and tests

### Skill collections

- [oh-my-workbuddy](https://github.com/mrzhangguoguo/oh-my-workbuddy) - An MIT-licensed WorkBuddy Skill pack with 46 catalog-driven Skills, user/project-scoped installation, bilingual docs, and zero runtime dependencies
- [WorkBuddy Skills Collection](https://github.com/yinqd3/workbuddy-skills) - An MIT-licensed collection of seven WorkBuddy Skills covering academic research, frontend slides, knowledge-base linting, macOS maintenance, PPTX generation, engineering methodology, and tool-call repair
- [WorkBuddy Skills (ai3027)](https://github.com/ai3027/workbuddy-skills) - An MIT-licensed WorkBuddy Skill collection with workspace migration/cleanup and technical WeChat writing Skills, each documented with a `SKILL.md` and scripts
- [WorkBuddy AI Agent Skills Collection](https://github.com/Tugoukezhang/workbuddy-skills) - A collection of 78 WorkBuddy Skills spanning games, frontend, backend, documents, AI creation, Tencent/WeChat, and Agent tooling
- [Ontology-Driven AI Data Management Skills](https://github.com/SuperChason/ontology-driven-ai-data-management-skills) - An MIT-licensed set of 25 enterprise ontology and AI data-management Skills with explicit WorkBuddy support, WorkBuddy ZIPs, install scripts, version metadata, a NOTICE, and validation workflow
- [Zhijian Skills](https://github.com/zjp1997720/zhijian-skills) - An MIT-licensed portfolio of 19 Agent Skills with standard npx installation, per-Skill documentation, versions, and validation metadata, including a WorkBuddy-specific CLI model bridge
- [WorkBuddy Wiki](https://github.com/YuanYiZheXue/workbuddy-wiki) - An Apache-2.0 WorkBuddy + Obsidian local knowledge-base system with versioned schemas, cross-workspace synchronization, source/concept/entity organization, and health diagnostics
- [WeChat Mini Program Virtual Payment Skill](https://github.com/beeyang0/miniprogram-VirtualPayment) - An MIT-licensed documentation-only Skill covering virtual goods, coin top-ups, iOS routing, signing, idempotent callbacks, error diagnosis, and launch checklists. It is primarily written in the Claude Code Skill format but can serve as CodeBuddy reference material

- [WorkBuddy Skill Hub](https://github.com/sandbaseai/workbuddy-skill) - A searchable catalog of 10,000 public Skill paths with provenance, license, security, and compatibility review fields.
- [Agency Agents 中文版](https://github.com/jnMetaCode/agency-agents-zh) - An MIT-licensed Chinese community collection of 276 role-oriented experts across 20 departments, with explicit conversion and installation support for WorkBuddy's `~/.workbuddy/skills/` directory
- [Senmu BuildOS](https://github.com/SenMuShare/senmu-buildos) - An Apache-2.0 cross-tool Agent engineering coach and Skill collection with explicit WorkBuddy support, covering requirements, design, implementation, testing, Git, releases, evidence, and rollback
- [i18n Helper Skills](https://github.com/liangdabiao/i18n-helper-skills) - A license-not-declared internationalization Skill collection for WorkBuddy/Codex and other Agents, with complementary workflows for static HTML language directories and translation functions in React/Vue/PHP/Python/Java source, plus extraction, application, and completeness-check scripts
- [PMCockpit](https://github.com/wsdlp46/PMCockpit) - An Apache-2.0 AI product-management cockpit for WorkBuddy, Codex, and Claude that turns requirements, specs, prototypes, reviews, retrospectives, and lessons into eight executable Skills
- [QingFeng Skills](https://github.com/chenwg001/qingfengskill) - An MIT-licensed WorkBuddy-first collection of 17 Skills for education and content work, covering writing, PPTs, image/video production, and platform draft publishing, with per-directory installation
- [Image Skill](https://github.com/Mariposa-FLOA/image-skill) - A collection of 17 visual Skills for WorkBuddy, Codex, and compatible Agents covering poster art direction, image workflows, page-flip showcases, and layered PSD export, with bilingual usage documentation and per-asset provenance
- [workbuddyskills](https://github.com/infometa/workbuddyskills) - An offline archive of WorkBuddy Skills, connectors, and experts.
- [Doubao / WorkBuddy / QwenWork Skills Archive](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills) - A license-not-declared, script-synchronized archive of multi-platform Skills, experts, and connectors whose WorkBuddy directory currently contains about 500 entries and 15,245 files with scenario navigation
- [WorkBuddy Skill Groups](https://github.com/darker2016/workbuddy-skill-groups) - An MIT-licensed, provenance-disclosed collection of 39 WorkBuddy expert-team Skill packages spanning investment research, content, engineering, legal, tax, data, sales, and HR
- [WorkBuddy Experts](https://github.com/vbarter/workbuddy-experts) - A prompt-engineering study archive with 246 WorkBuddy 4.22.16 expert prompts, seven Nunjucks system templates, two built-in Skills, and a client reverse-engineering report. The repository states that MIT covers only its curation/index/report, while expert bodies and Tencent-customized templates remain under upstream and Tencent copyright
- [Unified Legal AI CN](https://github.com/laubeing-droid/unified-legal-ai-cn) - An MIT-licensed China-law assistance workspace built primarily for WorkBuddy, with five core Agents, 17 legal tools, nine domain applications, evidence/legal guardrails, document output, and an optional MCP reasoning engine across the litigation lifecycle
- [Five-layer Memory System](https://github.com/juventini10/Five-layer-memory-system) - An MIT-licensed five-layer long-term-memory Skill for WorkBuddy that uses 33 onboarding questions to capture preferences, trade-offs, and behavior patterns in maintainable memory layers
- [Personal User Manual Skill](https://github.com/NI9N/gerenshiyongshuomingshu) - An MIT-licensed, zero-dependency WorkBuddy Skill that uses a multi-turn self-discovery coaching process to organize values, strengths, and interests, challenge the result, and produce a maintainable Markdown personal manual
- [Web Security Test Rules](https://github.com/mowenQWQ/Web-Security-Test-Rules) - An MIT-licensed bilingual CodeBuddy/WorkBuddy web-security-testing Skill with authorization allowlists, expiry/signature gates, non-destructive checks, evidence records, and review intervals
- [AI HR Department](https://github.com/GiaSip/ai-hr) - An MIT-licensed Chinese WorkBuddy Skill whose read-only Python collector emits only directory statistics, extensions, and fixed enum keys—never filenames, contents, or network requests—before generating a shareable profile card
- [Website Prompts and Skills](https://github.com/TencentEdgeOne/awesome-website-prompts-and-skills) - Website-generation prompts, Skills, and challenge entries maintained by Tencent EdgeOne.
- [Ray Skills](https://github.com/imraywang/rayskills) - Executable, verifiable, and recoverable workflows for content production and publishing.
- [WorkBuddy Skills](https://github.com/bitcjm/workbuddy-skills) - Skills for writing, programming, office work, and general utilities.
- [Zotero MCP WorkBuddy Guide](https://github.com/maciechen/zotero-mcp-workbuddy-guide) - A Chinese guide with no repository license declared, connecting Zotero libraries to WorkBuddy through local, cloud, and hybrid modes with MCP templates and environment checks
- [WorkBuddy MCP OAuth Guide](https://github.com/normalpeople553/workbuddy-mcp-oauth-guide) - An MIT-licensed guide to troubleshooting and launching remote MCP OAuth 2.1/PKCE with WorkBuddy, including dynamic client registration, redirect-URI allowlists, authorization checks, redacted examples, and unit tests
- [DSH Skill Picker](https://github.com/a735624258/dsh-skill-picker) - Adds searchable, pinyin-aware, keyboard-friendly skill picking to the DeepSeek Harness Web GUI, reproducing WorkBuddy-style `/skill-name` invocation
- [Kunpeng Skill](https://github.com/hufeng173/kunpeng-skill) - An Apache-2.0 multi-source distillation Skill for WorkBuddy, Codex, Claude Code, and other Agents. It turns repositories, websites, UI, images, audio/video, and documents into evidence-backed reusable methods and generation specifications
- [Skill Doctor](https://github.com/evilstar2016/skill-doctor) - A local MIT-licensed CLI for auditing Skill conflicts, duplicates, security risks, and context cost across WorkBuddy and other Agents. It reads local resources by default and binds its UI to loopback
- [WorkBuddy Usage Status](https://github.com/clancy-feng/workbuddy-usage-status) - Turns WorkBuddy's local data into an offline, auditable dashboard for token/credit usage, model efficiency, and errors
- [Agent Analytics Report](https://github.com/Elisabeth15501/agent-analytics-report) - An MIT-licensed, WorkBuddy-first usage-analysis Skill that reads local session/usage data to produce token, cache, model-cost, and anomaly reports in Markdown, HTML, or JSON, with 306 synthetic-fixture tests
- [UsageMonitor WorkBuddy Provider](https://github.com/masclown/usage-monitor-plugin-workbuddy) - An Apache-2.0 independently versioned UsageMonitor provider that reads WorkBuddy subscription quotas, gift packages, and request history with model, channel, and operation slicing
- [Session Digger](https://github.com/taxueseek/session-digger) - An ISC-licensed cross-agent session search and knowledge-management toolkit that natively parses `~/.workbuddy/projects`, builds an incremental SQLite FTS index, and produces self-contained local reports
- [memU](https://github.com/NevaMind-AI/memU) - An Apache-2.0 cross-agent personal-memory system with direct WorkBuddy support that distills reusable Skills from sessions and tool calls, then uses a local sidecar for memory injection and retrieval
- [SmileX AI Universal Memory](https://github.com/smileluck/SmileX-AI-Universal-Memory) - An MIT-licensed local-first cross-agent memory store with an MCP server and read-only Web panel, plus manual WorkBuddy connection guidance

### Ready-to-use Skills

- [Skill Integrator](https://github.com/smiling66652/skill-integrator) - An MIT-licensed WorkBuddy meta-Skill for scanning, comparing, integrating, and optimizing multiple Skills, with on-demand loading and fallback methods
- [One-person Company](https://github.com/wzx11223344/one-person-company) - An MIT-licensed WorkBuddy Skill for one-person company operations across content, operations, product, finance, and growth automation
- [WorkBuddy Theme Manager](https://github.com/codexthemes/skills/tree/main/skills/workbuddy-theme-manager) - An Apache-2.0 WorkBuddy theme Skill that converts `.codex-theme` packages to `.workbuddy-theme` and supports installation, switching, and restoration
- [Academic Research Skills for WorkBuddy](https://github.com/jinmao-lin/academic-research-skills-workbuddy) - A CC BY-NC 4.0 academic-research Skill suite covering deep research, paper writing, manuscript review, research pipelines, and experiment planning, with attribution information included
- [OpenMobius Skill](https://github.com/MobiusQuant/OpenMobius-skill) - An Apache-2.0 trading-knowledge Skill with explicit WorkBuddy support, attributable ICT/SMC knowledge cards, market analysis, and chart generation, with unsupported routes stopping explicitly
- [Nuwa Skill](https://github.com/alchaincyf/nuwa-skill) - An MIT-licensed cross-agent thought-distillation Skill with explicit WorkBuddy support, turning public material into reusable analysis and expression frameworks
- [Narrator AI CLI Skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) - An MIT-licensed video-narration Skill compatible with WorkBuddy, covering material search, scripting, voice, BGM, and video composition
- [Superpowers WorkBuddy](https://github.com/ToussaintKnight/superpowers-workbuddy) - An MIT-licensed WorkBuddy testing and debugging methodology with four Skills and a reported 19/19 experiment suite, useful for bringing tests, diagnosis, and result verification into task workflows
- [WorkBuddy Runbook](https://github.com/maning636/workbuddy-runbook) - An MIT-licensed workflow Skill that turns multi-step work into runbooks with objectives, expected output, verification, fallback, and definition-of-done sections
- [Minecraft Mod Search](https://github.com/MasterHesse/minecraft-mod-search) - An MIT-licensed Minecraft Java mod search Skill with a `SKILL.md` and search scripts, with explicit installation paths for WorkBuddy/CodeBuddy
- [Workplace Communication](https://github.com/wanghoween-design/gaoqingshang-skill) - An MIT-licensed WorkBuddy workplace-communication Skill covering 23 common scenarios and helping draft clear, tactful responses
- [WeChat 4.x Decrypt Skill](https://github.com/xscanzm/wechat-4x-decrypt) - An MIT-licensed Windows-only WorkBuddy Skill for decrypting and searching local Weixin 4.x chat databases, with timestamped digests and structured exports
- [CareerStar](https://github.com/HanGu007/workbuddy-career-skills) - An MIT-licensed WorkBuddy career expert package for resume diagnosis and rewriting, interview coaching, company research, HTML resumes, and application tracking

- [WorkBuddy Skin Skill](https://github.com/zhangxiaoqiang1991/workbuddy-skin-skill) - An MIT-licensed downloadable WorkBuddy Skill supporting local reference-image analysis, private theme generation, ten built-in skins, screenshot verification, and failure recovery
- [open-kimi-ppt Skill](https://github.com/jinwyp/open-ppt-skill) - An MIT-licensed PPT Skill explicitly supporting WorkBuddy, installable with npx and able to produce editable PPTD projects and PPTX files with a local browser editor
- [MiniWorkBuddy](https://github.com/joezxh/mini-workbuddy) - An MIT-licensed open-source AI workbench inspired by Tencent WorkBuddy, built on AgentScope with multi-agent teams, Skills, deep research, scheduling, MCP, knowledge-base/ontology workflows, and text/voice interfaces
- [Design Workflow](https://github.com/yang20040317-svg/design-workflow) - An MIT-licensed WorkBuddy/Claude Code-format design workflow Skill organized around five layers and reusable modules, with subskills for charts, frontend, icons, mobile, motion, references, typography, and more

- [Majia Huiyuan](https://github.com/maojiebc/majia-huiyuan) - An MIT-licensed membership-operations and data-system Skill with a WorkBuddy single-expert package, 55 simulated logical datasets, 25 ETL flows, 12 role-oriented dashboards, and RFM, retention, coupon-effectiveness, and data-quality references
- [Pandadata API Skill](https://github.com/quantskills/skill-pandadata-api) - A GPL-3.0 installable financial-data Skill for WorkBuddy/Codex with local documentation for 218 APIs, search tooling, a compatibility index, and optional live calls
- [Photo to Monthly Zine Postcard](https://github.com/shenchangyi/photo-to-monthly-zine-postcard) - An MIT-licensed, directly installable WorkBuddy/Codex Skill that turns a user photo into a 3:4 monthly Zine postcard and requires verified, image-matched literature and music sources
- [XHS Blogger Analyzer](https://github.com/arraycto/xhs-blogger-analyzer) - An MIT-licensed WorkBuddy/Claude Skill that uses MCP to collect public Xiaohongshu creator content and generate content-strategy, topic, and structured-analysis documents
- [AI 10x Learning](https://github.com/luozhilzh/ai-10x-learning) - An MIT-licensed ten-step learning-loop Skill compatible with WorkBuddy, Codex, Claude, and Cursor, combining multi-perspective research, retrieval practice, Feynman explanation, and HTML learning cards
- [Book Video Generator](https://github.com/chenjun198711/book-video-generator) - An MIT-licensed book-video Skill compatible with WorkBuddy, Codex, Claude, and other Agents, covering book research, scripts, storyboards, AI images, TTS, subtitles, and ffmpeg MP4 composition
- [OpenMAIC Skill](https://github.com/THU-MAIC/OpenMAIC) - An MIT-licensed standard `SKILL.md` classroom workbench with direct WorkBuddy support, generating multi-agent lessons, slides, quizzes, interactive HTML, PBL activities, and TTS from topics or documents in hosted or self-hosted mode
- [WeChat Article Skills](https://github.com/aiworkskills/wechat-article-skills) - Apache-2.0 Skills compatible with WorkBuddy for WeChat Official Account operations, covering topic selection, writing, review, layout, images, and draft publishing, with a WorkBuddy integration guide
- [Eagle Untagged Organizer](https://github.com/ChosenXu/eagle-untagged-organizer) - An MIT-licensed WorkBuddy Skill that batch-organizes untagged design assets in Eagle through Eagle MCP, with multilingual names, structured annotations, tags, dry-run approval, snapshots, and restore
- [Rainskills](https://github.com/goodrain/rainskills) - An Apache-2.0 cross-agent Skill collection with explicit WorkBuddy support for project detection, deployment, troubleshooting, delivery verification, version management, and rollback
- [AI Operating Protocol](https://github.com/nehemc2026/ai-operating-protocol) - An MIT-licensed, zero-dependency WorkBuddy behavior protocol using six laws, leverage-based risk grading, and a Stop Rule to separate discussion, execution, and stopping
- [Xuanlan Governance Kit](https://github.com/jackyjinggit/xuanlan-governance-kit) - An Apache-2.0 WorkBuddy planning Agent and architecture-compliance toolkit with a self-contained Agent, cross-runtime converter, and checks for PII, de-identification leaks, and source-pointer drift
- [MaZhu](https://github.com/kcylp/mazhu) - An Apache-2.0 offline tool for preparing software-copyright-registration materials, with a desktop app, CLI, and WorkBuddy Skill that reads local projects and validates generated source-program and manual documents
- [CodeDrobe Skills](https://github.com/CodeDrobe/skills) - Apache-2.0 installable theme Skills with explicit Tencent WorkBuddy support for creating, applying, verifying, repairing, restoring, and publishing reversible themes
- [Data Analysis Skills](https://github.com/cabbage2000-lab/data-analysis-skills) - An MIT-licensed multi-host data-analysis Skill with documented WorkBuddy adaptation and testing. It turns CSV, Excel, JSON, and TSV files into insight-led single-file HTML reports with industry templates, evaluations, and tests
- [Graphic Design Guide](https://github.com/genapohub/graphic-design-guide) - An MIT-licensed WorkBuddy/CodeBuddy graphic-design Skill that routes brand, marketing, single-asset, rebrand, and style-exploration work into color, typography, logo, asset, and rights-review deliverables
- [QA Testing Guide](https://github.com/genapohub/qa-testing-guide) - An MIT-licensed WorkBuddy/CodeBuddy QA Skill covering test foundations, functional testing, automation, performance, defect management, and technical research with scenario-specific templates
- [DevOps Guide](https://github.com/genapohub/devops-guide) - An MIT-licensed WorkBuddy/CodeBuddy DevOps Skill covering CI/CD, Kubernetes, observability, logs, disaster recovery, migrations, and incident repair
- [Frontend Development Guide](https://github.com/genapohub/frontend-dev-guide) - An MIT-licensed WorkBuddy/CodeBuddy frontend-engineering Skill that generates architecture, component, performance, testing, and technical-research plans by scenario
- [Growth Guide](https://github.com/genapohub/growth-guide) - An MIT-licensed WorkBuddy/CodeBuddy growth Skill covering growth models, acquisition matrices, experiments, retention, and channel ROI
- [Monetization Guide](https://github.com/genapohub/monetization-guide) - An MIT-licensed WorkBuddy/CodeBuddy monetization Skill covering business models, pricing, sales funnels, customer success, and financial forecasts
- [Release Skill](https://github.com/ifoohoo/release-skill) - An Apache-2.0 auditable release Skill explicitly supporting WorkBuddy, Codex, CodeBuddy, and Kimi Code, with frozen plans, checks, approvals, publishing, consumer-install verification, and GitHub/npm/plugin distribution workflows
- [Hotspot Monitor Skill](https://github.com/jiangxu1024/hotspot-monitor-skill) - An MIT-licensed WorkBuddy trend-monitoring Skill that collects several Chinese platforms, filters by keywords, and schedules Feishu Base writes and mobile notifications
- [Bazi-Ziwei Skill](https://github.com/mingze21/bazi-ziwei-skill) - An MIT-licensed Bazi and Ziwei-doushu Skill compatible with WorkBuddy, Codex, Claude, and Cursor, using local chart algorithms, prompts, and shareable HTML posters with a test guide and synthetic examples
- [Prompt Toolkit](https://github.com/xiaolouJB/prompt-toolkit) - A CC BY-NC 4.0 multi-agent distribution package with 12 general-purpose prompts, including native WorkBuddy Skills and adaptations for Claude Code, Cursor, Trae, and CodeBuddy, covering questioning, learning, fact-checking, decisions, and life design
- [Paper CN Reader](https://github.com/langlibai66/paper-cn-reader) - An MIT-licensed academic-paper reading, translation, and annotation Skill for WorkBuddy that preserves PDF figures, tables, and formulas while producing HTML/PDF
- [Translate Book Windows](https://github.com/NikoKennedy/translate-book-windows) - An MIT-licensed WorkBuddy book-translation Skill with upstream attribution that processes PDF/DOCX/EPUB in chunks, maintains a glossary, validates manifest/hash integrity, supports resumable runs, and exports HTML/DOCX/EPUB/PDF
- [BossMate](https://github.com/yinren112/bossmate) - An MIT-licensed local job-search Skill for WorkBuddy that reads complete JDs in a visible browser, deduplicates opportunities, and gates messages before sending
- [Career Copilot](https://github.com/ronineymessjr-sudo/career-copilot) - An MIT-licensed, evidence-driven career workspace with native WorkBuddy Expert and MCP support for job search, JD analysis, profiles, resume generation, application tracking, and interview review
- [AIChuangpin Product Creator](https://github.com/zhangx1234994/aicp-product-creator-skill) - An MIT-licensed product-design workflow with WorkBuddy Skill/plugin packages and MCP configuration that matches images or ideas to live products, previews them, and returns a quote, with explicit user confirmation before credits are charged and a short-lived checkout link opened
- [IELTS Buddy Agent Skills](https://github.com/Jobo16/ielts-buddy) - An MIT-licensed IELTS learning Skill collection for WorkBuddy covering study plans, writing/speaking/reading/listening review, vocabulary, and mock exams, with installation and validation scripts
- [PDF Structured Extractor](https://github.com/ttww1111/pdf-structured-extractor) - An MIT-licensed PDF-extraction Skill compatible with WorkBuddy, Codex, and Claude
- [Roundtable KG](https://github.com/xiewende424/roundtable-kg) - An MIT-licensed, WorkBuddy-compatible offline roundtable Skill that debates serious questions through position-based personas and renders argument relations as an interactive force-directed graph
- [AI Weekly Report](https://github.com/Elisabeth15501/ai-weekly) - An MIT-licensed AI-industry weekly-report Skill compatible with WorkBuddy, Codex, and other Agents. It builds a searchable, filterable, dark-mode single-file HTML report from RSS and optional search data, preserving source links and fallbacks
- [AI Short Drama Skills](https://github.com/zkhyww/ai-short-drama-skills) - An MIT-licensed pair of Skills for WorkBuddy and other Agents that separates short-drama development and production across topic, script, table read, storyboards, assets, sound, editing, and QC, with deterministic preflight and distinct master/submission documents
- [Open Film Skills](https://github.com/62656456/ai-film-skills) - An Apache-2.0 multi-host collection of standalone Skills for story, directing, storyboards, visual assets, AI-video production, web design, and source-backed media research
- [Infoseek](https://github.com/GYINT/infoseek) - An MIT-licensed end-to-end research MCP/Skill compatible with WorkBuddy, combining multi-source discovery, four-level fetching, four-dimensional scoring, cross-source contradiction detection, structured reports, and long-term archiving with regression tests and key management
- [MarkItDown Skill](https://github.com/stwhwing/markitdown-skill) - An MIT-licensed WorkBuddy-compatible document and web-to-Markdown Skill built on Microsoft's MarkItDown, adding SPA/web fallbacks, batch conversion, and a local token estimator
- [Bilibili Video Summary](https://github.com/Willson-Huang/bilibili-video-summary) - An MIT-licensed local video-knowledge Skill with a WorkBuddy edition that uses subtitles or local Whisper transcription to produce 14-section Markdown notes with timestamps, entity tables, and claims-to-verify
- [Knowledge Base Builder](https://github.com/miaqu766520-a11y/kb-builder) - An MIT-licensed local knowledge-base setup Skill tested on WorkBuddy that interviews the user to create folders, templates, personal archives, and a manual, writing files only after the user approves the plan
- [AI Finance Workbench](https://github.com/feng-liu-1994/workbuddy-finance-workbench) - An MIT-licensed visual finance workbench with a WorkBuddy MCP App, 20 modules, and 25 workflows that specify fields, trial runs, checks, human review, exception ownership, and local backups
- [Universal Travel Planner](https://github.com/chaoliuzhu65-tech/universal-travel-planner-skill) - An MIT-licensed, 13-star WorkBuddy business-travel Skill combining 12306, flights, maps/weather, hotel comparison, budget tiers, packing lists, and responsive HTML itineraries with real outbound links
- [Travel Planner Skill](https://github.com/ycyliu/travel-planner-skill) - An MIT-licensed Skill directly compatible with WorkBuddy and CodeBuddy that confirms requirements, researches external sources with optional Xiaohongshu MCP, and generates responsive HTML itineraries and three budget tiers
- [1688 Product Reader](https://github.com/yyc424666lvy/1688-product-reader) - An MIT-licensed, read-only WorkBuddy Skill for extracting product title, price, MOQ, seller, SKU, images, and specifications from logged-in 1688 pages
- [A-share Watch Copilot](https://github.com/WaterCMY/A-share-watch-copilot) - A WorkBuddy Skill for A-share/Hong Kong market monitoring with position and fund schemas, eight automation templates, reports, and an optional local dashboard
- [Math Concept Film](https://github.com/liangdabiao/math-concept-film) - A license-not-declared mathematics short-film Skill compatible with WorkBuddy, Codex, and Claude, using a voice-first caption timeline to drive Manim animation with a six-act teaching framework, still-frame checks, and ffmpeg composition
- [Session Fork](https://github.com/yamingmou/session-fork-core) - An MIT-licensed WorkBuddy Skill that copies a conversation into an independent branch by the prior output, request ID, or text match, with dry-run preview, automatic backup, and branch lineage
- [Cross-Device Sync for WorkBuddy](https://github.com/jamesting-eng/workbuddy-skills) - An MIT-licensed Windows Skill for cross-device task continuity that uses a WPS cloud-drive Junction as the primary channel, HANDOFF/memory files as a transit channel, and a daemon/watchdog for ongoing sync


- [WorkBuddy Guide](https://github.com/Neo5093/workbuddy-guide) - An installable WorkBuddy usage and troubleshooting Skill covering connectors, experts, automations, memory, interaction modes, and FAQs
- [R Package Development Skills for CodeBuddy](https://github.com/shajoezhu/skills_codebuddy_rpackagedev) - An Apache-2.0 collection of five Skills for Claude Code and CodeBuddy Code covering R-package scaffolding, quality, `R CMD check`, CI gates, collaboration, and releases
- [DSH CodeBuddy Plugin](https://github.com/taikaikaikai-pixel/dsh-codebuddy-plugin) - An MIT-licensed DeepSeek Harness plugin offering 18 CodeBuddy models, search/web fetch, image generation, OAuth/API-key login, usage accounting, and a loopback-only streaming bridge
- [Kindle2WorkBuddy](https://github.com/MWang-TS/kindle2workbuddy) - An MIT-licensed Kindle e-ink WorkBuddy dashboard with a `SKILL.md`
- [Codex WorkBuddy Desktop Bridge](https://github.com/gosick233-cloud/Codex-WorkBuddy-Desktop-Bridge) - An MIT-licensed local MCP bridge that exposes a running WorkBuddy desktop agent as a Codex sub-agent, with web search, S1/S2/S3 code/dependency reviews, cancellation, and review-session reuse. It discovers sidecar ports and temporary passwords, starts a temporary Host per task, and defaults Workers to `fullAccess` with always-allow tool authorization, so confirm workdir, prompts, ACP sessions, transcripts, and local logs
- [WorkBuddy China Legal Skills](https://github.com/MAXXXXXLI/workbuddy-cn-legal-skills) - An Apache-2.0 collection of 151 importable China-law Skills with explicit attribution to Anthropic's `Claude for Legal`, covering contracts, data compliance, AI governance, labor, IP, disputes, and regulatory work. It is for research, drafts, and learning rather than legal advice
- [WorkBuddy Check-in (Maquer)](https://github.com/Maquer/workbuddy-checkin) - An MIT-licensed, dependency-free Python check-in and credit-reporting tool supporting CN/Global accounts, token refresh, multi-account rotation, daily reports, and cron scheduling
- [DSH WorkBuddy XD Pool](https://github.com/aosi526/dsh-workbuddy-xdpool) - An MIT-licensed DeepSeek Harness plugin that discovers historical WorkBuddy desktop logins and combines them into a failover model pool with model catalog, credits, cooldowns, and a loopback streaming bridge
- [E-commerce Visual Copywriting](https://github.com/feichanggege/ecommerce-visual-copywriting-skill) - A repeatable workflow for product analysis, copywriting, and commerce imagery.
- [Image Story Video Wizard](https://github.com/aaronyi97/image-story-video-wizard) - An audio-first story-video Skill for WorkBuddy and Codex with approval gates at consequential steps.
- [LibTV Video Agent](https://github.com/PomeloR611/libtv-video-agent) - An MIT-licensed video-production Skill compatible with WorkBuddy, Codex, and Claude, covering storyboards, image/video generation, TTS, subtitles, and local FFmpeg finishing
- [Social Account Doctor](https://github.com/JuneYaooo/social-account-doctor) - Diagnoses accounts and high-performing posts across major Chinese content platforms.
- [Bruce Draw.io](https://github.com/bruc3van/bruce-drawio) - Generates, validates, and exports draw.io diagrams across platforms.
- [Textbook Writer Skills](https://github.com/cabbage2000-lab/textbook-writer-skills) - Plans, writes, and reviews textbooks using Understanding by Design.
- [OfferLoop](https://github.com/riwonswain-ovo/OfferLoop) - An open job-search system built from seven Skills and a Feishu workspace.
- [Job Navigation Skill](https://github.com/AriaXXX-free/job-navigation-skill) - An evidence-based Skill that researches current roles and JDs, compares them with resume/project evidence, and prioritizes job-search actions
- [WorkBuddy WeChat Publisher](https://github.com/cnproduct/workbuddy-wechat-publisher) - Produces copy, images, layout, and WeChat Official Account drafts.
- [CordysCRM Skills](https://github.com/1Panel-dev/CordysCRM-skills) - Agent Skills covering a CRM lead-to-cash workflow.
- [Self-media Compliance Review](https://github.com/JuneYaooo/self-media-compliance-review) - Reviews videos, covers, subtitles, sales claims, and platform risks before publishing.
- [Ontology-driven Development](https://github.com/sharptoolbox/ontology-driven-dev) - A traceable workflow from requirements and ontology modeling to application delivery.
- [Codebase Reverse](https://github.com/sharptoolbox/codebase-reverse) - Reconstructs functional, architectural, API, and data-model documentation from Java services.
- [Trade Pipeline](https://github.com/Dangooy/trade-pipeline-skill) - Generates quotations, pro forma invoices, commercial invoices, and packing lists from one order record.
- [SeaTable Production](https://github.com/Darling5/seatable-production) - An MIT-licensed WorkBuddy production-delivery Skill covering projects, planning, procurement, BOM/inventory, shipping, maintenance, and analysis
- [Local Markdown Memory](https://github.com/asen-goat-mine/boujoy-local-markdown-memory) - A local-first, auditable long-term Markdown memory template for WorkBuddy and Codex.
- [llm-wiki Skill](https://github.com/JustineJiao/llm-wiki-skill) - A GPL-3.0 personal knowledge-base Skill explicitly supporting WorkBuddy, turning web pages, PDFs, local files, and other material into linked Markdown pages with confidence labels and review items
- [Org Context](https://github.com/wangjialiang678/org-context) - An MIT-licensed context-organization Skill for WorkBuddy, Claude Code, and OpenCode that separates facts, decisions, and status to make enterprise materials easier to retrieve, with templates, a runnable example, and mechanical checks
- [Delivery Razor](https://github.com/Ketian823/delivery-razor) - An MIT-licensed WorkBuddy delivery-hygiene Skill that removes cross-session memory labels, in-session residue, and defensive disclaimers, with optional compression rules for executive one-pagers
- [WorkBuddy App Builder Skill](https://github.com/sharptoolbox/WorkBuddy-AppBuilderSkill) - An ontology-driven Skill for requirements discovery, human checkpoints, and local SQLite/API domain-app generation
- [WorkBuddy Theme Skill](https://github.com/comeonzhj/WorkBuddy-theme-skill) - Creates, validates, previews, applies, and restores reversible runtime themes for WorkBuddy
- [ZhiGui Second Brain Skill](https://github.com/CarlWangChina/zhigui-openclaw-ui-second-brain-skill) - A local MCP-backed planning and knowledge-graph workspace for WorkBuddy

### Tools and integrations

- [Codex ↔ WorkBuddy MCP Bridge](https://github.com/ZhaoXiangyu99/workbuddy-mcp) - A license-un-declared Node.js MCP bridge that hands Codex subtasks to a WorkBuddy inbox and provides tools for opening WorkBuddy views
- [Lexiang Knowledge Base Skill](https://github.com/tencent-lexiang/lexiang-mcp-skill) - A license-un-declared Lexiang knowledge-base MCP Skill for search, reading, document writing, Block editing, file transfer, and external imports; its guide notes that WorkBuddy users can use the built-in Lexiang connector directly
- [Claude Code Router](https://github.com/musistudio/claude-code-router) - An MIT-licensed local model router and Agent control plane with explicit WorkBuddy support, unifying model, account, failover, tool, and MCP configuration
- [Qwen MM Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) - An Apache-2.0 multimodal Agent Skills/MCP collection from Qwen with setup paths for WorkBuddy, QoderWork, and QwenWork, covering educational video, document, and vision tasks
- [Huawei Cloud DevKit](https://github.com/huaweicloud/huaweicloud-devkit) - An Apache-2.0 official Huawei Cloud Agent toolkit with explicit WorkBuddy support, Skills, MCP tools, deployment utilities, and safety guardrails
- [CloudBase AI Toolkit](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) - Tencent CloudBase's official MIT-licensed toolkit, bringing database, authentication, cloud functions, storage, and deployment Skills and MCP to WorkBuddy
- [workbuddy_to_api](https://github.com/yxxawa/workbuddy_to_api) - An MIT-licensed local WorkBuddy proxy exposing OpenAI/Anthropic-compatible APIs, health/model endpoints, and optional MCP configuration
- [SkillDeck](https://github.com/crossoverJie/SkillDeck) - An MIT-licensed open-source macOS Skill manager with explicit WorkBuddy/CodeBuddy support
- [DocuGenius](https://github.com/bruc3van/DocuGenius) - An MIT-licensed open-source editor extension that converts Word, Excel, PowerPoint, and PDF files into structured Markdown for WorkBuddy/CodeBuddy and other AI tools
- [workbuddy-api (simplast)](https://github.com/simplast/workbuddy-api) - An MIT-licensed lightweight Node.js 18+ local proxy that connects CodeBuddy/WorkBuddy to OpenAI-compatible clients and the Vercel AI SDK, exposing chat, model, and health endpoints
- [WorkBuddy2API (hawklithm)](https://github.com/hawklithm/workbuddy2api) - An MIT-licensed, well-tested local protocol adapter that converts WorkBuddy/CodeBuddy-compatible traffic to OpenAI, Anthropic, and Responses formats, with streaming, tool calls, desensitization, and isolated multi-account state
- [Xiaohongshu Viral Note Agent Skill](https://github.com/xuboboo/xiaohongshu-viral-note-agent-skill) - An MIT-licensed WorkBuddy-compatible Skill/MCP for public trend research, note generation, claim/originality/compliance checks, account analytics, and draft-preview-approval-publish workflows
- [WorkBuddy Agent File Parser Downloader](https://github.com/mayuhaos/workbuddy-agent-file-parser-downloader) - An MIT-licensed Python 3.11+ CLI/GUI utility that parses the public expert/team manifest, downloads `.tar.gz` bundles, and produces local Excel summaries and retry lists
- [WorkBuddy × ChatCut MCP](https://github.com/chonpszhou/workbuddy-chatcut-mcp) - An MIT-licensed WorkBuddy video-editing MCP integration with OAuth 2.0 + PKCE authorization scripts, a configuration template, token refresh, and ChatCut project operations
- [IMA Knowledge Base MCP](https://github.com/xuewolai/ima-mcp-server) - An MIT-licensed Node.js MCP server with explicit WorkBuddy support for searching, browsing, reading, and importing URLs into IMA knowledge bases
- [CaSee Intelligence MCP](https://github.com/xcasee/casee-mcp-server) - An MIT-licensed WorkBuddy-compatible research MCP offering 500+ source retrieval, T-Score credibility metadata, and stdio/Streamable HTTP modes
- [QClaw × WorkBuddy Bridge](https://github.com/liuboacean/qclaw-workbuddy-bridge) - An MIT-licensed macOS workflow bridge that sends Weixin/QClaw tasks to WorkBuddy through a shared JSON queue and launchd events, with Skills for submission, result checking, and queue management
- [GitHub Trending MCP](https://github.com/ImLeonLi/GitHub-Trending-MCP) - An Apache-2.0 GitHub Trending retrieval tool with WorkBuddy Skill support, filtering by time range, programming language, and spoken language, with MCP and local web modes
- [PowerContext](https://github.com/oceanbase/powercontext) - An Apache-2.0 cross-Agent memory and work-handoff system maintained by the OceanBase team, with a one-command WorkBuddy `UserPromptSubmit` hook, Streamable HTTP MCP, and `project-context` Skill for searching/writing Memory and creating/committing Handoffs. Installation updates hooks, settings, MCP, and Skills under `~/.workbuddy`
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) - An MIT-licensed team Agent-memory hub maintained by Tencent with direct WorkBuddy Proxy integration, turning sessions, documents, and code into Chat Memory, Skills, an LLM Wiki, and CodeGraph through a local Docker stack
- [BrowserSkill](https://github.com/Tencent/BrowserSkill) - Tencent-maintained MIT-licensed local browser bridge with explicit WorkBuddy support
- [Maestro](https://github.com/joosure/Maestro) - An AGPL-3.0 project-task orchestration platform connecting Linear/TAPD tasks to GitHub/CNB and Codex, Claude Code, OpenCode, or CodeBuddy. It runs tasks in isolated workspaces, records diffs/logs/tool calls, and writes results back
- [WorkIsland](https://github.com/qianzhu18/workisland) - An Apache-2.0 local Agent status and attention router for Apple Silicon macOS with native WorkBuddy/CodeBuddy, Codex, Claude Code, and other integrations, providing task monitoring, approval/question handling, and source-session navigation. It installs local hooks, observes task/transcript signals, stores clipboard history and terminal state, and sends approval replies that change Agent execution
- [WorkBuddy OpenAPI PHP SDK](https://github.com/JaguarJack/workbuddy-openapi) - An MIT-licensed third-party PHP 8.1+ SDK for the official WorkBuddy OpenAPI, covering OAuth, profile and phone verification, local-assistant messages/permissions, cloud tasks, artifacts, redemption, and ACP. It does not persist tokens itself, but handles client secrets, user/task tokens, and prompts
- [WorkBuddy2API (Tom6814)](https://github.com/Tom6814/WorkBuddy2API) - An MIT-licensed third-party local/containerized protocol converter that wraps WorkBuddy models as an OpenAI-compatible REST API with streaming chat, tool calls, text/image generation, token refresh, and Docker deployment
- [WorkBuddy Jupyter Bridge](https://github.com/Kallium-cn/workbuddy-jupyter-bridge) - An MIT-licensed JupyterLab MCP wiring Skill for WorkBuddy 5.x that provides code execution in the real kernel, notebook/cell read-write, persistent variables, and DataFrame introspection, with nine end-to-end checks for configuration and troubleshooting
- [BuddyBridge](https://github.com/ben4202121/buddybridge) - An MIT-licensed Windows-only Obsidian plugin that brings the local WorkBuddy/CodeBuddy CLI into a Vault sidebar with streaming chat, thinking/tool-step views, conversation history, and current-note context
- [DSH Subagent CodeBuddy](https://github.com/flg1217/dsh-subagent-codebuddy) - An MIT-licensed DeepSeek Harness plugin that registers CodeBuddy CLI as parallel, continuable subagents and translates tool steps
- [WorkBuddy Computer Use for Intel Mac](https://github.com/Guyzn/workbuddy-cua-mcp) - An MIT-licensed Intel-Mac WorkBuddy MCP providing screenshots, mouse/keyboard/window control, and Chrome CDP automation to cover the gap before Apple Silicon's native Computer Use
- [WorkBuddy Token Tracker](https://github.com/abc1317679842-ui/workbuddy-token-tracker) - An MIT-licensed Windows WorkBuddy Skill and hook that aggregates per-turn tokens, duration, per-model daily ledgers, and system notifications from local traces/transcripts. It scans complete sessions, persistently writes ledgers and diagnostic logs, invokes Node/Python/PowerShell, and enables refreshes from several public pricing sources by default
- [AgentSessionQuery](https://github.com/iuuunlyk/AgentSessionQuery) - An MIT-licensed, PowerShell 7 local session-query tool that searches Codex, Claude Code, and WorkBuddy sessions, workspaces, models, and token statistics through one command. It makes no network requests and opens the WorkBuddy database in SQLite read-only mode, but scans complete transcripts, invokes local Python, briefly writes and deletes an intermediate JSON file, and can expose titles, paths, branches, and resume commands in output, so redact results before sharing or redirecting them.
- [Agent Avatar](https://github.com/joyparkray/agent-avatar) - An MIT-licensed Live2D desktop companion for macOS and Windows that observes WorkBuddy, Codex, Claude Code, Hermes, and DeepSeek Harness events and maps Agent state to animation. It bundles no model, while Live2D Cubism Core has separate license terms
- [AgentsView](https://github.com/kenn-io/agentsview) - An MIT-licensed local-first cross-agent session search, analytics, and token-use tool supporting WorkBuddy's `~/.workbuddy/projects`
- [DSH Agent Preset Recommender](https://github.com/LeemanCheung/dsh-agent-preset-recommender) - An MIT-licensed DeepSeek Harness host plugin that boundedly summarizes local Codex, Claude Code, and WorkBuddy/CodeBuddy activity and recommends a preset without an LLM call, network request, command execution, installation, or preset mutation
- [AgentNave](https://github.com/TimWongUp/agentnave) - An MIT-licensed local STDIO MCP runtime that starts and supervises version-pinned CodeBuddy, Codex, Claude, Antigravity, and Grok CLI subagents with timeout, wait, cancel, provider-exclusion, and tested lifecycle controls
- [agentsw](https://github.com/tchivs/agentsw) - An MIT-licensed cross-agent provider switcher that imports and synchronizes OpenAI/Anthropic-compatible provider settings, model metadata, and WorkBuddy/DSH configuration across nine coding agents
- [AgentSkillsManager](https://github.com/lasoons/AgentSkillsManager) - An MIT-licensed VS Code extension for browsing and installing Skill repositories across CodeBuddy, Cursor, Trae, Antigravity, Qoder, Windsurf, and VS Code
- [HTML to Feishu Doc](https://github.com/bonboruyau-dev/html-to-feishu-doc) - An MIT-licensed cross-platform Skill that converts HTML or URLs to Markdown and optionally creates Feishu/Lark documents while preserving tables, images, headings, and integrity checks
- [WeChat Article to Markdown](https://github.com/bonboruyau-dev/wechat-article-to-md) - An MIT-licensed Python Skill that fetches WeChat Official Account articles, extracts structured Markdown, downloads images, converts tables to GFM, and supports Obsidian output for WorkBuddy, Claude Code, and Codex
- [Codex Mate](https://github.com/SakuraByteCore/codexmate) - An Apache-2.0 local CLI + Web UI for managing CodeBuddy, Codex, Claude Code, Gemini CLI, OpenCode, KiloCode, OpenClaw, and Pi configurations, sessions, Skills, MCP, and task queues. It explicitly supports WorkBuddy/CodeBuddy session browsing and a local Skills market, with unit and E2E tests. It reads and writes local configuration, sessions, and credentials, and can start protocol bridges, import Skills, or delete sessions, so back up first and review paths, keys, ports, and each write action.
- [CLI2API](https://github.com/caigee-cmd/cli2api) - An MIT-licensed self-hosted local gateway that converts WorkBuddy (and Qoder/Trae) login state into OpenAI/Anthropic-compatible APIs with multi-account routing, isolated workers, Docker, and a loopback console
- [WorkBuddy2API](https://github.com/ShouZhuo0413/codebuddy2api) - An MIT-licensed local protocol converter that exposes an already signed-in WorkBuddy/CodeBuddy session through OpenAI, Responses, and Anthropic-compatible APIs
- [CodeBuddy2OpenAI](https://github.com/HanHan666666/codebuddy2openai) - An MIT-licensed single-file local protocol converter that wraps a signed-in CodeBuddy/WorkBuddy session as an OpenAI-compatible `/v1/chat/completions` endpoint, listening on `127.0.0.1` by default
- [CodeBuddy Statusline](https://github.com/runzhi/codebuddy-statusline) - An MIT-licensed cross-platform CodeBuddy Code statusline showing context progress, tokens, tool calls, cost, credits, duration, and line changes, with detailed cost reports and configurable layouts
- [CodeBuddy2API](https://github.com/orangeboyChen/codebuddy2api) - An MIT-licensed, source- and test-backed self-hosted CodeBuddy gateway with OpenAI/Anthropic-compatible APIs, encrypted SQLite or PostgreSQL storage, a web admin console, access keys, credential management, and sanitized debug traces. The example binds to `127.0.0.1`, but Docker and multi-instance deployments handle sign-in credentials, prompts, and request traces, so set a strong random encryption key, restrict the admin console and ports, and review logs, retention, and Tencent account terms first.
- [CodeBuddy Proxy](https://github.com/wnddd839/codebuddyapi-proxy) - A BSD-3-Clause Go self-hosted gateway that translates CodeBuddy OAuth/API access into an OpenAI-compatible interface with streaming, model discovery, domestic/global endpoints, account pools, a loopback admin UI, source builds, and multi-platform releases. It defaults to loopback and documents mode-0600 credential files, API-key protection, and restore flows, but OAuth, account rotation, the admin UI, and prebuilt artifacts still require review of account authorization, network boundaries, logs/backups, and service terms.
- [OpenCode CodeBuddy Auth](https://github.com/kuops/opencode-codebuddy-auth) - An MIT-licensed OpenCode plugin with source and installation documentation that authenticates CodeBuddy/IOA through browser OAuth, discovers models dynamically from `/v3/config`, and refreshes tokens automatically across Chinese and international endpoints. OpenCode manages the token in local `auth.json`
- [CodeBuddy IDE CN for Linux](https://github.com/JipZeonGit/codebuddy-ide-cn-linux) - An MIT-licensed unofficial Linux packaging adapter that converts a CodeBuddy CN x86_64 DEB fetched by the user from Tencent's official CDN into Arch/AUR, RPM, or AppImage packages locally. The repository explicitly does not host or redistribute Tencent binaries and documents version checks, ignored build directories, EULA, and trademark boundaries, but building it installs system dependencies, extracts, and repackages an upstream Electron application
- [Buddy2api](https://github.com/wicm84266964/Buddy2api) - An MIT-licensed local multi-channel gateway that separately exposes WorkBuddy/CodeBuddy, QClaw, QwenWork, and TraeWork login states through OpenAI-compatible APIs, with Codex Responses, Docker, and API-key channel routing
- [WorkBuddy CLIProxy provider](https://github.com/lovingfish/workbuddy-cliproxy) - An MIT-licensed CLIProxyAPI plugin that exposes CodeBuddy models to OpenAI/Anthropic clients with QR login and token refresh
- [CodeBuddy OpenAI Proxy (Jevil961)](https://github.com/Jevil961/codebuddy-openai-proxy) - An MIT-licensed lightweight Python service that converts CodeBuddy CN chat into an OpenAI-compatible API through OAuth2 or a manually supplied Bearer token
- [WorkBuddy Remote](https://github.com/vergess3/workbuddy-remote) - An MIT-licensed Windows remote browser bridge that reuses the desktop WorkBuddy WebUI and forwards page calls through local CDP
- [Skill Buddy](https://github.com/konnga/skill-buddy) - An MIT-licensed, 93-star cross-agent desktop workspace with WorkBuddy user-scope support, unified Skill/MCP inventory, multi-platform installation, drift detection, exact write previews, trash/undo removal, public-resource discovery, private Git backup, and protected-branch team libraries
- [AgentHub](https://github.com/nicechencs/AgentHub) - An MIT-licensed local cross-platform Agent management GUI/CLI for installing and connecting WorkBuddy and other tools, managing shared/project Skills, sessions, usage, and backups
- [FyAgent](https://github.com/fy-agent/fyagent) - A local cross-platform AI-tool configuration workspace under PolyForm Noncommercial 1.0.0 (with CC Switch-derived portions remaining MIT), supporting WorkBuddy discovery plus previewed and validated management of models/providers, Skills, MCP, prompts, and related resources
- [WorkBuddy Expert Bridge](https://github.com/xiaojinlucky/workbuddy-expert-bridge) - An MIT-licensed local Skill that lets Codex, Cursor, Claude Code, Grok, and VS Code read and recommend already-installed WorkBuddy experts or teams, showing match evidence and local availability before the user chooses whether to use one
- [WorkBuddy for Obsidian](https://github.com/bigbay957-sudo/workbuddy-for-obsidian) - An MIT-licensed community Obsidian plugin that connects the local WorkBuddy CLI in a sidebar, supporting selection editing, multiple tasks, file references, source tracing, and local uploads
- [Workbuddian](https://github.com/jiang198012/workbuddian) - An MIT-licensed Obsidian desktop plugin that brings local WorkBuddy/CodeBuddy CLI into a vault with streaming chat, `@` references, session forks, MCP management, per-action approval, and undoable edits
- [Codex × WorkBuddy Token Monitor](https://github.com/tylerchen0123-sudo/CODEX-Inspection-Guidelines-for-Dosage) - An MIT-licensed local real-time Token dashboard with no third-party Python dependencies
- [Tencent Meeting CLI](https://github.com/TencentCloud/tencentmeeting-cli) - Tencent's official CLI for meeting management and Agent integration.
- [DCC-MCP Agent Plugins](https://github.com/dcc-mcp/dcc-mcp-agent-plugins) - An MIT-licensed official-distribution suite of DCC-MCP Agent Skills and plugins compatible with WorkBuddy, Codex, Claude Code, and other hosts
- [SkillHive](https://github.com/tonycc/skillhive) - An MIT-licensed enterprise Skill hub that uses a WorkBuddy MCP connector for centralized distribution, versioning, review, feedback, and operation auditing, with auditable connector build and verification scripts
- [GitHub MCP Server Lite](https://github.com/1186247283zj-pixel/github-mcp-server-lite) - An MIT-licensed GitHub MCP server using only the Python standard library, with 24 tools for repositories, files, branches, issues, pull requests, search, and notifications
- [BailingHub WorkBuddy Connector](https://github.com/bailinghub/bailinghub-workbuddy-connector) - An MIT-licensed independent WorkBuddy enterprise connector that uses browser PKCE authorization, capability checks, idempotent invocations, approvals, limits, and audit to query or operate connected business systems
- [AssetPlex](https://github.com/wynter-cai/assetplex) - An MIT-licensed, fully local cross-agent asset hub that centralizes identity, Skills, rules, and MCP configuration and syncs them to WorkBuddy, Codex, Claude Code, TRAE, and Qoder, with reverse import, format translation, symlinks, and a local Web UI
- [VOKO](https://github.com/laoyudashu/voko) - An AGPL-3.0 local-agent communication runtime for WorkBuddy and other Agents, supporting MCP, A2A 1.0, REST/Webhook, precise conversation routing, permission policies, human intervention, and local audit
- [Task Passport](https://github.com/dongsheng123132/task-passport) - An MIT-licensed versioned task-handoff protocol compatible with WorkBuddy, Codex, Claude, and other Harnesses. It packages verified state, facts, decisions, and next steps into portable TaskPacks with stale-write conflicts, ask/receipt handback, conformance checks, and cross-machine import
- [Garmin Connect Plugin for DSH](https://github.com/Likenttt/garmin-connect-plugin-for-dsh) - An MIT-licensed, 11-star Garmin Connect MCP/Skill plugin that supports WorkBuddy and other Agents with browser MFA for activities, sleep, steps, and heart-rate queries, while distinguishing read-only tools from local FIT-file writes and workout-library creation
- [NetSuite MCP](https://github.com/Bolton-Z/ns-mcp-china) - An MIT-licensed NetSuite MCP connector built with Node.js built-ins that lets WorkBuddy use OAuth 2.0 to query SuiteQL, reports, and records with automatic token refresh
- [Origin Auto](https://github.com/simcrq/origin-auto) - An MIT-licensed OriginLab scientific-plotting MCP and WorkBuddy Skill for Windows, with 28 COM-automation tools, a standalone-script fallback, real-data plotting validation, and PNG/PDF/OPJU existence checks
- [DSH Reminder](https://github.com/Aisland-SJL/dsh-reminder) - An MIT-licensed DeepSeek Harness cross-window reminder plugin that notifies you when a task finishes or waits for human approval
- [Devnors Data MCP](https://github.com/DevnorsAI/devnors-data-mcp) - An MIT-licensed, 256-star remote/local MCP data service for WorkBuddy covering laws and legal cases, company registries and annual reports, tax-invoice lookup, enforcement checks, content/index/trending data, and express tracking, with capability and parameter discovery before calls
- [Wudao A-Share Stock Data MCP](https://github.com/jcdreamjc/wudao-mcp) - An MIT-licensed, 11-star remote HTTP MCP data service with direct WorkBuddy support and 63 read-only A-share tools for quotes, K-lines, indexes/ETFs, limit-up ladders, sector rotation, capital flow, Dragon Tiger Lists, research reports, disclosures, and post-market review
- [Beav](https://github.com/Jamailar/Beav) - A local-first workspace for creator research, assets, ideation, and production that connects to WorkBuddy through a user-scoped plugin and loopback MCP service. It uses a custom MIT-derived license that prohibits commercial use, production packages may lead the public source snapshot, and workflows can involve local workspaces, model credentials, browser/social content, and localhost services
- [wechat-openclaw-channel](https://github.com/HenryXiaoYang/wechat-openclaw-channel) - Routes WeChat messages to a local OpenClaw Agent through QClaw or WorkBuddy OAuth/Centrifuge mode. It stores WorkBuddy access and refresh tokens in `~/.openclaw/openclaw.json`, carries message content through Tencent endpoints, and has no LICENSE file despite MIT claims in its README/package metadata
- [DSH WorkBuddy Connect](https://github.com/corrinehu/dsh-workbuddy-connect) - Connects WorkBuddy desktop models to DeepSeek Harness across Web, Desktop, and TUI
- [DSH Connect WorkBuddy](https://github.com/dingminhua/dsh-connect-workbuddy) - An MIT-licensed DSH plugin building on the preceding project's published design, adding a selectable model catalog, per-model image opt-in, local multi-account switching, package-level credits, check-in, diagnostics, and a random-secret loopback shim. It reads current and historical WorkBuddy auth files, writes refreshed credentials under `$DSH_HOME` with mode 0600, sends prompts and tool results to non-public Tencent endpoints, and changes state through account selection, settings saves, and user-clicked check-in, so review credential provenance, account choice, network data, and platform terms before use.
- [DSH Memory Palace](https://github.com/lovezi0/dsh-memory-palace) - An MIT-licensed DeepSeek Harness memory plugin that bridges existing `.workbuddy/memory` directories, keeps editable Markdown memories/logs/summaries across sessions, and gates deletion behind confirmation
- [DSH Hybrid Memory](https://github.com/Frog755/dsh-hybrid-memory) - An MIT-licensed local hybrid-memory plugin combining frozen snapshots, a SQLite FTS5 fact base, and imports from Hermes, Claude, Codex, and WorkBuddy, with threat scanning, a review queue, atomic writes, and drift detection
- [DSH Agent Selector](https://github.com/jiang12345-code/dsh-agent-selector) - An MIT-licensed DeepSeek Harness plugin that dispatches tasks to WorkBuddy built-in/custom models, Codex, or Claude and returns provenance receipts
- [Tonghuasun Agent](https://github.com/zhuyifang/tonghuasun-agent) - An AGPL-3.0 connector for the Tonghuashun Windows desktop client that exposes quotes, account, positions, and trade data to WorkBuddy and other Agents
- [DSH WorkBuddy Provider](https://github.com/Axiaohungry/dsh-llm-workbuddy) - Adds WorkBuddy China models to DeepSeek Harness with API-key and browser-token authentication
- [OpenWorkBuddy](https://github.com/CatCatUncle/openworkbuddy) - An open-source WorkBuddy-style local Agent workspace with Skills, MCP, desktop support, and multiple IM channels
- [SailFish](https://github.com/ysyx2008/SailFish) - A WorkBuddy-style personal desktop secretary for macOS and Windows with memory, Skills, MCP, browser, terminal, and multi-IM channels
- [OpenBuddy](https://github.com/opensymph/OpenBuddy) - An MIT-licensed Rust/Tauri WorkBuddy-style cross-platform desktop client with BYOK, multi-provider models, Skills, MCP, plan mode, sub-agents, and local automations
- [Agent Context Sync](https://github.com/westsource/agentctxsync) - Self-hosted session synchronization and backup across devices and Agents.

### Community clients and enhancements

- [Clawd on Desk](https://github.com/rullerzhou-afk/clawd-on-desk) - An AGPL-3.0 cross-platform Agent desktop pet and status notifier with explicit WorkBuddy support through optional hooks
- [Dream Work Theme](https://github.com/xxxhh336/dream-work-theme) - An Apache-2.0 cross-platform Electron theme manager with explicit WorkBuddy support, app discovery, compatibility filtering, runtime switching/restoration, and a floating theme menu
- [WorkBuddy Dream Skin (macOS)](https://github.com/smartcai87/workbuddy-dream-skin) - An MIT-licensed macOS skin utility that injects reversible themes through loopback CDP, supports light/dark modes, local images, hot switching, and restoration without modifying WorkBuddy.app, its signature, or `app.asar`
- [WorkBuddy Buddy](https://github.com/FlashFamily/workbuddy-buddy) - An MIT-licensed macOS WorkBuddy status pet that shows thinking, tool use, approval waits, completion, and failure, and can feed allow/deny decisions back to WorkBuddy
- [Skills Hub](https://github.com/qufei1993/skills-hub) - An MIT-licensed cross-platform desktop Skill manager with an explicit WorkBuddy adapter, central installation, organization, updates, and sync across multiple Agents
- [WorkBuddy Auto Sign-in](https://github.com/88lin/workbuddy-auto-signin) - Dependency-free check-in and reward automation
- [WorkBuddy Check-in](https://github.com/Coco-katarina/workbuddy-checkin) - An MIT-licensed WorkBuddy daily check-in Skill that reads local login state and makes idempotent requests to Tencent's documented official endpoint
- [WorkBuddy Auto Check-in](https://github.com/liubinne/workbuddy-free-credits) - An MIT-licensed macOS/Windows WorkBuddy daily check-in Skill with credential-path checks, a single-instance lock, sanitized logs, scheduled-task install/uninstall, legacy-job backup, and tests
- [WorkDaddy](https://github.com/babygoton/WorkDaddy) - A desktop enhancement for backups, session migration, and long-running task support.
- [WorkBuddy Skin Studio](https://github.com/cdredfox/workbuddy-skin-studio) - A reversible theme manager for WorkBuddy Desktop.
- [WorkBuddy Skin](https://github.com/itcastWsy/workbuddy-skin) - An MIT-licensed cross-platform WorkBuddy skinning CLI that uses a loopback-only `127.0.0.1` CDP injector for wallpapers, frosted-glass themes, local image processing, live switching, restore, and offline self-tests. Optional persistence writes a user environment variable or rewrites Windows shortcuts, and the published single-file binaries have no signing statement
- [WorkBuddy Dream Skin](https://github.com/zhouwei713/WorkBuddy-Dream-Skin) - An MIT-licensed, image-driven Windows theme system with presets, a tray controller, verification, and restore tooling. It restarts WorkBuddy with a loopback CDP port and runs unsigned PowerShell plus renderer injection, so save active work and review the scripts before enabling it.
- [M5Stack Toys / Core2 Buddy](https://github.com/sindney/m5stack_toys) - An MIT-licensed collection of M5Stack hardware projects
- [LinkCode](https://github.com/arcboxlabs/linkcode) - An open desktop client supporting multiple coding Agents.
- [CodeDrobe Desktop](https://github.com/CodeDrobe/desktop) - An open-source, reversible theme manager for WorkBuddy and other AI desktop apps
- [WorkBuddy Switch](https://github.com/changexbc/workbuddy-switch) - An MIT-licensed cross-platform WorkBuddy/CodeBuddy account manager with OAuth login, account switching, session backup/copy, points and Token usage views, and macOS, Windows, and Linux packages
- [Trae WorkBuddy Assistant](https://github.com/cxqc168-wq/Trae-workbuddyAssistant) - An MIT-licensed Windows Tauri tool for Trae and WorkBuddy account management, OAuth/tokens, points queries, check-in, and a local OpenAI-compatible gateway
- [WorkBuddy Account Migrate](https://github.com/xiaoliuzhuan666/workbuddy-account-migrate) - Moves conversations, long-term memory, and MCP connectors after an account switch
- [Crew](https://github.com/shuishenghualalala/Ace) - An Apache-2.0 open-source WorkBuddy-style local multi-agent workbench with Desktop, Web, CLI, Skills, MCP, knowledge-base, task automation, and multi-agent collaboration
- [OpenWorkbuddy](https://github.com/chenin0931/OpenWorkbuddy) - An MIT-licensed independent open-source WorkBuddy-style macOS Agent workbench with BYOK models, files and Shell, browser control, MCP, Skills, memory, automation, approvals, and crash recovery

### Benchmarks

- [workbuddy-bench](https://github.com/Tencent/workbuddy-bench) - Tencent's multi-domain coding-agent benchmark with 260 Code, Web, Office, and Security tasks, a Docker-sandboxed evaluation framework, a Hugging Face dataset, and the `wbbench-run-setup` Skill


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

- [Workbuddy](https://github.com/Lincyaw/workbuddy) - An Apache-2.0 GitHub Issue-driven Agent orchestration platform that maps Issue states to workflows and dispatches Claude, Codex, and other runtimes
- [Better Harness](https://github.com/QoderAI/better-harness) - An MIT-licensed Agent Harness Engineering platform with explicit WorkBuddy support, evidence-backed workflow reports, resumable tasks, Skill/MCP/Hook boundaries, controlled experiments, and adapters for 37 Agent platforms
- [Comet](https://github.com/rpamis/comet) - An MIT-licensed resumable long-running task and Skill platform with explicit WorkBuddy support, Native/Classic requirements workflows, phase gates, Skill authoring/evaluation/release tooling, and adapters for 37 Agent platforms
- [Automated daily briefing](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Daily-Briefing) - Connect QQ Mail, test a briefing, schedule daily delivery, and personalize the result.
- [AI self-directed execution](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/AI-Self-Driven) - Define an outcome, let WorkBuddy plan the steps, and require a self-check before delivery.

## Research and Engineering

- [Tencent WorkBuddy Bench](https://arxiv.org/abs/2607.20911) - A multi-domain coding-agent benchmark with a reproducible evaluation protocol.
- [WorkBuddy Bench website](https://workbuddybench.com/) - Official benchmark overview, tracks, results, and evaluation entry point.
- [WorkBuddy Bench dataset](https://huggingface.co/datasets/tencent/workbuddy-bench) - Official task archives for the Code, Web, Office, and Security subsets.
- [CloudBase model configuration](https://docs.cloudbase.net/ai/ai-tools/workbuddy) - Connect an OpenAI-compatible model endpoint.

</details>

## About

This is an independently maintained WorkBuddy resource index released under [CC0 1.0 Universal](LICENSE). Indexed resources retain their own licenses and terms; the machine-readable index is [`site/llms.txt`](site/llms.txt), project-maintenance notes are in [CONTRIBUTING.md](CONTRIBUTING.md), and citation metadata is in [CITATION.cff](CITATION.cff).
