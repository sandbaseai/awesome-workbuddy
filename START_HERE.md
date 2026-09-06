# WorkBuddy 上手教程

不用先读完整目录。下面这条路径适合第一次使用：先完成一个小任务，再按需要添加 Skill、MCP 或自动化。

## 三步完成第一个任务

### 第一步：准备材料

打开 [官方快速开始](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart)，准备一份不含密码、客户隐私和密钥的文件副本。第一次建议只处理少量文件，并把输出放到单独的文件夹。

### 第二步：把任务说清楚

一条好用的任务说明通常包含：

- **材料**：要读取哪些文件、文件夹或信息
- **结果**：要生成什么，以及使用什么语言和格式
- **限制**：范围、页数、风格、截止时间或不能做的事
- **检查**：完成后需要核对什么

可以直接复制下面的模板，把方括号替换成你的内容：

> 请读取 `[文件或文件夹]`，生成 `[想要的结果]`。使用 `[语言/格式/风格]`，只处理 `[范围]`，不要修改 `[不应修改的位置]`。完成后检查 `[引用、数字、链接或格式]`，并列出不确定的内容。

例如：

> 请阅读 `reports/` 中的三份脱敏报告，生成一份中文 Markdown 对比表。每个数字标注文件名和页码，只修改 `output/`，完成后检查引用和数字是否一致，并列出待确认事项。

### 第三步：检查结果

先打开生成的文件，确认内容、引用和保存位置，再继续追加要求。复杂任务可以拆成几轮：先让 WorkBuddy 总结材料，再生成初稿，最后检查和修改。

## 什么时候需要 Skill、MCP 或 Automation？

| 你想做的事 | 选择 | 例子 |
| --- | --- | --- |
| 反复执行一套固定步骤 | **Skill** | 周报、文案改写、资料整理 |
| 读取或操作外部服务 | **MCP** | 数据库、知识库、企微、API |
| 在指定时间或条件下执行 | **Automation** | 定时汇总、周期提醒、自动处理 |

建议顺序：**普通任务 → Skill → MCP / Automation**。先确认任务本身能稳定完成，再把重复步骤做成 Skill；确实需要外部系统时再配置 MCP。

- [创建或导入 Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills)
- [配置 MCP](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide)
- [创建 Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide)
- [企微助理](https://cloud.tencent.com/document/product/1831/134441) · [企业 Agent](https://cloud.tencent.com/document/product/1831/134527)

## 使用社区资源前

打开原项目 README，确认适用版本、系统、安装方式和许可证；先用非敏感数据试运行。涉及删除、发布、付款、账号设置或真实业务数据时，请保留人工确认。

不要把密钥、Cookie、客户数据或个人路径写进 Skill，也不要提交到仓库。更多安全建议见 [安全指南](SECURITY.md)。

## 常见问题

- **Skill 没有触发**：确认已安装到 WorkBuddy 的 Skills 目录，并在任务中明确写“使用 `[Skill 名称]`”。
- **MCP 连接失败**：检查服务是否运行、地址和端口是否正确，再检查密钥与权限；分享错误时先隐藏敏感信息。
- **改错文件或改动太多**：明确写“只读取 `[目录]`，只修改 `[目录]`”，并先让 WorkBuddy 列出准备修改的文件。
- **结果不可靠**：要求列出来源、引用和待确认事项；重要结果先人工复核。

## 继续阅读

- [在线资源目录](https://sandbaseai.github.io/awesome-workbuddy/)：按关键词、分类和类型筛选
- [完整中文目录](RESOURCES.md) · [English catalog](RESOURCES.en.md)
- [项目更新记录](CHANGELOG.md)

这是社区维护的第三方索引，不代表腾讯官方。
