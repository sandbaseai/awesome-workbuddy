![Awesome WorkBuddy - Skills, MCP, Workflows and Guides](assets/awesome-workbuddy-banner.webp)

# Awesome WorkBuddy

[English](README.en.md) · 简体中文

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Check links](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml/badge.svg)](https://github.com/sandbaseai/awesome-workbuddy/actions/workflows/links.yml) [![GitHub stars](https://img.shields.io/github/stars/sandbaseai/awesome-workbuddy?style=social)](https://github.com/sandbaseai/awesome-workbuddy)

<!-- REPOSITORY-SNAPSHOT:START -->
**144 curated repositories · 4 original Skills · 18 discovery candidates · weekly validation**
<!-- REPOSITORY-SNAPSHOT:END -->

> 精选、可验证的腾讯 WorkBuddy 学习资料、Skills、MCP 与真实工作流。

如果这个清单对你有用，请点一个 **Star**，让更多 WorkBuddy 用户更容易找到经过筛选的资源。

想帮助我们达到 100 个真实 Star？请在 [社区路线图 Issue](https://github.com/sandbaseai/awesome-workbuddy/issues/172) 提交可核验的资源、失效链接或使用反馈。

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
- [macOS 安装指南](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) - Mac 环境要求、下载、安装、登录与版本更新的官方步骤.
- [Windows 安装指南](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide) - Windows 环境要求、下载、安装、登录与版本更新的官方步骤.
- [十个上手技巧](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Efficient-Tips) - 涵盖任务表达、迭代、示例、备份、自动化和上下文管理的官方实践建议.
- [常见问题](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FAQ) - 安装登录、平台连接、文件、工作空间与会话恢复的官方排障入口.
- [Changelog](https://www.workbuddy.ai/docs/zh/workbuddy/Changelog) - 版本能力、修复与兼容性变化.
- [本清单更新记录](CHANGELOG.md) - 记录生态收录、索引、质量门禁与安全披露的版本变化.
- [Automation guide](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) - 创建一次性或周期任务，并向连接的平台推送结果.
- [MCP guide](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) - 通过可视化配置连接外部工具与数据源.
- [WorkBuddy Enterprise quick start](https://cloud.tencent.com/document/product/1831/134527) - 创建、测试、发布企业 Agent 并接入消息渠道.

## Official Resources

### Core concepts

- [创建任务](https://www.workbuddy.ai/docs/zh/workbuddy/Create-Task) - 描述目标、选择工作目录、添加上下文并启动执行.
- [任务对话](https://www.workbuddy.ai/docs/zh/workbuddy/Conversation) - 使用对话方式、发送文件和图片、查看执行过程、中断并继续任务.
- [任务管理](https://www.workbuddy.ai/docs/zh/workbuddy/Task-Management) - 搜索筛选任务、查看状态、管理工作空间并继续已有任务.
- [结果查看](https://www.workbuddy.ai/docs/zh/workbuddy/Results) - 检查产物、表格和文档预览、网页输出、全部文件与变更.
- [Task bar and Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar) - 了解内置 Skill、导入与创建入口.
- [技能市场](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) - 统一浏览、安装、启用和管理 WorkBuddy Skills.
- [Create a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) - 用自然语言沉淀可复用工作流.
- [探索](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Explore) - 浏览七类官方精选成品，一键预填对应 Prompt、Skill 与专家来制作自己的版本，并理解探索、Skill 和专家的分工.
- [专家中心](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Expert-Center) - 选择带独立方法和工具链的专家，或由团长拆解并行任务的多 Agent 专家团.
- [助理（远程任务）](https://cloud.tencent.com/document/product/1831/134392) - 从微信、企业微信、QQ、钉钉或飞书远程触发电脑上的 WorkBuddy；连接前请确认渠道授权、本地工作区、任务权限和返回产物范围.
- [两个权限模式](https://cloud.tencent.com/document/product/1831/134401) - 官方说明默认权限、工作空间边界、确认弹窗与 Full Access；重要文件先备份，完全访问只应在可信、隔离且可恢复的环境中短时开启.
- [连接器](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Connector) - 将 QQ 邮箱、腾讯文档等外部服务接入工作流，并了解配置与授权步骤.
- [记忆](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Memory) - 查看、编辑、导入或要求 WorkBuddy 忘记从对话中提取的偏好与习惯.
- [模型配置](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model) - 选择自动或内置模型，或接入自定义模型与协议.
- [数据管理](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Data) - 查找已分享文件并管理归档任务.
- [系统设置](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Setting) - 配置语言、字号、显示模式、安全安装行为与防休眠.
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
- [乐享知识库](https://cloud.tencent.com/document/product/1831/134398) - 授权 WorkBuddy 按团队空间检索和引用乐享内容，并将产物回存；使用前请核对账号授权、知识库可见范围、来源文件与写回位置.

### Community channels

- [WorkBuddy product page](https://cloud.tencent.com/product/workbuddy) - 腾讯云产品介绍与动态.
- [Tencent Cloud developer articles](https://cloud.tencent.com/developer/search/article-WorkBuddy) - 社区技术文章检索入口.

## Open-source Ecosystem

> [!NOTE]
> “Works with WorkBuddy” 不等于腾讯官方背书。以下项目按与 WorkBuddy 的直接相关性、文档质量、维护活跃度和社区采用度筛选；使用非官方增强、自动化或 API 工具前请检查许可证、账号条款和权限范围。

### Learning and reference

- [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) - MIT 许可、2,807 Star/397 Fork 的 WorkBuddy 实战蓝皮书，按“先完成第一项任务，再落地团队系统”组织安装、Skills、连接器、API、自动化、知识管理、专业诊断和多 Agent 案例；提供[在线阅读站](https://workbuddy.homes/)、社区案例集、场景问卷与阅读指南，案例强调输入、权限、安全边界和验收标准，适合从入门到团队落地.
- [How to Use Agent](https://github.com/Lukanytsu7551/how-to-use-agent-guide) - MIT 许可的中文教程站，提供 27 章 WorkBuddy 使用手册、100 个案例及 Codex/Agent 学习路径，并维护来源 NOTICE 与安全政策；部分 Agent 教程适用 CC BY-NC-SA 4.0，仓库含大量媒体文件，AI News 构建会请求外部公开 API，复用内容或本地构建前请核对对应许可、存储与网络范围.
- [Agent 学习指南](https://github.com/tangshiyegit/agent-guide) - 包含 19 篇 WorkBuddy 教程和 12 个办公、内容创作与自动化案例；仓库采用 MIT 许可证，文章中的第三方产品信息仍需按官方资料复核.
- [AI Coding Guide Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh) - 包含 WorkBuddy 在内的中文 AI Coding 与办公 Agent 学习路径.
- [learn-workbuddy](https://github.com/adongwanai/learn-workbuddy) - 从零实现 WorkBuddy 风格桌面 Agent 的 24 章 Python 教程.
- [WorkBuddy Harness Bluebook](https://github.com/zjp1997720/zhijian-ai-bluebook-workbuddy-harness) - 拆解提示词、记忆、插件、专家、Skill 与安全边界.
- [Undergraduate Thesis AI Workflow](https://github.com/Sqhao-O/undergraduate-thesis-ai-workflow) - MIT 许可的本科毕业论文 AI 辅助工作流文档，覆盖 Claude Code、Kimi、CC Switch、Pandoc、Lark-Formatter 与 WorkBuddy 排版的 6 篇教程；明确要求研究创新、实验数据和引用保持真实，配置 API Key 与使用 AI 辅助写作前请遵守学校规范并审查密钥和资料范围.

### Skill collections

- [WorkBuddy Wiki](https://github.com/YuanYiZheXue/workbuddy-wiki) - Apache-2.0 的 WorkBuddy + Obsidian 本地知识库构建系统，提供版本化 Schema、跨工作区同步、来源/概念/实体组织和健康度诊断；使用前请确认本地知识库内容与同步范围.

- [WorkBuddy Skill Hub](https://github.com/sandbaseai/workbuddy-skill) - 可检索 10,000 条公开 Skill 路径的来源索引与适配仓库，提供许可证、安全和 WorkBuddy 兼容性审查状态.
- [Senmu BuildOS](https://github.com/SenMuShare/senmu-buildos) - Apache-2.0 的跨工具 Agent 工程教练与 Skill 集合，明确支持 WorkBuddy，覆盖需求、设计、实现、测试、Git、发布、版本证据和回滚；安装后会影响项目工作区规则并可执行部署/版本操作，使用前请审查其指令、主机权限、凭据和发布目标.
- [i18n Helper Skills](https://github.com/liangdabiao/i18n-helper-skills) - 许可未声明、面向 WorkBuddy/Codex 等 Agent 的国际化 Skill 集合，分别处理静态 HTML 多语言目录和 React/Vue/PHP/Python/Java 等源码翻译函数，附带提取、应用与完整性检查脚本；脚本会批量读取和改写项目文件，使用前请备份并核对目标范围与许可.
- [PMCockpit](https://github.com/wsdlp46/PMCockpit) - Apache-2.0 的产品经理 AI 协作驾驶舱，支持 WorkBuddy、Codex 和 Claude，将需求、规格、原型、评审、复盘与经验沉淀为 8 个可执行 Skill；安装脚本会改写或软链工作区入口，测试和 VitePress 能力需显式启用，使用前请确认工作区、模板和外部项目权限.
- [QingFeng Skills](https://github.com/chenwg001/qingfengskill) - MIT 许可、以 WorkBuddy 为主的 17 个教育工作与内容生产 Skill 集合，覆盖写作、PPT、图文/视频制作、平台草稿发布，并支持按目录单独复制安装；发布类 Skill 会通过浏览器/CDP接触平台账号和内容，使用前请确认凭据不硬编码、人工审核门禁、平台条款和发布范围.
- [Image Skill](https://github.com/Mariposa-FLOA/image-skill) - 面向 WorkBuddy、Codex 等 Agent 的 17 个视觉 Skill，覆盖海报设计、图像工作流、翻页展示与分层 PSD 导出，并提供双语使用文档和逐项素材来源；Skill 与文档采用 CC BY-NC 4.0、脚本采用 Apache-2.0，示例素材仅允许查看和链接，使用时还应确认输入图像隐私、外部生成服务、HyperFrames/FFmpeg/Pillow 依赖及本地输出范围.
- [workbuddyskills](https://github.com/infometa/workbuddyskills) - WorkBuddy Skills、连接器与专家的离线学习归档.
- [WorkBuddy Skill Groups](https://github.com/darker2016/workbuddy-skill-groups) - MIT 许可、透明标注来源的 39 个 WorkBuddy 专家团 Skill 包，覆盖投研、内容、工程、法律、财税、数据、销售和 HR 等场景；内容由用户通过 WorkBuddy 官方渠道生成，不保证与平台原版一致，部分方法论和文档有第三方归属，使用前请核验法律/财税/投资/医疗等事实并遵守原作者条款.
- [Five-layer Memory System](https://github.com/juventini10/Five-layer-memory-system) - MIT 许可、面向 WorkBuddy 的五层长期记忆 Skill，通过 33 道问答沉淀偏好、取舍和行为模式，并按层级维护可持续更新的工作记忆；内容可能包含敏感个人信息并写入本地文件，使用前请确认保存位置、备份与共享范围，不要把生成建议作为医疗、法律、财务或其他重大决策依据.
- [Personal User Manual Skill](https://github.com/NI9N/gerenshiyongshuomingshu) - MIT 许可、零依赖的 WorkBuddy 个人使用说明书 Skill，基于多轮自我认知教练流程整理价值观、才能和热情，经过证伪关后生成可自行维护的 Markdown；它不做测评、不替用户匹配职业或下唯一结论，回答可能包含敏感自我认知信息，使用前请确认保存和分享范围，并把输出当作待验证假设.
- [website prompts and skills](https://github.com/TencentEdgeOne/awesome-website-prompts-and-skills) - 腾讯 EdgeOne 维护的网站生成 Prompt、Skill 与挑战赛作品池.
- [Ray Skills](https://github.com/imraywang/rayskills) - 面向内容生产与发布的可执行、可验证、可恢复工作流.
- [WorkBuddy Skills](https://github.com/bitcjm/workbuddy-skills) - 涵盖创作、编程、办公和通用工具的 Skill 集合.
- [Zotero MCP WorkBuddy Guide](https://github.com/maciechen/zotero-mcp-workbuddy-guide) - 将 Zotero 文献库接入 WorkBuddy 的中文配置指南.
- [DSH Skill Picker](https://github.com/a735624258/dsh-skill-picker) - 为 DeepSeek Harness Web GUI 增加可搜索、拼音检索和键盘导航的技能选择器，复刻 WorkBuddy 式 `/技能名` 调用交互；MIT 许可。插件会读取用户与项目 Skill 目录并提供本地 Web 路由，安装前请审查其文件系统访问范围.
- [Kunpeng Skill](https://github.com/hufeng173/kunpeng-skill) - 面向 WorkBuddy、Codex、Claude Code 等 Agent 的 Apache-2.0 多源蒸馏 Skill，可从代码、网站、UI、图片、音视频和文档建立带证据的可迁移方法与生成规范；本地分析器需要按需安装依赖，使用前请确认资源与本地文件范围.
- [Skill Doctor](https://github.com/evilstar2016/skill-doctor) - 面向 WorkBuddy 等 Agent 的本地 Skill 冲突、重复、安全风险与上下文成本审计 CLI；MIT 许可，默认只读取本地文件并绑定回环地址，使用前仍应确认扫描范围与导出报告内容.
- [WorkBuddy Usage Status](https://github.com/clancy-feng/workbuddy-usage-status) - 将 WorkBuddy 本地用量生成离线、可审计的 Token/Credit、模型效率与错误分析看板；MIT 许可，默认只读本地数据且不联网，精确用量 API 仅在用户主动提供令牌时启用.
- [Agent Analytics Report](https://github.com/Elisabeth15501/agent-analytics-report) - MIT 许可、原生支持 WorkBuddy 的用量分析 Skill，读取本地会话/用量数据生成 Token、缓存、模型成本与异常报告，支持 Markdown、HTML 和 JSON，并以合成数据覆盖 306 个测试用例；报告中的单价只是估算，使用前请确认本地读取范围并脱敏输出.
- [UsageMonitor WorkBuddy Provider](https://github.com/masclown/usage-monitor-plugin-workbuddy) - Apache-2.0 的独立 UsageMonitor provider，读取 WorkBuddy 订阅额度、赠送包和请求历史，并支持按模型、渠道与操作切片；它通过浏览器登录态访问 `workbuddy.cn` 的官方网页接口并处理 Cookie，使用前请核对账号授权、网络请求、保存范围和服务条款.
- [Session Digger](https://github.com/taxueseek/session-digger) - ISC 许可的跨 Agent 会话检索与知识管理工具，原生解析 `~/.workbuddy/projects`，用 SQLite FTS 建立增量索引并生成自包含本地报告；它会读取完整会话并写入索引、报告和可选记忆文件，内容可能包含提示词、路径与项目资料，环境诊断还可探测外部端点，使用 `apply`/`prune` 等写入或删除命令前应逐项确认目标与备份.

### Ready-to-use Skills

- [Majia Huiyuan](https://github.com/maojiebc/majia-huiyuan) - MIT 许可的会员运营与数据体系 Skill，提供 WorkBuddy 单专家发布包、55 个模拟逻辑数据集、25 条 ETL、12 类角色看板以及 RFM、留存、券效益和数据质量参考；所有数值均非真实经营基准，SQL 面向 Spark 3.4，历史平台 JSON 不可直接作为当前导入包，生产使用前必须完成字段映射、口径确认和回归验收，构建脚本还会重建指定的输出目录与 ZIP.
- [Pandadata API Skill](https://github.com/quantskills/skill-pandadata-api) - GPL-3.0 的可安装 WorkBuddy/Codex 金融数据 Skill，内置 218 个接口的本地文档、检索工具、兼容性索引和可选真实调用；运行时会安装 `panda_data` 及数据依赖并连接用户配置的外部服务，配置器可将用户名和明文密码保存到权限为 600 的 `~/.pandadata/pandadata.env`，SDK 还会写入 `user.json`，因此请保护凭据、核对数据授权，且勿将结果视为投资建议.
- [Photo to Monthly Zine Postcard](https://github.com/shenchangyi/photo-to-monthly-zine-postcard) - MIT 许可、可直接安装的 WorkBuddy/Codex Skill，将用户照片制作成 3:4 月历 Zine 明信片，并要求先核验匹配的文学与音乐来源；仓库不含执行脚本或凭据处理，但照片可能包含人物、位置、EXIF 或品牌信息，且资料检索与图像生成可能访问外部服务，使用前请确认素材隐私和网络边界.
- [XHS Blogger Analyzer](https://github.com/arraycto/xhs-blogger-analyzer) - MIT 许可的 WorkBuddy/Claude Skill，通过 MCP 抓取小红书博主公开内容并生成内容策略、选题与结构化分析文档；安装脚本会下载依赖和第三方 MCP 二进制，首次运行需要扫码登录，使用前请核对平台条款、账号权限、抓取范围、下载来源和个人/创作者数据隐私.
- [AI 10x Learning](https://github.com/luozhilzh/ai-10x-learning) - MIT 许可、兼容 WorkBuddy/Codex/Claude/Cursor 的十步学习闭环 Skill，结合多视角研究、主动回忆、费曼复述和 HTML 学习卡；带安装脚本、引用/核实规则与本地校验器，使用前请确认外部事实、个人学习资料和安装脚本的文件范围.
- [Book Video Generator](https://github.com/chenjun198711/book-video-generator) - MIT 许可、兼容 WorkBuddy/Codex/Claude 等 Agent 的读书视频 Skill，从书籍检索、文案与分镜到 AI 插图、TTS、字幕和 ffmpeg 合成输出 MP4；会访问外部模型/语音服务并可读取 API Key，使用前请核验书籍事实、版权与引用、密钥存储和生成内容质量.
- [Hotspot Monitor Skill](https://github.com/jiangxu1024/hotspot-monitor-skill) - MIT 许可的 WorkBuddy 热点监控 Skill，可抓取多个中文平台、按关键词筛选，并定时写入飞书多维表和推送移动端；配置会涉及飞书 App Secret、Base Token、Table ID 与 Webhook，且抓取/推送受平台条款和个人数据边界约束，使用前请改用安全的本地配置并审查权限.
- [Bazi-Ziwei Skill](https://github.com/mingze21/bazi-ziwei-skill) - MIT 许可、兼容 WorkBuddy/Codex/Claude/Cursor 的八字与紫微斗数 Skill，使用本地算法排盘、提示词和可分享的 HTML 海报，并附测试指南与合成示例；出生时间等个人信息会进入本地产物，命理内容不具科学诊断效力，不应用于医疗、法律、财务或重大人生决策.
- [Prompt Toolkit](https://github.com/xiaolouJB/prompt-toolkit) - CC BY-NC 4.0 的 12 个通用 Prompt 多智能体分发包，含 WorkBuddy 原生 Skill 目录以及 Claude Code、Cursor、Trae、CodeBuddy 适配格式，覆盖提问、学习、核查、决策和人生设计；内容整理改编自数字生命卡兹克并要求署名、保留来源且不得商用，使用前请遵守原作者许可.
- [Paper CN Reader](https://github.com/langlibai66/paper-cn-reader) - MIT 许可的学术论文精读、翻译与批注 Skill，支持 WorkBuddy，保留 PDF 图片、表格、公式并输出 HTML/PDF；需要 PyMuPDF、Playwright 和 Chromium，默认从 jsDelivr 加载 MathJax，且会在用户指定目录写入文档和提取资源，使用前请确认依赖和网络/写入范围.
- [Translate Book Windows](https://github.com/NikoKennedy/translate-book-windows) - MIT 许可（含上游作者署名）、面向 Windows 的 WorkBuddy 全书翻译 Skill，将 PDF/DOCX/EPUB 分块处理，维护术语表、manifest/哈希完整性校验并支持断点续传和 HTML/DOCX/EPUB/PDF 输出；需要 Calibre、Pandoc 和 Python，可能读取整本书并写入大量本地产物，使用前请确认版权/授权、外部模型与数据流、依赖来源及输出目录.
- [BossMate](https://github.com/yinren112/bossmate) - MIT 许可的本地求职 Skill，支持 WorkBuddy，通过可见浏览器读取完整 JD、去重并在发送前设置人工确认门禁；不会索取密码、Cookie 或会话令牌，但仍需遵守招聘平台规则并审查简历、浏览器资料和沟通内容范围.
- [Career Copilot](https://github.com/ronineymessjr-sudo/career-copilot) - MIT 许可、原生支持 WorkBuddy Expert 与 MCP 的证据驱动求职工作台，覆盖岗位搜索、JD 拆解、画像、简历生成、投递跟踪和面试复盘，并对投递/邮件等关键动作设置人工确认；CLI 需要 Tavily Key，求职画像、简历和岗位数据可能含敏感个人信息，使用前请核对外部搜索、保存位置和最终投递内容.
- [AI创品 Product Creator](https://github.com/zhangx1234994/aicp-product-creator-skill) - MIT 许可、提供 WorkBuddy Skill/插件包与 MCP 配置的商品设计工作流，可从图片或创意匹配实时商品、预览并生成报价，明确由用户确认后才扣积分和进入短期结算链接；账号、图片资产、商品、订单、支付和风控由外部服务托管，使用前请核对授权页面、上传隐私、积分扣除、最终商品与付款信息，不要把仓库内容视作官方服务本身.
- [IELTS Buddy Agent Skills](https://github.com/Jobo16/ielts-buddy) - MIT 许可的 IELTS 学习 Skill 集合，支持 WorkBuddy，覆盖学习计划、作文/口语/阅读/听力复盘、词汇和模考，并提供安装与验证脚本；可选绑定个人学习 API 和本地令牌，使用前请确认数据范围，不要分享密码、Cookie 或 Token.
- [PDF Structured Extractor](https://github.com/ttww1111/pdf-structured-extractor) - MIT 许可、兼容 WorkBuddy/Codex/Claude 的 PDF 提取 Skill，仅依赖 PyMuPDF，将文本、表格和图片输出为结构化 Markdown/CSV；可识别双栏、扫描页和乱码并生成质量警告，默认无网络与遥测，但会读取用户指定的 PDF 并写入输出文件，使用前请确认文件和输出目录.
- [Roundtable KG](https://github.com/xiewende424/roundtable-kg) - MIT 许可、兼容 WorkBuddy 的离线圆桌求真 Skill，用立场型角色讨论严肃议题并将论证关系渲染为可交互力导向图；仅需 Python 3.8+、无第三方依赖，图谱展示的是讨论结构而非事实证明，使用时仍应复核来源与结论.
- [AI Weekly Report](https://github.com/Elisabeth15501/ai-weekly) - MIT 许可、兼容 WorkBuddy/Codex 等 Agent 的 AI 行业周报 Skill，从 RSS 和可选搜索数据生成可检索、可筛选、暗色模式的单文件 HTML，并保留原始链接与失败回退；需要联网抓取和少量 Python 依赖，使用前请复核来源、时效、市场数据及外部发布目标.
- [AI Short Drama Skills](https://github.com/zkhyww/ai-short-drama-skills) - MIT 许可、面向 WorkBuddy 等 Agent 的短剧创作与制作双 Skill，将选题、剧本、桌读、分镜、资产、声音、剪辑和 QC 分阶段交接，并提供确定性预检与母稿/投稿稿分离；媒体执行可能调用 Dreamina OAuth、模型与 ffmpeg，涉及积分、版权和外部服务，交付前仍需人工试演与审核.
- [Infoseek](https://github.com/GYINT/infoseek) - MIT 许可、兼容 WorkBuddy 的端到端研究 MCP/Skill，包含多源发现、四级抓取、四维评分、跨源矛盾检测、结构化报告和长期归档，并提供回归测试与 Key 管理；高级抓取可能使用浏览器、Whisper、搜索 Key 和外部模型，使用前请审查凭据注入、网络范围、个人数据与归档目录，并人工复核研究结论.
- [MarkItDown Skill](https://github.com/stwhwing/markitdown-skill) - MIT 许可、兼容 WorkBuddy 的文档与网页转 Markdown Skill，基于 Microsoft MarkItDown 并提供 SPA/网页回退、批量转换和本地 token 估算；默认启用 SSRF 防护但可显式放开内网地址，浏览器回退和文件输出仍会读取外部页面/本地资料，使用前请确认 URL、依赖、输出目录和版权范围.
- [Bilibili Video Summary](https://github.com/Willson-Huang/bilibili-video-summary) - MIT 许可、提供 WorkBuddy 版的本地视频知识整理 Skill，通过字幕或本地 Whisper 转写生成带时间戳、实体表和待核实声明的 14 节 Markdown 笔记；需要下载视频/字幕及可选 Cookie、faster-whisper 和模型文件，使用前请确认版权、隐私、磁盘空间和来源事实，生成笔记仍需人工复核.
- [Knowledge Base Builder](https://github.com/miaqu766520-a11y/kb-builder) - MIT 许可、已在 WorkBuddy 验收的本地知识库搭建 Skill，通过逐题访谈生成目录、模板、个人档案和使用手册，并在用户确认计划后写入 Markdown 文件；迁移旧资料会读取并重组本地内容，安装前请确认知识库根目录、机密排除规则、备份和写入范围.
- [AI Finance Workbench](https://github.com/feng-liu-1994/workbuddy-finance-workbench) - MIT 许可、支持 WorkBuddy MCP App 的可视化财务工作台，提供 20 个模块、25 个带字段口径/小样本试跑/校验/人工复核的工作流，以及异常责任闭环和本机备份；仓库只含虚构数据，但真实使用会处理财务资料并可能写入本地存储，使用前请先在样本或沙箱验证、确认会计口径与权限，不要把 AI 输出当作专业意见.
- [Universal Travel Planner](https://github.com/chaoliuzhu65-tech/universal-travel-planner-skill) - MIT 许可、13 Star 的 WorkBuddy 商旅规划 Skill，整合 12306、航班、地图/天气、酒店比价、预算分档、清单和响应式 HTML 报告，并提供真实跳转链接；需要外部 MCP、搜索结果和可选高德 API Key，价格/余票/房态与链接可能变化，使用前请核对来源、平台条款、个人行程隐私和最终预订信息.
- [1688 Product Reader](https://github.com/yyc424666lvy/1688-product-reader) - MIT 许可、只读的 WorkBuddy 商品研究 Skill，可从已登录的 1688 页面提取标题、价格、起订量、卖家、SKU、图片和参数；独立浏览器 Profile 由用户手动登录，Skill 不负责下单或管理登录态，使用前请确认平台条款、页面访问和商品信息时效.
- [A-share Watch Copilot](https://github.com/WaterCMY/A-share-watch-copilot) - 面向 WorkBuddy 的 A 股/港股盯盘 Skill，提供持仓与基金 Schema、8 个自动化模板、报告及可选本地工作台；许可证在 MIT 文本后附加个人学习研究限制，金融数据和结论必须人工复核且不可用于自动下单或非法投顾。持仓文件含敏感财务数据，脚本会访问腾讯、东财、新浪等端点，本地服务默认监听 `0.0.0.0:8801`、无认证并可写回持仓，仅应在可信私网使用或改为回环地址.
- [Math Concept Film](https://github.com/liangdabiao/math-concept-film) - 许可未声明、兼容 WorkBuddy/Codex/Claude 的数学概念短片 Skill，以语音先行的字幕时间轴驱动 Manim 动画，提供六幕教学框架、静帧自检和 ffmpeg 合成流程；配音依赖微软在线 TTS，使用前请确认网络、素材版权、输出目录和许可边界.
- [Eagle Untagged Organizer](https://github.com/ChosenXu/eagle-untagged-organizer) - MIT 许可的 WorkBuddy Skill，通过 eagle-mcp 为未标记的设计素材生成名称、结构化注释和受控标签；支持多模态预检、预览清单、批量备份、人工批准与回滚，执行前请确认 Eagle 库、MCP 权限和即将写回的素材范围.
- [Rainskills](https://github.com/goodrain/rainskills) - Apache-2.0 许可、兼容 WorkBuddy/Codex/Claude 等 Agent 的部署 Skill 集合，可识别项目、构建部署、排查日志、验证页面/API，并管理版本、快照和回滚；可连接 Rainbond Cloud、已有 Rainbond 或本机/服务器环境，执行前请确认凭据、网络、主机权限和回滚目标.
- [Session Fork](https://github.com/yamingmou/session-fork-core) - MIT 许可的 WorkBuddy 会话分叉 Skill，可按上一轮输出、请求 ID 或文本匹配点复制独立分支，支持预览、自动备份和分支谱系树；它依赖非官方的本地存储结构，会读取会话、向 `~/.workbuddy/workbuddy.db` 插入记录、写入谱系索引，且 `--fix` 会改写分支文件，而备份仅包含源 JSONL，执行前请退出 WorkBuddy 并另行备份数据库和敏感会话.
- [Cross-Device Sync for WorkBuddy](https://github.com/jamesting-eng/workbuddy-skills) - MIT 许可、面向 Windows 的跨设备任务续接 Skill，以 WPS 云盘 Junction 为主通道、HANDOFF/记忆文件为交接通道，并用守护进程与看门狗维持同步；它需要 WPS 本地云盘、管理员权限并会双向同步 `.workbuddy`、日志和工作区文件，使用前请确认云盘隐私、冲突/备份策略、密钥文件和同步范围.

本仓库维护四个可直接安装的原创 Skill：[Document Quality Review](skills/document-quality-review/SKILL.md) 以只读方式检查交付物质量；[Skill Security Audit](skills/skill-security-audit/SKILL.md) 在安装前审查第三方扩展；[Source-backed Research Brief](skills/source-backed-research-brief/SKILL.md) 将网页和资料整理为可核验、明确区分事实与推断的研究简报；[Curate WorkBuddy Resource](skills/curate-workbuddy-resource/SKILL.md) 对候选资源给出基于相关性、质量、许可证、来源和安全证据的收录、暂缓或排除结论。

- [WorkBuddy Guide](https://github.com/Neo5093/workbuddy-guide) - 可直接安装的 WorkBuddy 使用与故障排查 Skill，覆盖连接器、专家、自动化、记忆、交互模式和常见问题；MIT 许可。其可选诊断脚本会读取本机 `~/.workbuddy` 配置与近期日志并探测本地健康端点，分享输出前请先检查并脱敏。
- [E-commerce Visual Copywriting](https://github.com/feichanggege/ecommerce-visual-copywriting-skill) - 将电商卖点分析、文案和商品图制作沉淀为可执行 SOP.
- [Image Story Video Wizard](https://github.com/aaronyi97/image-story-video-wizard) - 面向 WorkBuddy/Codex 的音频优先故事视频生产 Skill，关键步骤带确认门禁.
- [Social Account Doctor](https://github.com/JuneYaooo/social-account-doctor) - 分析主流中文内容平台账号与爆款，并输出诊断和选题建议.
- [Bruce Draw.io](https://github.com/bruc3van/bruce-drawio) - 生成、校验并导出 draw.io 图表的跨平台 Skill.
- [Textbook Writer Skills](https://github.com/cabbage2000-lab/textbook-writer-skills) - 以 UbD 逆向设计驱动教材规划、逐章写作和审核.
- [OfferLoop](https://github.com/riwonswain-ovo/OfferLoop) - 由七个 Skills 和飞书工作区组成的开源求职系统.
- [Job Navigation Skill](https://github.com/AriaXXX-free/job-navigation-skill) - 基于证据研究当前职位与 JD，对照简历和项目证据并规划求职行动；MIT 许可，面向 WorkBuddy、Codex、Claude 和 Cursor。它会按用户请求检索公开岗位信息，使用前请检查输入资料的隐私范围与外部检索结果.
- [WorkBuddy WeChat Publisher](https://github.com/cnproduct/workbuddy-wechat-publisher) - 从写作、配图、排版到微信公众号草稿发布的 Skill 包.
- [CordysCRM Skills](https://github.com/1Panel-dev/CordysCRM-skills) - 覆盖销售 L2C 流程的 CRM Agent Skills.
- [Self-media Compliance Review](https://github.com/JuneYaooo/self-media-compliance-review) - 发布前审核视频、封面、字幕、带货信息与平台合规风险，并保留证据定位.
- [Ontology-driven Development](https://github.com/sharptoolbox/ontology-driven-dev) - 从需求探索、本体建模到应用构建的可追溯业务系统开发 Skill.
- [Codebase Reverse](https://github.com/sharptoolbox/codebase-reverse) - 将 Java Web 或微服务代码逆向为功能、架构、接口和数据模型文档.
- [Trade Pipeline](https://github.com/Dangooy/trade-pipeline-skill) - 由一份订单档案联动生成报价单、PI、CI 与装箱单.
- [SeaTable Production](https://github.com/Darling5/seatable-production) - MIT 许可的 WorkBuddy 生产交付协同 Skill，覆盖立项、计划、采购、BOM/库存、发货、维修和分析；默认使用本地 CSV，写入前展示完整变更并等待确认，也可选接入 SeaTable、PartDB 或 ERP，使用前请核对凭据、字段映射、外部 API 和写入范围.
- [Local Markdown Memory](https://github.com/asen-goat-mine/boujoy-local-markdown-memory) - 面向 WorkBuddy/Codex 的本地优先、可审计 Markdown 长期记忆模板.
- [Org Context](https://github.com/wangjialiang678/org-context) - MIT 许可、支持 WorkBuddy/Claude Code/OpenCode 的企业上下文组织 Skill，以事实树、判断账和状态页降低 Agent 找错资料的概率，附带模板、可运行示例和机械校验；默认处理本地企业资料并会改写工作区文件，使用前请备份并确认资料范围.
- [Delivery Razor](https://github.com/Ketian823/delivery-razor) - MIT 许可的 WorkBuddy 交付清理 Skill，剔除跨会话记忆标签、本轮残留和防御性免责话术，并为老板汇报提供可选的精炼规则；安装包含扫描/安装脚本，使用前应保留原稿、人工复核事实与语气，不要让自动清理替代最终验收.
- [WorkBuddy App Builder Skill](https://github.com/sharptoolbox/WorkBuddy-AppBuilderSkill) - 以本体驱动需求探索、人工确认和本地 SQLite/API 生成领域应用；安装前请复核生成代码与本地接口权限.
- [WorkBuddy Theme Skill](https://github.com/comeonzhj/WorkBuddy-theme-skill) - 创建、校验、预览、应用和恢复可逆的 WorkBuddy 运行时主题；会通过本地 CDP 注入样式，必要时重启应用并运行本地 guard，但不修改 app.asar、签名、账号或对话数据，使用前请确认重启影响.
- [ZhiGui Second Brain Skill](https://github.com/CarlWangChina/zhigui-openclaw-ui-second-brain-skill) - 结合本地 MCP、规划数据和知识图谱的桌面第二大脑，支持 WorkBuddy；采用 PolyForm Noncommercial 1.0.0，且会读写个人规划数据，安装前请确认许可与权限.

### Tools and integrations

- [PowerContext](https://github.com/oceanbase/powercontext) - Apache-2.0 许可、OceanBase 团队维护的跨 Agent 记忆与任务交接系统，为 WorkBuddy 提供一键安装的 `UserPromptSubmit` Hook、Streamable HTTP MCP 和 `project-context` Skill，可检索/写入 Memory 并创建、提交 Handoff；安装会改写 `~/.workbuddy` 下的 hooks、settings、MCP 与 Skills，且提示词采集默认开启并作为 Source 持久化，自动召回内容仅是不可信历史，使用前应决定是否关闭采集、核对本地/远程 Server 与模型数据流、配置鉴权并让 CLI/Server/插件保持同一 Git revision，当前 WorkBuddy 集成仍位于未发布的 `master`.
- [WorkIsland](https://github.com/qianzhu18/workisland) - Apache-2.0 许可、面向 macOS Apple Silicon 的本地 Agent 状态与注意力路由器，原生支持 WorkBuddy/CodeBuddy、Codex、Claude Code 等，可监控任务、处理审批/提问并跳回源会话；它会安装本地 hooks、观察任务/转录信号、读写剪贴板历史与终端状态，审批回复会改变 Agent 执行，打包版还默认开启可关闭的匿名 PostHog 遥测并联网检查更新，安装前请审查 hook 变更、遥测白名单、日志/剪贴板范围与每项审批，Windows 版本目前暂停公开发布.
- [WorkBuddy OpenAPI PHP SDK](https://github.com/JaguarJack/workbuddy-openapi) - MIT 许可的第三方 PHP 8.1+ SDK，封装官方 WorkBuddy OpenAPI 的 OAuth、用户资料与手机号验证、本地助手消息/权限、云任务、产物、兑换和 ACP；它本身不持久化令牌，但会处理客户端密钥、用户/任务令牌及提示词，并可发送消息、创建任务、响应权限、兑换权益和执行 ACP，且会信任官方 API 返回的 ACP/沙箱 URL 并向其发送任务令牌，接入时应使用最小权限、服务端密钥存储、OAuth state/幂等校验、主机白名单和逐项人工确认.
- [WorkBuddy Jupyter Bridge](https://github.com/Kallium-cn/workbuddy-jupyter-bridge) - MIT 许可、面向 WorkBuddy 5.x 的 JupyterLab MCP 接线 Skill，提供真实内核中的代码执行、Notebook/Cell 读写、变量留存和 DataFrame 自省，并用 9 项端到端校验固化配置与排障；它会合并写入 `~/.workbuddy/mcp.json`，连接器可改变当前内核状态，虽默认只监听 `127.0.0.1` 且需用户在 UI 中显式信任，仍应先备份配置并确认 Notebook、数据和 WSL 网络范围.
- [WorkBuddy Computer Use for Intel Mac](https://github.com/Guyzn/workbuddy-cua-mcp) - MIT 许可、面向 Intel Mac 的 WorkBuddy MCP，提供截图、鼠标/键盘/窗口控制和 Chrome CDP 自动化，用于补足 Apple Silicon 原生 Computer Use 的平台差异；它需要 macOS 辅助功能权限、可自动启动带调试端口的 Chrome，并能控制整台桌面，使用前请确认进程授权、调试端口绑定、浏览器 Profile、敏感页面和每次操作的人工监督.
- [WorkBuddy Token Tracker](https://github.com/abc1317679842-ui/workbuddy-token-tracker) - MIT 许可、面向 Windows WorkBuddy 的 Skill 与 hook，通过本地 trace/transcript 汇总每轮 Token、耗时、分模型日账本和系统通知；它会扫描完整会话、长期写入账本及诊断日志、调用 Node/Python/PowerShell，且默认联网刷新多个公开价格源，余额查询虽默认关闭但开启后会读取 DeepSeek API Key，费用仅为可变价格数据与人工时段规则下的估算，不能视为账单，安装前请审查源码、日志保留、网络和凭据范围.
- [AgentSessionQuery](https://github.com/iuuunlyk/AgentSessionQuery) - MIT 许可、基于 PowerShell 7 的本地会话查询工具，以统一命令检索 Codex、Claude Code 与 WorkBuddy 的会话、工作区、模型和 Token 统计；它不联网并以 SQLite 只读模式打开 WorkBuddy 数据库，但会扫描完整 transcript、调用本机 Python、短暂写入并删除临时 JSON，输出还可能暴露会话标题、路径、分支和恢复命令，分享或重定向结果前请先脱敏.
- [Agent Avatar](https://github.com/joyparkray/agent-avatar) - MIT 许可的 macOS/Windows Live2D 桌面伙伴，通过只读观察器连接 WorkBuddy、Codex、Claude Code、Hermes 和 DeepSeek Harness，并把 Agent 状态映射为动画；项目不附带模型，Live2D Cubism Core 受单独许可约束，应用未沙箱化且 Windows 构建未签名，安装器还会调用宿主 CLI、写入插件配置并携带 Python 运行时，启用前请核对二进制、模型许可、hook 权限和本地状态文件范围.
- [CLI2API](https://github.com/caigee-cmd/cli2api) - MIT 许可的自托管本地网关，将 WorkBuddy（及 Qoder/Trae）登录态转换为 OpenAI/Anthropic 兼容接口，支持多账号路由、独立 worker、Docker 和回环控制台；默认仅监听 `127.0.0.1` 并要求 API Key，但会处理 OAuth/PAT/凭据导入，使用前请保护导出文件、端口和账号条款边界，勿用于共享转售.
- [WorkBuddy2API](https://github.com/ShouZhuo0413/codebuddy2api) - MIT 许可的本地协议转换器，将已登录的 WorkBuddy/CodeBuddy 会话转为 OpenAI、Responses 和 Anthropic 兼容接口；它会读取本机登录态并向 `copilot.tencent.com` 转发，使用前请审查源码、凭据文件、端口暴露和腾讯账号条款.
- [CodeBuddy2OpenAI](https://github.com/HanHan666666/codebuddy2openai) - MIT 许可的单文件本地协议转换器，将已登录的 CodeBuddy/WorkBuddy 会话包装为 OpenAI 兼容的 `/v1/chat/completions` 接口，默认仅监听 `127.0.0.1`；它会读取本机登录态、刷新令牌并可记录完整请求/响应日志，且不兼容新版 Codex CLI，使用前请审查源码、凭据文件、日志、端口暴露和腾讯账号条款.
- [Buddy2api](https://github.com/wicm84266964/Buddy2api) - MIT 许可的本地多通道网关，将 WorkBuddy/CodeBuddy、QClaw、QwenWork 和 TraeWork 登录态分别接入 OpenAI 兼容接口，支持 Codex Responses、Docker 和 API Key 通道路由；项目明确要求仅本机使用、不要公开部署或分享凭据，使用前请审查本地认证文件、数据库、端口和各平台账号条款.
- [WorkBuddy CLIProxy provider](https://github.com/lovingfish/workbuddy-cliproxy) - MIT 许可的 CLIProxyAPI 插件，将 CodeBuddy 模型接入 OpenAI/Anthropic 客户端并支持扫码登录与令牌刷新；凭据保存在本地插件目录，且包含针对上游审核模板的适配逻辑，使用前请核对源码、账号条款与数据流.
- [WorkBuddy Remote](https://github.com/vergess3/workbuddy-remote) - 从其他设备远程使用 WorkBuddy.
- [Skill Buddy](https://github.com/konnga/skill-buddy) - MIT 许可、93 Star 的跨 Agent 桌面工作台，支持 WorkBuddy 用户级 Skills、Skills/MCP 清单、跨平台安装、漂移检测、精确变更预览、垃圾箱撤销、公共资源发现、私有 Git 备份和受保护分支团队库；目前为 public preview，会扫描并可能读写多个 Agent 配置目录，使用前请备份、审查自定义路径与同步目标，并确认团队仓库和凭据范围.
- [AgentHub](https://github.com/nicechencs/AgentHub) - MIT 许可的本地跨平台 Agent 管理 GUI/CLI，支持 WorkBuddy 等工具的安装环境、登录连接、共享/项目 Skills、会话、用量和备份，并明确 MCP 当前仅做只读发现；它会读写本机 Agent 配置和日志，凭据沿用本地存储且当前不加密，使用前请审查配置变更、备份位置、日志脱敏和本地权限.
- [WorkBuddy Expert Bridge](https://github.com/xiaojinlucky/workbuddy-expert-bridge) - MIT 许可的本地 Skill，让 Codex、Cursor、Claude Code、Grok 和 VS Code 等工具只读发现并推荐本机已有的 WorkBuddy 专家/专家团，先展示匹配依据和本地可用性，再由用户决定是否使用；它不需要账号或密钥，也不会自行安装、下载或启用陌生内容，但会读取本机 WorkBuddy 文件，使用前请确认文件权限、上下文数据范围和宿主工具的数据政策.
- [WorkBuddy for Obsidian](https://github.com/bigbay957-sudo/workbuddy-for-obsidian) - 在 Obsidian 中使用本机 WorkBuddy，支持引用、编辑和溯源.
- [Workbuddian](https://github.com/jiang198012/workbuddian) - MIT 许可的 Obsidian 桌面插件，将本机 WorkBuddy/CodeBuddy CLI 接入笔记库，支持流式对话、`@` 引用、会话分叉、MCP 管理、逐项批准和编辑撤销；仅支持 Windows/macOS，能读取 Vault 并执行获批的本地命令/MCP，安装前请审查路径和权限.
- [Codex × WorkBuddy Token Monitor](https://github.com/tylerchen0123-sudo/CODEX-Inspection-Guidelines-for-Dosage) - MIT 许可、零第三方 Python 依赖的本地实时 Token 监控看板，读取 Codex 与 WorkBuddy 会话日志并通过 SSE 展示用量、缓存命中和活跃会话；本地会话可能含敏感内容，且统计值不是官方计费记录，使用前请确认扫描范围和端口暴露.
- [Tencent Meeting CLI](https://github.com/TencentCloud/tencentmeeting-cli) - 腾讯会议官方 CLI，可作为 Agent 的会议管理工具.
- [DCC-MCP Agent Plugins](https://github.com/dcc-mcp/dcc-mcp-agent-plugins) - MIT 许可、官方分发式的 DCC-MCP Agent Skills/插件集合，兼容 WorkBuddy、Codex、Claude Code 等宿主，可发现数字内容创作工具并在审批边界内调用；安装会引入 npm/插件运行时和本地或外部工具权限，使用前请核对插件来源、凭据、文件与网络范围.
- [SkillHive](https://github.com/tonycc/skillhive) - MIT 许可的企业内部 Skill 中枢，通过 WorkBuddy MCP 连接器集中分发、版本管理、评审、反馈和操作审计，并提供可审计的连接器构建/校验流程；部署需要 PostgreSQL、管理员令牌和获批的 HTTPS 企业 MCP 地址，真实客户端兼容性与上线审核仍需人工验证，禁止把构建产物或内部地址当作公共安装入口.
- [GitHub MCP Server Lite](https://github.com/1186247283zj-pixel/github-mcp-server-lite) - MIT 许可、仅依赖 Python 标准库的 GitHub MCP Server，提供仓库、文件、分支、Issue、PR、搜索和通知等 24 个工具，适合 WorkBuddy 在 OAuth/npm 不稳定的环境中通过 PAT 连接；配置会授予 GitHub API 权限，且 `run_api` 可访问任意 REST 端点，使用前应最小化 Token scope、保护 Token，并逐项审核写入/删除操作.
- [BailingHub WorkBuddy Connector](https://github.com/bailinghub/bailinghub-workbuddy-connector) - MIT 许可的独立 WorkBuddy 企业连接器，通过浏览器 PKCE 授权、能力校验、幂等 invocation、审批、限流和审计让 Agent 查询或操作已接入的业务系统；真实业务端点、租户授权和 Client/Agent Token 由部署方管理，安装前必须核对业务方授权页、凭据存储、权限版本和回退流程，不得分发内部令牌或 Cookie.
- [AssetPlex](https://github.com/wynter-cai/assetplex) - MIT 许可、完全本地的跨 Agent 资产中枢，将 identity、Skills、rules 和 MCP 配置集中管理并同步到 WorkBuddy、Codex、Claude Code、TRAE 和 Qoder，支持反向导入、格式转换、符号链接和本地 Web UI；同步可能读写多个 Agent 配置目录并覆盖/链接文件，使用前请备份、审查适配器与路径权限，并确认敏感配置不会被意外导出.
- [VOKO](https://github.com/laoyudashu/voko) - AGPL-3.0 许可、面向 WorkBuddy 等本地 Agent 的通信运行时，支持 MCP、A2A 1.0、REST/Webhook、精确会话路由、权限策略、人工介入和本地审计；可选公网入口、注册/跨端消息和运营服务会扩大数据与暴露面，且 E2EE 只覆盖明确的私聊边界，部署前请核对云端依赖、TLS/密钥模型、Provider 权限、端口和许可证义务.
- [Task Passport](https://github.com/dongsheng123132/task-passport) - MIT 许可、兼容 WorkBuddy/Codex/Claude 等 Harness 的版本化任务交接协议，以已验证状态、事实、决策和下一步生成可携带的 TaskPack，支持过期写入冲突、ask/receipt 回执、结构合规检查和跨机导入；TaskPack 不内建签名且包内内容都是数据而非指令，使用前请在包外核对完整性、审查敏感附件并确认本地 store 权限.
- [Garmin Connect Plugin for DSH](https://github.com/Likenttt/garmin-connect-plugin-for-dsh) - MIT 许可、11 Star 的 Garmin Connect MCP/Skill 插件，支持 WorkBuddy 等 Agent 通过浏览器 MFA 查询活动、睡眠、步数和心率，并将只读工具与本地 FIT 文件写入、训练计划创建明确分开；会处理健康数据和 Garmin 账号会话，使用前请确认授权、隐私、区域登录流程，并对任何训练库写入保留人工确认.
- [NetSuite MCP](https://github.com/Bolton-Z/ns-mcp-china) - MIT 许可、纯 Node.js 内置模块的 NetSuite MCP 连接器，可供 WorkBuddy 通过 OAuth 2.0 查询 SuiteQL、报表和记录，并自动刷新令牌；它面向真实 ERP 数据和写操作，需管理员配置集成与专用角色，凭据虽以本地权限 600 保存仍应最小化权限、先在沙箱验证，并为每项生产写入保留人工审批和审计.
- [Origin Auto](https://github.com/simcrq/origin-auto) - MIT 许可、面向 Windows OriginLab 的科研绘图 MCP 与 WorkBuddy Skill，提供 28 个 COM 自动化工具、独立脚本回退、真实数据出图验证以及 PNG/PDF/OPJU 存在性检查；需要本机已授权 Origin、Python 依赖和可见桌面自动化，运行会读取/写入工作簿并启动 Origin 进程，使用前请确认数据版权、安装许可、文件路径和导出结果.
- [DSH Reminder](https://github.com/Aisland-SJL/dsh-reminder) - MIT 许可的 DeepSeek Harness 跨窗口提醒插件，在任务完成或等待人工批准时发送浏览器通知；它只提醒、不代替用户批准，需在浏览器中授予通知权限，适合作为 WorkBuddy/Codex 风格 Agent 的相邻协作工具.
- [Devnors Data MCP](https://github.com/DevnorsAI/devnors-data-mcp) - MIT 许可、256 Star 的 WorkBuddy 远程/本地 MCP 数据服务，覆盖法律法规与裁判文书、企业登记/年报、税号开票、失信核查、内容/指数/热搜和快递查询，并支持先发现能力与参数再调用；远程模式会把请求发送到服务端，本地模式仍需 API Key，使用前请核对数据授权、收费、个人/企业信息范围和密钥保存方式.
- [Wudao A-Share Stock Data MCP](https://github.com/jcdreamjc/wudao-mcp) - MIT 许可、11 Star 的远程 HTTP MCP 数据服务，直接支持 WorkBuddy，提供 63 个只读 A 股工具，覆盖行情、K 线、指数/ETF、涨停梯队、板块轮动、资金流、龙虎榜、研报、公告和盘后复盘；需要申请 API Key 并把数据请求发送到远程端点，项目明确不执行交易、不承诺收益或提供投资建议，使用前请核对数据授权、费用、隐私和金融合规边界.
- [Beav](https://github.com/Jamailar/Beav) - 本地优先的自媒体素材、调研、选题与创作工作台，通过用户级插件和本机 MCP 连接 WorkBuddy；采用限制商业使用的自定义 MIT 衍生许可，生产安装包可能领先公开源码，并会涉及本地工作区、模型密钥、浏览器/社媒内容和回环服务，安装前请核对版本、许可、平台条款与权限范围.
- [wechat-openclaw-channel](https://github.com/HenryXiaoYang/wechat-openclaw-channel) - 让微信消息通过 QClaw 或 WorkBuddy OAuth/Centrifuge 通道触发本地 OpenClaw Agent；会把 WorkBuddy access/refresh token 写入 `~/.openclaw/openclaw.json`，消息经腾讯端点传输，且虽在 README/package 中声明 MIT，仓库并无 LICENSE 文件，使用前请保护配置、核对源码及微信/腾讯账号条款.
- [DSH WorkBuddy Connect](https://github.com/corrinehu/dsh-workbuddy-connect) - 将 WorkBuddy 桌面端模型接入 DeepSeek Harness，支持 Web、Desktop 与 TUI；会读取本机 WorkBuddy 登录文件并将刷新凭据保存到 DSH 自有目录，依赖非官方接口，安装前请复核源码与账号条款.
- [DSH Connect WorkBuddy](https://github.com/dingminhua/dsh-connect-workbuddy) - MIT 许可、建立在前者公开设计上的 DSH 插件，增加可选模型目录、逐模型图片输入授权、本机多账号切换、分套餐积分、签到和诊断面板，并以随机密钥保护回环 shim；它会读取 WorkBuddy 当前及历史登录文件、把刷新凭据以 0600 权限写入 `$DSH_HOME`，向非公开腾讯端点发送提示词与工具结果，且账号切换、设置保存和用户点击签到均会改变状态，使用前请审查凭据来源、账号选择、网络数据与平台条款.
- [DSH Memory Palace](https://github.com/lovezi0/dsh-memory-palace) - MIT 许可的 DeepSeek Harness 记忆插件，可桥接已有 `.workbuddy/memory`，用可编辑 Markdown 保存跨会话记忆、日志和摘要，并提供带确认门禁的删除工具；会读写本地记忆，智能摘要可调用模型，使用前应确认目录、敏感内容和网络/费用边界.
- [DSH Hybrid Memory](https://github.com/Frog755/dsh-hybrid-memory) - MIT 许可的本地混合记忆插件，将冻结快照、SQLite FTS5 可检索事实和跨 Hermes/Claude/Codex/WorkBuddy 导入结合，并提供威胁扫描、审核队列、原子写和漂移检测；它会读写记忆目录、导入会话内容并建立索引，安装前请确认数据根目录、备份、敏感内容和默认 auto-accept 行为.
- [DSH Agent Selector](https://github.com/jiang12345-code/dsh-agent-selector) - MIT 许可的 DeepSeek Harness 插件，可把任务真实委派给 WorkBuddy 内置/自定义模型、Codex 或 Claude，并返回出处凭证；WorkBuddy 通道会读取本地模型与会话数据、写入 automations 数据库并依赖逆向调度器，使用前请审查凭据、任务内容、数据库备份和账号条款.
- [Tonghuasun Agent](https://github.com/zhuyifang/tonghuasun-agent) - 面向 Windows 同花顺桌面客户端的 AGPL-3.0 Agent 连接工具，支持在 WorkBuddy 等 Agent 中查询行情、账户、持仓和成交；本机接口使用令牌并可选开启交易，且核心 Windows 插件未签名且暂时闭源，使用前务必核对二进制、隐私、证券账户权限和交易确认流程.
- [DSH WorkBuddy Provider](https://github.com/Axiaohungry/dsh-llm-workbuddy) - 为 DeepSeek Harness 接入 WorkBuddy 中国区模型，支持 API Key 与网页登录令牌；MIT 许可。插件会保存凭据、打开登录页并请求 `copilot.tencent.com` 官方域名接口，但属于第三方适配器，使用前请核对账号条款与令牌存储.
- [OpenWorkBuddy](https://github.com/CatCatUncle/openworkbuddy) - 腾讯 WorkBuddy 的开源复刻版，提供本地 Agent 工作台、Skills、MCP、桌面与多 IM 通道；采用 PolyForm Noncommercial 1.0.0，商业使用需另行授权，并具备 Shell、浏览器和外部通道能力，使用前请审查权限与数据流.
- [SailFish](https://github.com/ysyx2008/SailFish) - 面向 macOS/Windows 的私人桌面秘书与 WorkBuddy 风格 Agent，支持记忆、Skills、MCP、浏览器、终端和多 IM 渠道；采用 AGPL v3 与商业许可双许可模式，使用前请确认许可、凭据和本地/远程操作权限.
- [OpenBuddy](https://github.com/opensymph/OpenBuddy) - 基于 Rust/Tauri 的 MIT 开源 WorkBuddy 风格跨平台桌面客户端，支持 BYOK、多模型、Skills、MCP、计划模式、子 Agent 和本地自动化；模型凭据保存在本机明文配置中，使用前请按其说明保护配置文件.
- [Agent Context Sync](https://github.com/westsource/agentctxsync) - 在自托管服务中跨设备、跨 Agent 同步与备份会话.

### Community clients and enhancements

- [WorkBuddy Auto Sign-in](https://github.com/88lin/workbuddy-auto-signin) - 零依赖的签到与成长任务自动化；会读取本机登录令牌并调用逆向得到的非官方接口，使用前应核对账号条款与源码.
- [WorkDaddy](https://github.com/babygoton/WorkDaddy) - WorkBuddy 桌面增强工具，提供备份、会话迁移和长任务辅助.
- [WorkBuddy Skin Studio](https://github.com/cdredfox/workbuddy-skin-studio) - 可逆的 WorkBuddy Desktop 主题管理工具.
- [WorkBuddy Dream Skin](https://github.com/zhouwei713/WorkBuddy-Dream-Skin) - MIT 许可的 Windows 图片驱动主题系统，提供预设、托盘控制、验证与恢复工具；它会通过本机 CDP 端口重启 WorkBuddy，并运行未签名 PowerShell 与渲染器注入，启用前应保存任务并审查脚本.
- [M5Stack Toys / Core2 Buddy](https://github.com/sindney/m5stack_toys) - MIT 许可的 M5Stack 硬件项目集合，其中 Core2 Buddy 通过 USB 串口扫描 WorkBuddy 任务，在触摸屏显示工作区/任务并用 TTS、LED 通知状态；需要 Arduino、Python、串口和 edge-tts，使用前请确认本地 WorkBuddy 数据读取范围、硬件烧录脚本与外部语音服务.
- [LinkCode](https://github.com/arcboxlabs/linkcode) - 支持多种 coding agent 的开源桌面客户端.
- [CodeDrobe Desktop](https://github.com/CodeDrobe/desktop) - 支持 WorkBuddy 的开源主题管理器，可浏览、应用并随时恢复桌面主题；使用登录、应用路径或下载功能前请复核权限与来源.
- [WorkBuddy Switch](https://github.com/changexbc/workbuddy-switch) - 跨平台切换 WorkBuddy/CodeBuddy 账号并查看用量；会保存 OAuth token、改写本地认证文件并调用非官方接口，使用前请复核源码与账号条款.
- [WorkBuddy Account Migrate](https://github.com/xiaoliuzhuan666/workbuddy-account-migrate) - 迁移账号切换后的对话、长期记忆与 MCP 连接器；MIT 许可，支持备份、回滚与迁移后验证，但会改写 SQLite 中的 `user_id` 并合并本地数据，执行前务必确认备份、源/目标账号和数据范围.
- [Crew](https://github.com/shuishenghualalala/Ace) - Apache-2.0 的开源 WorkBuddy 风格本地多智能体工作台，提供 Desktop、Web、CLI、Skills、MCP、知识库、任务自动化和多 Agent 协作；源码预览版默认可操作本地文件并支持浏览器、外部渠道和自有模型，使用前请检查安全开关、API 密钥、账号配置与数据边界.

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

- [文件内容识别与处理](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/File-Recognition) - 官方工作流：批量重命名、整理会议纪要和翻译外文视频.
- [Google Calendar 与 Drive](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Google-Integration) - 连接 Google 服务、描述目标并核验日程或文件结果.
- [零代码制作本地应用](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Local-App) - 用 WorkBuddy 设计、排错并持续升级本地应用.
- [文档生成与编辑](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Document-Generation) - 官方演练：生成 Word 文档，以及依据素材和模板制作演示文稿.
- [数据分析并可视化](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Data-Analysis) - 官方演练：将表格或搜集的数据转为图表和可视化报告.
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

- [自媒体运营](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Social-Media) - 小红书图文和视频内容生产的官方工作流.
- [AI content production pipeline](https://mp.weixin.qq.com/s/dSKr_a5lUYunDfS79oRzcA) - 从选题到发布的内容工作流.
- [Exam prep and job search](https://mp.weixin.qq.com/s/ldhLYboHnLiqrz12I5vW9Q) - 学习与求职任务编排.
- [Six time-consuming job-search tasks](https://mp.weixin.qq.com/s/mogl1CFtEEf9GCK2_BxbCg) - 求职自动化案例.

### Automation and Agent workflows

- [每日自动资讯简报](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Daily-Briefing) - 连接 QQ 邮箱、测试简报、设置每日发送并进行个性化调整.
- [AI 自驱动执行](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/AI-Self-Driven) - 说明任务目标，让 WorkBuddy 自行拆解步骤并在交付前完成自检.

## Research and Engineering

- [Tencent WorkBuddy Bench](https://arxiv.org/abs/2607.20911) - 多领域 coding-agent 基准与可复现实验协议.
- [WorkBuddy Bench 官网](https://workbuddybench.com/) - 官方基准概览、评测赛道、结果与运行入口.
- [WorkBuddy Bench 数据集](https://huggingface.co/datasets/tencent/workbuddy-bench) - Code、Web、Office 与 Security 四个子集的官方任务归档.
- [CloudBase model configuration](https://docs.cloudbase.net/ai/ai-tools/workbuddy) - OpenAI-compatible 模型接入示例.

## Related Lists

- [semlinker/awesome-workbuddy](https://github.com/semlinker/awesome-workbuddy) - CC0 的中文 WorkBuddy 资源清单，覆盖官方资料、实战案例、提示词、Skills 与 MCP；与本清单互补，使用其中链接前仍需单独核验来源和权限.
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
