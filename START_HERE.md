# WorkBuddy 上手教程

第一次使用时，不需要先读完整目录。按下面的路径走，通常几分钟就能完成第一个任务。

## 1. 先选你的目标

| 你的目标 | 推荐入口 |
| --- | --- |
| 第一次使用 WorkBuddy | [官方快速开始](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) |
| 研究、写作、做表格或 PPT | [创建普通任务](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) |
| 把一套方法重复使用 | [创建或导入 Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) |
| 连接数据库、知识库、企微或 API | [配置 MCP](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) |
| 定时运行任务 | [创建 Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) |
| 远程下发任务或服务团队 | [企微助理](https://cloud.tencent.com/document/product/1831/134441) · [企业 Agent](https://cloud.tencent.com/document/product/1831/134527) |

## 2. 完成第一个任务

第一次请使用不敏感的文件副本，并在任务里说清楚四件事：

1. 要处理什么
2. 希望得到什么结果
3. 有哪些格式或范围限制
4. 怎样检查任务是否完成

可以直接复制这句话试试：

> 阅读 `reports/` 中三份脱敏行业报告，输出一份中文 Markdown 对比表和一份 10 页以内的管理层 PPT。每个数字标注文件名与页码，不确定的信息写“待确认”，完成后检查链接、页数和引用是否一致。只修改 `output/`。

任务完成后，先打开结果检查内容、引用和文件位置，再继续追加要求。把大任务拆成几轮，通常比一次说完更容易得到稳定结果。

## 3. 什么时候用 Skill、MCP 和 Automation？

按这个简单判断即可：

| 如果你需要…… | 使用…… |
| --- | --- |
| 让 WorkBuddy 按固定步骤反复完成同类任务 | **Skill** |
| 读取或操作外部系统、服务或 API | **MCP** |
| 在指定时间或条件下自动执行 | **Automation** |

建议先把普通任务跑通，再把稳定、重复的步骤整理成 Skill；只有确实需要外部系统时才配置 MCP。

## 4. 安装社区资源前先检查

- 打开原项目 README，确认适用版本、系统环境和安装方式。
- 查看许可证，以及它会访问的文件、账号、网络和外部服务。
- 先用无敏感数据测试；涉及删除、发布、付款、账号设置或真实业务数据时保留人工确认。

不要把密钥、Cookie、客户数据或机器专属路径写进 Skill，也不要提交到仓库。更完整的建议见 [安全指南](SECURITY.md)。

## 继续阅读

- [在线资源目录](https://sandbaseai.github.io/awesome-workbuddy/)：按关键词、分类和类型筛选
- [完整中文目录](RESOURCES.md) · [English catalog](RESOURCES.en.md)
- [项目更新记录](CHANGELOG.md)

这是社区维护的第三方索引，不代表腾讯官方。
