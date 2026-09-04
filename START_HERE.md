# Start Here

不确定该用普通任务、Skill、MCP、Automation 还是企业 Agent？先按目标选择。

| 你的目标 | 从哪里开始 | 为什么 |
| --- | --- | --- |
| 临时完成一次研究、文档、表格或 PPT | [创建普通任务](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) | 无需先配置扩展，直接描述交付物和验收标准 |
| 重复执行一套专业方法 | [创建或导入 Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) | 把步骤、知识、脚本和模板封装为可复用能力 |
| 连接数据库、消息机器人或外部 API | [配置 MCP](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) | 让 Agent 获得外部工具和数据源 |
| 每小时、每天或每周自动运行 | [创建 Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) | 为成熟任务增加计划与结果通知 |
| 在企业微信远程下发任务 | [配置企微助理](https://cloud.tencent.com/document/product/1831/134441) | 从消息端控制正在运行的 WorkBuddy |
| 为团队发布长期运行的数字员工 | [WorkBuddy Enterprise 快速开始](https://cloud.tencent.com/document/product/1831/134527) | 提供 Agent、Runtime、Session、渠道、凭据和评测管理 |

## A reliable first task

第一次任务尽量使用不敏感的副本，并写清四件事：

1. **输入**：指定文件、目录、网页或背景材料。
2. **结果**：说明需要 Markdown、Word、Excel、PPT、代码还是其他格式。
3. **约束**：给出语言、受众、模板、截止时间和不可修改的内容。
4. **验收**：列出完成标准，例如来源可追溯、公式可复算、链接有效或版式检查通过。

示例：

> 阅读 `reports/` 中三份脱敏行业报告，输出一份中文 Markdown 对比表和一份 10 页以内的管理层 PPT。每个数字标注文件名与页码，不确定的信息写“待确认”，完成后检查链接、页数和引用是否一致。只修改 `output/`。

先观察 WorkBuddy 的计划和权限请求。涉及删除、发布、付款、账号设置或真实业务数据时，不要取消人工确认。

## When to turn a task into a Skill

当同类任务已经成功执行两到三次，输入输出稳定、步骤可以验收时，再沉淀为 Skill。一个清楚的 Skill 通常包含：

- `SKILL.md`：触发条件、步骤、质量门禁与失败处理；
- `scripts/`：需要确定性执行的转换、校验或自动化代码；
- `references/`：规范、Schema、业务知识和来源；
- `assets/`：模板、字体、图片或交付物样板。

不要把密钥、Cookie、客户数据或机器专属绝对路径放进 Skill。安装第三方资源前执行 [安全检查](SECURITY.md)。

## When to add MCP

Skill 主要描述“怎样完成工作”，MCP 主要提供“可以调用什么”。只有任务确实需要外部系统时才添加 MCP，并优先：

1. 使用项目级配置隔离实验；
2. 采用最小权限和只读范围；
3. 通过环境变量或凭据管理传递密钥；
4. 用无敏感数据的小请求验证输入输出；
5. 确认失败、重试和撤销方式后再加入 Automation。

## Next steps

- 浏览 [经过筛选的 Skills、工具与案例](README.md#open-source-ecosystem)。
- 查看 [生态项目活跃度](ECOSYSTEM.md)。
- 从 [尚未审核的新项目队列](DISCOVERIES.md) 帮忙验证候选。
- 推荐资源前阅读 [贡献指南](CONTRIBUTING.md) 和 [安全指南](SECURITY.md)。
