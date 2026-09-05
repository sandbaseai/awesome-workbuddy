# Start Here

不知道从哪里开始？先按你要完成的事情选择入口：

| 你想做什么 | 从这里开始 |
| --- | --- |
| 临时完成研究、文档、表格或 PPT | [创建普通任务](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) |
| 重复使用一套方法 | [创建或导入 Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) |
| 连接数据库、消息平台或外部 API | [配置 MCP](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) |
| 定时运行任务 | [创建 Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) |
| 从企业微信远程下发任务 | [配置企微助理](https://cloud.tencent.com/document/product/1831/134441) |
| 为团队发布企业 Agent | [WorkBuddy Enterprise 快速开始](https://cloud.tencent.com/document/product/1831/134527) |

## 第一个任务这样说

第一次建议使用不敏感的副本，并告诉 WorkBuddy：

1. **要处理什么**：文件、目录、网页或背景材料。
2. **要交付什么**：Markdown、Word、Excel、PPT、代码或其他格式。
3. **有什么要求**：语言、受众、模板、截止时间和不能修改的内容。
4. **怎样算完成**：例如来源可追溯、公式可复算、链接有效或版式通过检查。

示例：

> 阅读 `reports/` 中三份脱敏行业报告，输出一份中文 Markdown 对比表和一份 10 页以内的管理层 PPT。每个数字标注文件名与页码，不确定的信息写“待确认”，完成后检查链接、页数和引用是否一致。只修改 `output/`。

涉及删除、发布、付款、账号设置或真实业务数据时，保留人工确认。

<details>
<summary>进阶：什么时候使用 Skill 或 MCP</summary>

### 使用 Skill

同类任务已经成功执行几次、输入输出稳定，并且步骤可以检查时，再沉淀为 Skill。安装第三方 Skill 前先看 [安全指南](SECURITY.md)。

### 使用 MCP

只有任务确实需要外部系统时才配置 MCP。优先使用最小权限、项目级配置和环境变量保存凭据，并先用无敏感数据测试；确认失败、重试和撤销方式后，再加入自动化。

不要把密钥、Cookie、客户数据或机器专属路径写进 Skill。

</details>

## 更多入口

- [完整资源目录](https://sandbaseai.github.io/awesome-workbuddy/)
- [双语 README](README.md)
- [安全指南](SECURITY.md)
