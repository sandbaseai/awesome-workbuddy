# Awesome WorkBuddy [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精选、可验证的腾讯 WorkBuddy 学习资料、Skills、MCP 与真实工作流。

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
- [Acknowledgements](#acknowledgements)

## Start Here

- [Product homepage](https://www.workbuddy.ai/) - 产品能力、下载与套餐入口.
- [Official documentation](https://www.workbuddy.ai/docs/zh/workbuddy/) - 功能说明与使用指南的权威入口.
- [Quick start](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) - 从安装到完成第一个任务.
- [Changelog](https://www.workbuddy.ai/docs/zh/workbuddy/Changelog) - 版本能力、修复与兼容性变化.

## Official Resources

### Core concepts

- [Task bar and Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar) - 了解内置 Skill、导入与创建入口.
- [Create a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) - 用自然语言沉淀可复用工作流.
- [From model to harness](https://mp.weixin.qq.com/s/X_kaKcXH2uELcemaNaZ4iQ) - WorkBuddy Agent 产品架构解读.

### Community channels

- [WorkBuddy product page](https://cloud.tencent.com/product/workbuddy) - 腾讯云产品介绍与动态.
- [Tencent Cloud developer articles](https://cloud.tencent.com/developer/search/article-WorkBuddy) - 社区技术文章检索入口.

## Open-source Ecosystem

> [!NOTE]
> “Works with WorkBuddy” 不等于腾讯官方背书。以下项目按与 WorkBuddy 的直接相关性、文档质量、维护活跃度和社区采用度筛选；使用非官方增强、自动化或 API 工具前请检查许可证、账号条款和权限范围。

### Learning and reference

- [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) - 开源实战蓝皮书，覆盖教程、真实工作流、Skills、MCP、自动化与多智能体.
- [AI Coding Guide Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh) - 包含 WorkBuddy 在内的中文 AI Coding 与办公 Agent 学习路径.
- [learn-workbuddy](https://github.com/adongwanai/learn-workbuddy) - 从零实现 WorkBuddy 风格桌面 Agent 的 24 章 Python 教程.
- [WorkBuddy Harness Bluebook](https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness) - 拆解提示词、记忆、插件、专家、Skill 与安全边界.

### Skill collections

- [workbuddyskills](https://github.com/infometa/workbuddyskills) - WorkBuddy Skills、连接器与专家的离线学习归档.
- [website prompts and skills](https://github.com/TencentEdgeOne/awesome-website-prompts-and-skills) - 腾讯 EdgeOne 维护的网站生成 Prompt、Skill 与挑战赛作品池.
- [Ray Skills](https://github.com/imraywang/rayskills) - 面向内容生产与发布的可执行、可验证、可恢复工作流.
- [WorkBuddy Skills](https://github.com/bitcjm/workbuddy-skills) - 涵盖创作、编程、办公和通用工具的 Skill 集合.
- [Zotero MCP WorkBuddy Guide](https://github.com/maciechen/zotero-mcp-workbuddy-guide) - 将 Zotero 文献库接入 WorkBuddy 的中文配置指南.

### Tools and integrations

- [WorkBuddy Remote](https://github.com/vergess3/workbuddy-remote) - 从其他设备远程使用 WorkBuddy.
- [Skill Buddy](https://github.com/konnga/skill-buddy) - 跨 AI Agent 管理、安装和同步 Skills 与 MCP Servers.
- [WorkBuddy for Obsidian](https://github.com/bigbay957-sudo/workbuddy-for-obsidian) - 在 Obsidian 中使用本机 WorkBuddy，支持引用、编辑和溯源.
- [Tencent Meeting CLI](https://github.com/TencentCloud/tencentmeeting-cli) - 腾讯会议官方 CLI，可作为 Agent 的会议管理工具.

### Community clients and enhancements

- [WorkDaddy](https://github.com/babygoton/WorkDaddy) - WorkBuddy 桌面增强工具，提供备份、会话迁移和长任务辅助.
- [WorkBuddy Skin Studio](https://github.com/cdredfox/workbuddy-skin-studio) - 可逆的 WorkBuddy Desktop 主题管理工具.
- [OpenWorkBuddy](https://github.com/CatCatUncle/openworkbuddy) - WorkBuddy 风格的本地 AI 办公工作台实现.
- [LinkCode](https://github.com/arcboxlabs/linkcode) - 支持多种 coding agent 的开源桌面客户端.

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
- [CloudBase model configuration](https://docs.cloudbase.net/ai/ai-tools/workbuddy) - OpenAI-compatible 模型接入示例.

## Contributing

欢迎提交高质量资源！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。一个好条目应当：

1. 与腾讯 WorkBuddy 直接相关，并有稳定、公开的链接；
2. 提供可验证的信息、可复现步骤或有独特价值的真实案例；
3. 使用 `标题 - 一句话说明价值。` 格式，并放入最精确的分类；
4. 清楚披露付费、推广、数据收集或高风险权限。

如果这个清单帮你节省了时间，欢迎点一个 ⭐；也欢迎通过 [Issue](https://github.com/sandbaseai/awesome-workbuddy/issues/new/choose) 推荐你验证过的资源。

## Acknowledgements

初始资料发现参考了 [semlinker/awesome-workbuddy](https://github.com/semlinker/awesome-workbuddy)，感谢原维护者与所有内容作者。所有链接内容的版权归各自作者所有。

本清单采用 [CC0 1.0 Universal](LICENSE)。被索引资源遵循其各自的许可证和使用条款。
