# WorkBuddy Getting Started

You do not need to read the full catalog first. Choose a goal below, complete one small task, and then move on to Skills, MCP, or automation when you need them.

## 1. Choose your goal

| Your goal | Recommended entry |
| --- | --- |
| Try WorkBuddy for the first time | [Official quickstart](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) |
| Research, write, make spreadsheets, or create slides | [Create a regular task](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart) |
| Reuse a reliable method | [Create or import a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills) |
| Connect a database, knowledge base, WeCom, or API | [Configure MCP](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide) |
| Run tasks on a schedule | [Create an Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide) |
| Trigger tasks remotely or serve a team | [WeCom assistant](https://cloud.tencent.com/document/product/1831/134441) · [Enterprise Agent](https://cloud.tencent.com/document/product/1831/134527) |

## 2. Complete your first task

Start with a non-sensitive copy of your files. Tell WorkBuddy four things:

1. What to process
2. What result you want
3. Which format or scope constraints matter
4. How to verify completion

Copy and adapt this example:

> Read three redacted industry reports in `reports/`. Produce a Chinese Markdown comparison table and a management PPT of no more than 10 slides. Cite the source filename and page for every number, mark uncertain information as “needs confirmation,” check links, slide count, and citations, and write only to `output/`.

After the task finishes, check the content, citations, and output location before adding more requirements. Breaking a large task into a few rounds is often easier to control than asking for everything at once.

## 3. When should you use a Skill, MCP, or Automation?

Use this quick rule:

| If you need to… | Use… |
| --- | --- |
| Repeat the same reliable steps | **Skill** |
| Read or operate an external service, system, or API | **MCP** |
| Run a task at a time or condition | **Automation** |

Get the regular task working first, then turn stable repeated steps into a Skill. Configure MCP only when an external system is genuinely required.

## 4. Check community resources before installing

- Open the original README and confirm the supported version, system, and installation method.
- Check the license and what files, accounts, network services, or external systems it can access.
- Test with non-sensitive data first. Keep human confirmation for deletion, publishing, payments, account settings, and real business data.

Never put keys, cookies, customer data, or machine-specific paths into a Skill or commit them to a repository. See the [security guide](SECURITY.md) for more advice.

## Continue reading

- [Online resource directory](https://sandbaseai.github.io/awesome-workbuddy/): filter by keyword, category, and type
- [Chinese catalog](RESOURCES.md) · [English catalog](RESOURCES.en.md)
- [Changelog](CHANGELOG.md)

This is a community-maintained third-party index and is not affiliated with Tencent.
