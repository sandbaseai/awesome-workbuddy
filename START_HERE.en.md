# Start Here

Not sure where to begin? Choose the task you want to complete:

| What you want to do | Start here |
| --- | --- |
| Finish research, documents, spreadsheets, or slides | [Create a regular task](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) |
| Reuse a reliable method | [Create or import a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) |
| Connect a database, messaging platform, or external API | [Configure MCP](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) |
| Run a task on a schedule | [Create an Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) |
| Trigger a task remotely from WeCom | [Configure the WeCom assistant](https://cloud.tencent.com/document/product/1831/134441) |
| Publish an Agent for your team | [WorkBuddy Enterprise quick start](https://cloud.tencent.com/document/product/1831/134527) |

## Describe your first task

Start with a non-sensitive copy and tell WorkBuddy four things: what to process, what to produce, what constraints matter, and how to verify completion.

For example:

> Read three redacted industry reports in `reports/`. Produce a Chinese Markdown comparison table and a management PPT of no more than 10 slides. Cite the source filename and page for every number, mark uncertain information as “needs confirmation,” check links, slide count, and citations, and write only to `output/`.

Keep human confirmation for deletion, publishing, payments, account settings, and real business data.

<details>
<summary>When should you use a Skill or MCP?</summary>

Create a Skill when a repeatable task has stable inputs and outputs. Configure MCP only when the task truly needs an external system. Before installing either one, read the [security guide](SECURITY.md), use least privilege, and test with non-sensitive data.

Never put keys, cookies, customer data, or machine-specific paths into a Skill.

</details>

## More

- [Full resource directory](https://sandbaseai.github.io/awesome-workbuddy/)
- [Bilingual README](README.md)
- [Security guide](SECURITY.md)
