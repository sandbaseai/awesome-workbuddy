# Contributing

[English](#english) · [简体中文](#简体中文)

## English

Thank you for improving Awesome WorkBuddy. We prefer a small, verifiable,
genuinely useful collection over a large unreviewed list.

### Add a resource

1. Search both READMEs and confirm that the resource is not already listed.
2. Confirm that the link is publicly accessible and directly relevant to
   Tencent WorkBuddy.
3. Add it to the narrowest category in both `README.md` and `README.en.md`:

   ```markdown
   - [Resource title](https://example.com) - One sentence explaining its value.
   ```

4. In the Pull Request, state what you personally verified and the review date.

License evidence must distinguish a repository-level `LICENSE` file from a
claim in a README, badge, or package manifest. When no license file exists,
record it as **not declared**: public access permits linking and review, but does
not imply permission to copy, modify, package, or redistribute. For collections,
also trace the provenance and license of each bundled Skill, prompt, template,
dataset, binary, or other third-party asset.

For a Skill, MCP server, script, desktop extension, or other executable
resource, also apply [SECURITY.md](SECURITY.md). Review installation commands,
dependencies, permissions, credentials, network destinations, data flow, and
irreversible actions, then record the important findings in the Pull Request.

Do not submit pure marketing, copied aggregation without provenance, private
group links, inaccessible material, duplicate entries, or Skills/MCP servers
whose source and permissions cannot be understood. Disclose whether you are the
author, maintainer, sponsor, or have another commercial relationship.

### Review checklist

- Use the canonical HTTPS URL, an accurate title, and no tracking parameters.
- Keep the description specific and neutral; avoid unprovable terms such as
  “best,” “essential,” or “official.”
- Explain file, account, credential, company-data, and external-action risks.
- Require human review for legal, medical, financial, or other high-stakes use.
- Keep one Pull Request focused on one resource or one coherent theme.
- Update both language editions and run `python3 -m unittest discover -s tests`.

### Refresh generated files

When `data/ecosystem-repos.txt` changes, refresh the checked-in directory and
metadata before opening the Pull Request:

```bash
python3 scripts/build_site_data.py
GITHUB_TOKEN="$(gh auth token)" python3 scripts/update_ecosystem.py
python3 scripts/update_readme_stats.py
python3 -m unittest discover -s tests
```

Commit the resulting `ECOSYSTEM.md`, `README.md`, `README.en.md`, and
`site/resources.json` changes together with the source edit. The ecosystem
workflow refreshes dynamic metadata weekly or through manual dispatch; it does
not run on every push, which keeps curation pushes free of metadata races.

### Report a broken or unsafe link

Use the [structured Issue Form](https://github.com/sandbaseai/awesome-workbuddy/issues/new?template=broken-link.yml)
and include the URL, observed problem, and review date. Maintainers may remove
malicious, unavailable, moved, or out-of-scope resources directly.

### Record a discovery audit

Maintainers should use the [discovery audit template](https://github.com/sandbaseai/awesome-workbuddy/issues/new?template=discovery-audit.md)
for candidates that need a documented include, hold, or exclude decision. Keep
the exact structure below: `Candidate` is plain text, followed by real blank
lines and the two level-two headings. Record the snapshot date and distinguish
GitHub's recognized license from a README claim.

```markdown
Candidate

- Repository: https://github.com/owner/repository
- Latest verified snapshot: YYYY-MM-DD
- GitHub reports N stars and SPDX license.

## Audit result

- Evidence about contents and direct WorkBuddy relevance.
- Evidence about license, provenance, and redistribution.
- Evidence about permissions, credentials, network/data flow, and account terms.

## Decision

Hold, curate, or exclude with the evidence needed for the next decision. This issue is an audit record, not an endorsement.
```

## 简体中文

感谢你帮助完善 Awesome WorkBuddy。我们重视少而精、可验证、对读者真正
有用的资源，而不是未经审核的数量。

### 添加资源

1. 搜索两份 README，确认条目尚未收录。
2. 确认链接可公开访问，内容与腾讯 WorkBuddy 直接相关。
3. 将条目加入 `README.md` 和 `README.en.md` 中最精确的分类：

   ```markdown
   - [资源标题](https://example.com) - 一句话说明它解决什么问题。
   ```

4. 在 Pull Request 中说明你实际验证了什么，以及检查日期。

许可证证据必须区分仓库级 `LICENSE` 文件与 README、徽章或 package metadata
中的声明。没有许可证文件时应记录为**未声明**：公开可访问只支持链接和审核，
并不自动授予复制、修改、打包或再分发权限。对于聚合仓库，还要追溯其中每个
Skill、提示词、模板、数据集、二进制或其他第三方资源的来源和许可证。

涉及 Skill、MCP、脚本、桌面扩展或其他可执行资源时，还需要按
[SECURITY.md](SECURITY.md) 检查安装指令、依赖、权限、凭据、网络目标、
数据流向与不可逆操作，并在 Pull Request 中记录重要结论。

请勿提交纯营销软文、来源不明的聚合转载、私域群链接、无法访问的资料、
重复条目，或源码与权限无法判断的 Skill/MCP。若你是作者、维护者、赞助方
或存在其他商业关系，请主动披露。

### 审查清单

- 使用规范 HTTPS 地址和准确标题，不带跟踪参数。
- 描述具体、中立，不使用“最好”“必备”“官方”等无法验证的表述。
- 说明本地文件、账号、密钥、公司数据与外部操作的权限和风险。
- 法律、医疗、财务等高风险内容明确要求人工复核。
- 一个 Pull Request 只处理一个资源或一个连贯主题。
- 同步更新两种语言，并运行 `python3 -m unittest discover -s tests`。

### 刷新生成文件

修改 `data/ecosystem-repos.txt` 后，开 Pull Request 前请先刷新已提交的目录和元数据：

```bash
python3 scripts/build_site_data.py
GITHUB_TOKEN="$(gh auth token)" python3 scripts/update_ecosystem.py
python3 scripts/update_readme_stats.py
python3 -m unittest discover -s tests
```

请把生成的 `ECOSYSTEM.md`、`README.md`、`README.en.md` 和 `site/resources.json`
与源文件修改一起提交。生态 workflow 每周定时或手动触发刷新动态元数据，
不会在每次 push 后运行，从而避免统计提交与收录提交互相竞态。

### 报告失效或不安全链接

使用[结构化 Issue 表单](https://github.com/sandbaseai/awesome-workbuddy/issues/new?template=broken-link.yml)，
附上链接、观察到的问题和检查日期。维护者可以直接移除恶意、失效、已迁移
或与主题无关的资源。

### 记录发现审计

维护者应使用[发现审计模板](https://github.com/sandbaseai/awesome-workbuddy/issues/new?template=discovery-audit.md)，
记录候选项目的收录、暂缓或排除决定。请保持下面的固定结构：`Candidate` 使用普通文本，
其后是真实空行和两个二级标题；记录快照日期，并区分 GitHub 识别出的许可证与 README 声明。

```markdown
Candidate

- Repository: https://github.com/owner/repository
- Latest verified snapshot: YYYY-MM-DD
- GitHub reports N stars and SPDX license.

## Audit result

- 记录内容和与 WorkBuddy 直接相关的证据。
- 记录许可证、来源和再分发依据。
- 记录权限、凭据、网络/数据流以及账号条款证据。

## Decision

写明暂缓、收录或排除，以及下一步需要的证据。本 Issue 是审计记录，不是背书。
```
