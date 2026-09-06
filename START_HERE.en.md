# WorkBuddy Getting Started

You do not need to read the full catalog first. Complete one small task, then add a Skill, MCP, or automation only when you need it.

## Complete your first task in three steps

### 1. Prepare your materials

Open the [official quickstart](https://www.workbuddy.ai/docs/zh/workbuddy/Quickstart). Use a copy of your files without passwords, customer data, or keys. For your first run, use a small number of files and save the output in a separate folder.

### 2. Describe the task clearly

A useful task request usually includes:

- **Materials**: which files, folders, or information to read
- **Result**: what to produce, in which language and format
- **Constraints**: scope, length, style, deadline, or exclusions
- **Checks**: what to verify before finishing

Copy and adapt this template:

> Read `[files or folder]` and produce `[desired result]`. Use `[language/format/style]`, process only `[scope]`, and do not modify `[off-limits location]`. When finished, check `[citations, numbers, links, or formatting]` and list anything uncertain.

### 3. Check the result

Open the generated files and confirm the content, citations, and save location before adding more requirements. For a complex task, work in rounds: summarize first, create a draft second, then review and revise.

## When should you use a Skill, MCP, or Automation?

| You want to… | Use… | Example |
| --- | --- |
| Repeat fixed steps | **Skill** | Weekly reports, rewriting, file organization |
| Use an external service | **MCP** | Database, knowledge base, WeCom, API |
| Run at a time or condition | **Automation** | Scheduled summaries and reminders |

Recommended order: **regular task → Skill → MCP / Automation**. Make the task reliable first, then package repeated steps into a Skill.

- [Create or import a Skill](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills)
- [Configure MCP](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide)
- [Create an Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide)
- [WeCom assistant](https://cloud.tencent.com/document/product/1831/134441) · [Enterprise Agent](https://cloud.tencent.com/document/product/1831/134527)

## Before using a community resource

- Open the original README and confirm the supported version, system, installation method, and license.
- Check the license and what files, accounts, network services, or external systems it can access.
- Test with non-sensitive data first. Keep human confirmation for deletion, publishing, payments, account settings, and real business data.

Never put keys, cookies, customer data, or machine-specific paths into a Skill or commit them to a repository. See the [security guide](SECURITY.md) for more advice.

## Common problems

- **The Skill does not trigger**: confirm that it is installed in WorkBuddy's Skills directory, then state the goal in the task; if needed, explicitly say “use the `<skill>` Skill”.
- **MCP connection fails**: check that the service is running and that its address, port, key, and permissions are correct. Redact secrets before sharing an error.
- **The wrong files were changed**: restart with a clear scope such as “read only this directory and modify only that directory”, and ask WorkBuddy to list planned files first.
- **The result seems unreliable**: ask for sources, citations, and unverified items. Review manually before real-business, publishing, or deletion actions.

## Continue reading

- [Online resource directory](https://sandbaseai.github.io/awesome-workbuddy/): filter by keyword, category, and type
- [Chinese catalog](RESOURCES.md) · [English catalog](RESOURCES.en.md)
- [Changelog](CHANGELOG.md)

This is a community-maintained third-party index and is not affiliated with Tencent.
