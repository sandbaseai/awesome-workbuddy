# Security Guide

WorkBuddy Skills, MCP servers and desktop extensions can read files, call external services, run programs and act through connected accounts. Treat them as software, not as harmless prompt text.

## Before installation

### 1. Read the complete instructions

- Inspect `SKILL.md`, setup scripts, hooks, configuration examples and referenced files.
- Look for instructions that download or execute changing remote content.
- Reject instructions that ask the Agent to hide actions, bypass approvals or ignore higher-priority safety rules.
- Confirm that the repository, release file and installation command refer to the same publisher.

### 2. Check code and dependencies

- Prefer open-source projects with a clear license, recent maintenance and reproducible setup.
- Review shell, Python, JavaScript, PowerShell and binary entry points before execution.
- Check lockfiles and package install scripts. Avoid unpinned dependencies for sensitive workflows.
- Scan release archives and binaries; do not assume a popular repository is automatically safe.

### 3. Minimize permissions

- Grant only the directories, tools, accounts and network destinations required for the task.
- Use a test workspace or disposable account before accessing real data.
- Keep destructive file operations, publishing, payments and account changes behind human confirmation.
- Prefer read-only OAuth scopes and short-lived credentials where available.

### 4. Trace data flow

- Identify what stays local and what is sent to a model, API, analytics service or remote MCP server.
- Remove personal information, customer data and company secrets unless the service is explicitly approved.
- Never paste API keys into prompts or committed configuration files. Use the operating system keychain or documented secret storage.
- Confirm retention, deletion and training policies for every external service in the workflow.

## Higher-risk categories

Apply additional scrutiny to unofficial API proxies, automatic sign-in tools, runtime patching, browser-cookie access, account switching, remote-control software and extensions that modify the WorkBuddy application. These tools may expose credentials, weaken application boundaries or conflict with product terms.

Legal, medical, financial, education assessment and platform-compliance Skills provide assistance only. Require qualified human review and verify current primary sources before acting on their output.

## Report a concern

For an unsafe or misleading indexed resource, use the [broken-link and safety report](https://github.com/sandbaseai/awesome-workbuddy/issues/new?template=broken-link.yml). Include the affected URL, observed behavior, version and check date. Do not publish credentials, exploit details that put users at immediate risk, or private personal data.

Security concerns about WorkBuddy itself should be reported through Tencent's official support or security channels rather than this community list.
