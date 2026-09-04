![Awesome WorkBuddy - Skills, MCP, Workflows and Guides](assets/awesome-workbuddy-banner.webp)

# Awesome WorkBuddy

[English](README.en.md) · 简体中文

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Check links](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml/badge.svg)](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml) [![GitHub stars](https://img.shields.io/github/stars/sandbaseai/awesome-workbuddy?style=social)](https://github.com/sandbaseai/awesome-workbuddy)

<!-- REPOSITORY-SNAPSHOT:START -->
**51 curated repositories · 4 original Skills · 40 discovery candidates · weekly validation**
<!-- REPOSITORY-SNAPSHOT:END -->

> 精选、可验证的腾讯 WorkBuddy 学习资料、Skills、MCP 与真实工作流。

如果这个清单对你有用，请点一个 **Star**，让更多 WorkBuddy 用户更容易找到经过筛选的资源。

第一次使用？从 [一分钟选型与快速开始](START_HERE.md) 开始，或打开 [可搜索资源目录](https://sandbaseai.github.io/awesome-workbuddy/) 按关键词与分类筛选。

供搜索引擎和 Agent 使用的机器可读入口见 [`site/llms.txt`](site/llms.txt)。

WorkBuddy 是腾讯推出的 AI Agent 办公工作台，可通过自然语言规划并执行研究、文档、数据、设计和开发任务。本清单帮助你从官方资料开始，找到值得复用的实践，而不是在零散信息中反复试错。

> [!IMPORTANT]
> 这是社区维护的第三方索引，不代表腾讯。安装第三方 Skill、MCP 或连接器前，请检查源码、权限和数据流向；不要上传密钥、个人隐私或未脱敏的公司资料。

## Contents

- [Start Here](#start-here)
- [Official Resources](#official-resources)
- [Open-source Ecosystem](#open-source-ecosystem)
- [Skills, Prompts and MCP](#skills-prompts-and-mcp)
- [Guides](#guides)
- [Use Cases](#use-cases)
- [Research and Engineering](#research-and-engineering)
- [Selection Standard](#selection-standard)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Start Here

- [Product homepage](https://www.workbuddy.ai/) - 产品能力、下载与套餐入口.
- [Official documentation](https://www.workbuddy.ai/docs/zh/workbuddy/) - 功能说明与使用指南的权威入口.
- [Quick start](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) - 从安装到完成第一个任务.
- [Changelog](https://www.workbuddy.ai/docs/zh/workbuddy/Changelog) - 版本能力、修复与兼容性变化.
- [Automation guide](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) - 创建一次性或周期任务，并向连接的平台推送结果.
- [MCP guide](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) - 通过可视化配置连接外部工具与数据源.
- [WorkBuddy Enterprise quick start](https://cloud.tencent.com/document/product/1831/134527) - 创建、测试、发布企业 Agent 并接入消息渠道.

## Official Resources

### Core concepts

- [Task bar and Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar) - 了解内置 Skill、导入与创建入口.
- [技能市场](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) - 统一浏览、安装、启用和管理 WorkBuddy Skills.
- [Create a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) - 用自然语言沉淀可复用工作流.
- [专家中心](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Expert-Center) - 选择带独立方法和工具链的专家，或由团长拆解并行任务的多 Agent 专家团.
- [连接器](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Connector) - 将 QQ 邮箱、腾讯文档等外部服务接入工作流，并了解配置与授权步骤.
- [记忆](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Memory) - 查看、编辑、导入或要求 WorkBuddy 忘记从对话中提取的偏好与习惯.
- [From model to harness](https://mp.weixin.qq.com/s/X_kaKcXH2uELcemaNaZ4iQ) - WorkBuddy Agent 产品架构解读.

### Platform integrations

- [Slack 接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Slack-Guide) - 按官方步骤创建 Slack App、配置权限并连接 WorkBuddy.
- [Telegram 接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Telegram-Guide) - 配置 Telegram Bot，并将令牌安全地交给 WorkBuddy 完成连接.
- [Discord 接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Discord-Guide) - 创建 Discord 应用与 Bot、设置权限并添加到服务器.
- [企业微信接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Wecom-Guide) - 将 WorkBuddy 助理接入企业微信，并完成企业侧配置.
- [飞书接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Feishu-Guide) - 创建飞书应用、配置事件与权限并连接 WorkBuddy.
- [钉钉接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/Dingtalk-Guide) - 按官方流程配置钉钉机器人与 WorkBuddy 助理.
- [QQ 接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/QQ-Guide) - 将 WorkBuddy 助理接入 QQ，并完成机器人配置与授权.
- [微信助理接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/WeixinBot-Guide) - 将 WorkBuddy 助理接入微信，并按官方步骤完成配置与二维码登录.
- [元宝派接入](https://www.workbuddy.ai/docs/zh/workbuddy/Platform-Integration/YuanBaoPai-Guide) - 将 WorkBuddy 助理接入元宝机器人，并完成官方配置流程.

### Community channels

- [WorkBuddy product page](https://cloud.tencent.com/product/workbuddy) - 腾讯云产品介绍与动态.
- [Tencent Cloud developer articles](https://cloud.tencent.com/developer/search/article-WorkBuddy) - 社区技术文章检索入口.

## Open-source Ecosystem

> [!NOTE]
> “Works with WorkBuddy” 不等于腾讯官方背书。以下项目按与 WorkBuddy 的直接相关性、文档质量、维护活跃度和社区采用度筛选；使用非官方增强、自动化或 API 工具前请检查许可证、账号条款和权限范围。

### Learning and reference

- [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) - 开源实战蓝皮书，覆盖教程、真实工作流、Skills、MCP、自动化与多智能体.
- [Agent 学习指南](https://github.com/tangshiyegit/agent-guide) - 包含 19 篇 WorkBuddy 教程和 12 个办公、内容创作与自动化案例；仓库采用 MIT 许可证，文章中的第三方产品信息仍需按官方资料复核.
- [AI Coding Guide Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh) - 包含 WorkBuddy 在内的中文 AI Coding 与办公 Agent 学习路径.
- [learn-workbuddy](https://github.com/adongwanai/learn-workbuddy) - 从零实现 WorkBuddy 风格桌面 Agent 的 24 章 Python 教程.
- [WorkBuddy Harness Bluebook](https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness) - 拆解提示词、记忆、插件、专家、Skill 与安全边界.

### Skill collections

- [WorkBuddy Skill Hub](https://github.com/sandbaseai/workbuddy-skill) - 可检索 10,000 条公开 Skill 路径的来源索引与适配仓库，提供许可证、安全和 WorkBuddy 兼容性审查状态.
- [workbuddyskills](https://github.com/infometa/workbuddyskills) - WorkBuddy Skills、连接器与专家的离线学习归档.
- [website prompts and skills](https://github.com/TencentEdgeOne/awesome-website-prompts-and-skills) - 腾讯 EdgeOne 维护的网站生成 Prompt、Skill 与挑战赛作品池.
- [Ray Skills](https://github.com/imraywang/rayskills) - 面向内容生产与发布的可执行、可验证、可恢复工作流.
- [WorkBuddy Skills](https://github.com/bitcjm/workbuddy-skills) - 涵盖创作、编程、办公和通用工具的 Skill 集合.
- [Zotero MCP WorkBuddy Guide](https://github.com/maciechen/zotero-mcp-workbuddy-guide) - 将 Zotero 文献库接入 WorkBuddy 的中文配置指南.
- [DSH Skill Picker](https://github.com/a735624258/dsh-skill-picker) - 为 DeepSeek Harness Web GUI 增加可搜索、拼音检索和键盘导航的技能选择器，复刻 WorkBuddy 式 `/技能名` 调用交互；MIT 许可。插件会读取用户与项目 Skill 目录并提供本地 Web 路由，安装前请审查其文件系统访问范围.
- [Kunpeng Skill](https://github.com/hufeng173/kunpeng-skill) - 面向 WorkBuddy、Codex、Claude Code 等 Agent 的 Apache-2.0 多源蒸馏 Skill，可从代码、网站、UI、图片、音视频和文档建立带证据的可迁移方法与生成规范；本地分析器需要按需安装依赖，使用前请确认资源与本地文件范围.
- [Skill Doctor](https://github.com/evilstar2016/skill-doctor) - 面向 WorkBuddy 等 Agent 的本地 Skill 冲突、重复、安全风险与上下文成本审计 CLI；MIT 许可，默认只读取本地文件并绑定回环地址，使用前仍应确认扫描范围与导出报告内容.

### Ready-to-use Skills

本仓库维护四个可直接安装的原创 Skill：[Document Quality Review](skills/document-quality-review/SKILL.md) 以只读方式检查交付物质量；[Skill Security Audit](skills/skill-security-audit/SKILL.md) 在安装前审查第三方扩展；[Source-backed Research Brief](skills/source-backed-research-brief/SKILL.md) 将网页和资料整理为可核验、明确区分事实与推断的研究简报；[Curate WorkBuddy Resource](skills/curate-workbuddy-resource/SKILL.md) 对候选资源给出基于相关性、质量、许可证、来源和安全证据的收录、暂缓或排除结论。

- [WorkBuddy Guide](https://github.com/Neo5093/workbuddy-guide) - 可直接安装的 WorkBuddy 使用与故障排查 Skill，覆盖连接器、专家、自动化、记忆、交互模式和常见问题；MIT 许可。其可选诊断脚本会读取本机 `~/.workbuddy` 配置与近期日志并探测本地健康端点，分享输出前请先检查并脱敏。
- [E-commerce Visual Copywriting](https://github.com/feichanggege/ecommerce-visual-copywriting-skill) - 将电商卖点分析、文案和商品图制作沉淀为可执行 SOP.
- [Image Story Video Wizard](https://github.com/aaronyi97/image-story-video-wizard) - 面向 WorkBuddy/Codex 的音频优先故事视频生产 Skill，关键步骤带确认门禁.
- [Social Account Doctor](https://github.com/JuneYaooo/social-account-doctor) - 分析主流中文内容平台账号与爆款，并输出诊断和选题建议.
- [Bruce Draw.io](https://github.com/bruc3van/bruce-drawio) - 生成、校验并导出 draw.io 图表的跨平台 Skill.
- [Textbook Writer Skills](https://github.com/cabbage2000-lab/textbook-writer-skills) - 以 UbD 逆向设计驱动教材规划、逐章写作和审核.
- [OfferLoop](https://github.com/riwonswain-ovo/OfferLoop) - 由七个 Skills 和飞书工作区组成的开源求职系统.
- [WorkBuddy WeChat Publisher](https://github.com/cnproduct/workbuddy-wechat-publisher) - 从写作、配图、排版到微信公众号草稿发布的 Skill 包.
- [CordysCRM Skills](https://github.com/1Panel-dev/CordysCRM-skills) - 覆盖销售 L2C 流程的 CRM Agent Skills.
- [Self-media Compliance Review](https://github.com/JuneYaooo/self-media-compliance-review) - 发布前审核视频、封面、字幕、带货信息与平台合规风险，并保留证据定位.
- [Ontology-driven Development](https://github.com/sharptoolbox/ontology-driven-dev) - 从需求探索、本体建模到应用构建的可追溯业务系统开发 Skill.
- [Codebase Reverse](https://github.com/sharptoolbox/codebase-reverse) - 将 Java Web 或微服务代码逆向为功能、架构、接口和数据模型文档.
- [Trade Pipeline](https://github.com/Dangooy/trade-pipeline-skill) - 由一份订单档案联动生成报价单、PI、CI 与装箱单.
- [Local Markdown Memory](https://github.com/asen-goat-mine/boujoy-local-markdown-memory) - 面向 WorkBuddy/Codex 的本地优先、可审计 Markdown 长期记忆模板.
- [WorkBuddy App Builder Skill](https://github.com/sharptoolbox/WorkBuddy-AppBuilderSkill) - 以本体驱动需求探索、人工确认和本地 SQLite/API 生成领域应用；安装前请复核生成代码与本地接口权限.
- [WorkBuddy Theme Skill](https://github.com/comeonzhj/WorkBuddy-theme-skill) - 创建、校验、预览、应用和恢复可逆的 WorkBuddy 运行时主题；会通过本地 CDP 注入样式，必要时重启应用并运行本地 guard，但不修改 app.asar、签名、账号或对话数据，使用前请确认重启影响.
- [ZhiGui Second Brain Skill](https://github.com/CarlWangChina/zhigui-openclaw-ui-second-brain-skill) - 结合本地 MCP、规划数据和知识图谱的桌面第二大脑，支持 WorkBuddy；采用 PolyForm Noncommercial 1.0.0，且会读写个人规划数据，安装前请确认许可与权限.

### Tools and integrations

- [WorkBuddy Remote](https://github.com/vergess3/workbuddy-remote) - 从其他设备远程使用 WorkBuddy.
- [Skill Buddy](https://github.com/konnga/skill-buddy) - 跨 AI Agent 管理、安装和同步 Skills 与 MCP Servers.
- [WorkBuddy for Obsidian](https://github.com/bigbay957-sudo/workbuddy-for-obsidian) - 在 Obsidian 中使用本机 WorkBuddy，支持引用、编辑和溯源.
- [Tencent Meeting CLI](https://github.com/TencentCloud/tencentmeeting-cli) - 腾讯会议官方 CLI，可作为 Agent 的会议管理工具.
- [Devnors Data MCP](https://github.com/DevnorsAI/devnors-data-mcp) - 为 WorkBuddy 提供法律、企业、内容与研究数据 API；需要外部 API Key.
- [DSH WorkBuddy Connect](https://github.com/corrinehu/dsh-workbuddy-connect) - 将 WorkBuddy 桌面端模型接入 DeepSeek Harness，支持 Web、Desktop 与 TUI；会读取本机 WorkBuddy 登录文件并将刷新凭据保存到 DSH 自有目录，依赖非官方接口，安装前请复核源码与账号条款.
- [DSH WorkBuddy Provider](https://github.com/Axiaohungry/dsh-llm-workbuddy) - 为 DeepSeek Harness 接入 WorkBuddy 中国区模型，支持 API Key 与网页登录令牌；MIT 许可。插件会保存凭据、打开登录页并请求 `copilot.tencent.com` 官方域名接口，但属于第三方适配器，使用前请核对账号条款与令牌存储.
- [OpenWorkBuddy](https://github.com/CatCatUncle/openworkbuddy) - 腾讯 WorkBuddy 的开源复刻版，提供本地 Agent 工作台、Skills、MCP、桌面与多 IM 通道；采用 PolyForm Noncommercial 1.0.0，商业使用需另行授权，并具备 Shell、浏览器和外部通道能力，使用前请审查权限与数据流.
- [SailFish](https://github.com/ysyx2008/SailFish) - 面向 macOS/Windows 的私人桌面秘书与 WorkBuddy 风格 Agent，支持记忆、Skills、MCP、浏览器、终端和多 IM 渠道；采用 AGPL v3 与商业许可双许可模式，使用前请确认许可、凭据和本地/远程操作权限.
- [Agent Context Sync](https://github.com/westsource/agentctxsync) - 在自托管服务中跨设备、跨 Agent 同步与备份会话.

### Community clients and enhancements

- [WorkBuddy Auto Sign-in](https://github.com/88lin/workbuddy-auto-signin) - 零依赖的签到与成长任务自动化；会读取本机登录令牌并调用逆向得到的非官方接口，使用前应核对账号条款与源码.
- [WorkDaddy](https://github.com/babygoton/WorkDaddy) - WorkBuddy 桌面增强工具，提供备份、会话迁移和长任务辅助.
- [WorkBuddy Skin Studio](https://github.com/cdredfox/workbuddy-skin-studio) - 可逆的 WorkBuddy Desktop 主题管理工具.
- [LinkCode](https://github.com/arcboxlabs/linkcode) - 支持多种 coding agent 的开源桌面客户端.
- [CodeDrobe Desktop](https://github.com/CodeDrobe/desktop) - 支持 WorkBuddy 的开源主题管理器，可浏览、应用并随时恢复桌面主题；使用登录、应用路径或下载功能前请复核权限与来源.
- [WorkBuddy Switch](https://github.com/changexbc/workbuddy-switch) - 跨平台切换 WorkBuddy/CodeBuddy 账号并查看用量；会保存 OAuth token、改写本地认证文件并调用非官方接口，使用前请复核源码与账号条款.
- [WorkBuddy Account Migrate](https://github.com/xiaoliuzhuan666/workbuddy-account-migrate) - 迁移账号切换后的对话、长期记忆与 MCP 连接器；MIT 许可，支持备份、回滚与迁移后验证，但会改写 SQLite 中的 `user_id` 并合并本地数据，执行前务必确认备份、源/目标账号和数据范围.

### Benchmarks

- [workbuddy-bench](https://github.com/Tencent/workbuddy-bench) - 腾讯发布的多领域 coding-agent 基准、任务与评测代码.

查看自动更新的 [生态仓库活跃度与 stars 排行](ECOSYSTEM.md)。

## Skills, Prompts and MCP

### Build and use Skills

- [Build a document review Skill](https://mp.weixin.qq.com/s/oFjSrlTp5VlMzPwN_iPOjg) - 文件审核场景的完整示例.
- [WorkBuddy + Kingsoft Docs Skill](https://mp.weixin.qq.com/s/t2XuzNFmTWYBYMLhn762eQ) - 整理微信读书笔记.
- [Eight prompts for internet teams](https://mp.weixin.qq.com/s/E1liM7qHAa-EbzVnmzYClA) - 运营与产品工作的提示词示例.

### Connect tools with MCP

- [Use an MCP server in WorkBuddy](https://developer.cloud.tencent.com/article/2698011) - MCP 配置与调用教程.
- [WorkBuddy + Agent Mail](https://mp.weixin.qq.com/s/4sEZdOlEptsqbwmWSUplVQ) - 自动处理邮件的实践.
- [WorkBuddy + Qichacha MCP](https://mp.weixin.qq.com/s/NRaiAMTHL6ckR9DGxUXPZA) - 企业尽调工作流案例.

## Guides

### Articles

- [Six WorkBuddy tips](https://mp.weixin.qq.com/s/Gdax9JpvDnDrolXFkuG-Pw) - 适合第一次使用的快速技巧.
- [WorkBuddy from zero to productive](https://mp.weixin.qq.com/s/JZWIB3tKNdRKRiXx-87Bpg) - 中文入门教程.
- [Three-month field guide](https://mp.weixin.qq.com/s/Uq8v9KIw1QJchBIouNRCkA) - 长期使用经验与工作流整理.
- [WorkBuddy beginner guide](https://mp.weixin.qq.com/s/Tiw2M-j05noSOS9rLbUiWg) - 面向中文办公场景的上手指南.

### Videos

- [Why is WorkBuddy popular?](https://www.bilibili.com/video/BV1DK7K65Ex2/) - 产品定位与能力速览.
- [WorkBuddy in 35 minutes](https://www.bilibili.com/video/BV1j1JP6oEHA/) - 完整功能演示.
- [From beginner to advanced](https://www.bilibili.com/video/BV1ggKf6AEVY/) - 系统化视频教程.
- [Build Agent workflows by talking](https://www.bilibili.com/video/BV1ngJH6yEKH/) - 一人公司自动化工作流案例.

## Use Cases

### Knowledge management

- [WorkBuddy + IMA knowledge loop](https://mp.weixin.qq.com/s/A1RpRA240rOwqFYb8RUJmg) - 可持续更新的个人知识库.
- [WorkBuddy + Obsidian](https://mp.weixin.qq.com/s/VlcgqGtKt6OpESkvfBG0Zw) - 本地笔记与 Agent 协作.
- [CFA knowledge base](https://mp.weixin.qq.com/s/B-S2cXBtSFk15QwyOeK7iQ) - 大型专业教材的检索实践.

### Documents, data and professional work

- [Create polished presentations](https://mp.weixin.qq.com/s/4v-aXrx3H3ndy0tobFJO2g) - PPT 生成与美化.
- [Automated financial report analysis](https://mp.weixin.qq.com/s/QsiUU8aep-xDQpA4ikz_DA) - 批量公司财报分析.
- [Build a 1,000-page bid](https://mp.weixin.qq.com/s/Ll6oP5J0rWhEmZ2pXdJOvw) - 超长文档处理案例.
- [Commercial lawyer starter guide](https://mp.weixin.qq.com/s/9mvnhDRrkx_UO_yA94LwGw) - 法律工作场景入门.
- [Organize local files](https://mp.weixin.qq.com/s/CmkC0VxwYjyK5MKTC-07MQ) - 文件分类与整理工作流.

### Education

- [Student learning analysis](https://mp.weixin.qq.com/s/KvPEcdJ2JUoH-F8R5E4Qww) - 学情数据处理.
- [Ten classroom applications](https://mp.weixin.qq.com/s/7z_-x3Yk6fHkSMDd3NgqEQ) - 教学场景合集.
- [Personalized student diagnostics](https://mp.weixin.qq.com/s/mgLjBbcD-avXRiM9sxJn4w) - 批量生成个性化报告.

### Content and career

- [AI content production pipeline](https://mp.weixin.qq.com/s/dSKr_a5lUYunDfS79oRzcA) - 从选题到发布的内容工作流.
- [Exam prep and job search](https://mp.weixin.qq.com/s/ldhLYboHnLiqrz12I5vW9Q) - 学习与求职任务编排.
- [Six time-consuming job-search tasks](https://mp.weixin.qq.com/s/mogl1CFtEEf9GCK2_BxbCg) - 求职自动化案例.

## Research and Engineering

- [Tencent WorkBuddy Bench](https://arxiv.org/abs/2607.20911) - 多领域 coding-agent 基准与可复现实验协议.
- [WorkBuddy Bench 官网](https://workbuddybench.com/) - 官方基准概览、评测赛道、结果与运行入口.
- [WorkBuddy Bench 数据集](https://huggingface.co/datasets/tencent/workbuddy-bench) - Code、Web、Office 与 Security 四个子集的官方任务归档.
- [CloudBase model configuration](https://docs.cloudbase.net/ai/ai-tools/workbuddy) - OpenAI-compatible 模型接入示例.

## Related Lists

- [staruhub/awesome-workbuddy](https://github.com/staruhub/awesome-workbuddy) - 中文优先的 Skills、提示词、教程、评测与集成索引.
- [awesome-workbuddy-skills](https://github.com/shuangying0001-beep/awesome-workbuddy-skills) - 自动化、数据、浏览器、微信与内容生产 Skills 集合.
- [awesome-workbuddy-use-cases](https://github.com/EvoLinkAI/awesome-workbuddy-use-cases) - 按职业和任务类型组织的大规模使用场景库.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP Server 通用生态清单；接入 WorkBuddy 前需单独安全审核.
- [Awesome DeepSeek Harness Plugins](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) - CC0 的 DSH 插件生态清单，包含与 WorkBuddy 式 Skill/Agent 工作流相邻的可安装扩展；它不是腾讯官方清单，安装任何插件前仍需逐项审查源码与权限.

## Selection Standard

本清单不以数量为目标。资源进入主列表前会从以下方面审核：

**相关性：** 必须直接支持、讲解或评测腾讯 WorkBuddy，而不是只在关键词中顺带提及.

**可验证性：** 优先官方资料、开放源码、可执行步骤、测试、演示和清楚的输入输出.

**维护状态：** 检查最近提交、Issue、归档状态和链接可用性；stars 只作为辅助信号.

**安全与透明度：** 检查许可证、脚本、依赖、权限、凭据处理、数据流向和商业关系.

**独特价值：** 重复、转载、纯营销或缺少实质说明的内容不会因为热度而收录.

安装任何第三方扩展前，请使用 [Skill、MCP 与扩展安全检查清单](SECURITY.md)。尚未完成审核的新项目仅出现在 [自动发现队列](DISCOVERIES.md)，不会自动进入主列表.

想自己制作 Skill？参考本仓库的 [原始 Skills 与结构校验工具](skills/README.md)。

## Contributing

欢迎提交高质量资源！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。一个好条目应当：

1. 与腾讯 WorkBuddy 直接相关，并有稳定、公开的链接；
2. 提供可验证的信息、可复现步骤或有独特价值的真实案例；
3. 使用 `标题 - 一句话说明价值。` 格式，并放入最精确的分类；
4. 清楚披露付费、推广、数据收集或高风险权限。

如果这个清单帮你节省了时间，欢迎点一个 ⭐；也欢迎通过 [Issue](https://github.com/sandbaseai/awesome-workbuddy/issues/new/choose) 推荐你验证过的资源。第一次参与可从[双语欢迎帖](https://github.com/sandbaseai/awesome-workbuddy/discussions/78)开始，问题请发到 [Q&A](https://github.com/sandbaseai/awesome-workbuddy/discussions/categories/q-a)，工作流案例请发到 [Show and tell](https://github.com/sandbaseai/awesome-workbuddy/discussions/categories/show-and-tell)；参与前请阅读 [社区行为准则](CODE_OF_CONDUCT.md)。

## Acknowledgements

初始资料发现参考了 [semlinker/awesome-workbuddy](https://github.com/semlinker/awesome-workbuddy)，感谢原维护者与所有内容作者。所有链接内容的版权归各自作者所有。

本清单采用 [CC0 1.0 Universal](LICENSE)。被索引资源遵循其各自的许可证和使用条款。
