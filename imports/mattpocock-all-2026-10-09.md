# Matt Pocock 全部 Skill 的完整包收集

上游固定提交：[`b0618bc436ad893b3c5e84e55fba86586d34a404`](https://github.com/mattpocock/skills/tree/b0618bc436ad893b3c5e84e55fba86586d34a404)。

按用户明确选择，收集该提交下全部 **38 个 Skill**，包含 engineering、productivity、misc 和 in-progress。这里的“全部”仅针对 Matt Pocock 仓库；其他来源仍按选中的 Skill 收集。

复用 9 个逐字一致的已有包，新补齐 29 个 intake 包。覆盖 103 个上游原始文件，其中 42 个不是 Markdown，包括 `agents/openai.yaml`、脚本和配置模板。每包附 Matt Pocock 完整 MIT 许可证；`pr` 另外附 HumanLayer 完整 MIT 许可证。

总计 142 个内容与许可文件（不计现有包的 SkillFlux manifest/review），逐文件字节比对 0 缺失、0 不一致；依赖映射 0 缺失。原始文件 Git blob SHA、字节数、权限和收录文件 SHA-256 见[机器可读清单](mattpocock-all-2026-10-09.json)。

## 范围和完整性的含义

- 整个 Skill 目录原样保存，包含其全部文件和子目录；未只提取 SKILL.md，未修改原始触发方式或引用。
- 宿主脚本、命令、第三方 CLI、issue tracker 与秘密配置是运行依赖；收集目录不等于安装这些依赖或授予执行权限。本次未运行上游脚本。
- 未发现 Skill 目录之外需要另外搬运的现存本地共享资源。技能间引用在清单中映射到相应完整包；目标项目的 GLOSSARY.md、ADR 和 tracker 配置是运行输入/产物。
- 收集后的技能仍须挑选、权限与宿主适配、人工验收。此次不新增 MCP 安装资格，现有 qualified 版本保持原样。
- `grilling` 当前上游与原有 1.0.0 不同，新增独立快照；`code-review` 使用来源隔离的路径，不覆盖同名 SkillFlux 种子。
- 7 个 in-progress 技能标为 beta；上游声明它们可能变更或移除，不随常规插件发布。4 个 misc 技能按上游 frozen 定位保留。

## 完整库存

| Skill | 上游分类 | 原始文件 / 非 MD | 保存位置 |
| --- | --- | --- | --- |
| `ask-matt` | engineering | 3 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/ask-matt/) |
| `code-review` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/code-review/) |
| `codebase-design` | engineering | 4 / 1 | [复用](../skills/development/codebase-design/1.0.0/) |
| `diagnosing-bugs` | engineering | 3 / 2 | [复用](../intake/mattpocock-2026-10-08/diagnosing-bugs/) |
| `domain-modeling` | engineering | 4 / 1 | [复用](../skills/development/domain-modeling/1.0.0/) |
| `grill-with-docs` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/grill-with-docs/) |
| `implement` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/implement/) |
| `implement-spec` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/implement-spec/) |
| `improve-codebase-architecture` | engineering | 3 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/improve-codebase-architecture/) |
| `pr` | engineering | 3 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/pr/) |
| `prototype` | engineering | 4 / 1 | [复用](../intake/mattpocock-2026-10-08/prototype/) |
| `research` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/research/) |
| `retro` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/retro/) |
| `setup-matt-pocock-skills` | engineering | 7 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/setup-matt-pocock-skills/) |
| `tdd` | engineering | 4 / 1 | [复用](../intake/mattpocock-2026-10-08/tdd/) |
| `to-spec` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/to-spec/) |
| `to-tickets` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/to-tickets/) |
| `triage` | engineering | 4 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/triage/) |
| `wayfinder` | engineering | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/wayfinder/) |
| `wizard` | engineering | 3 / 2 | [完整候选包](../intake/mattpocock-all-2026-10-09/engineering/wizard/) |
| `chief-of-staff` | in-progress | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/in-progress/chief-of-staff/) |
| `claude-handoff` | in-progress | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/in-progress/claude-handoff/) |
| `loop-me` | in-progress | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/in-progress/loop-me/) |
| `setup-ts-deep-modules` | in-progress | 3 / 2 | [完整候选包](../intake/mattpocock-all-2026-10-09/in-progress/setup-ts-deep-modules/) |
| `writing-beats` | in-progress | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/in-progress/writing-beats/) |
| `writing-fragments` | in-progress | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/in-progress/writing-fragments/) |
| `writing-shape` | in-progress | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/in-progress/writing-shape/) |
| `git-guardrails-claude-code` | misc | 3 / 2 | [完整候选包](../intake/mattpocock-all-2026-10-09/misc/git-guardrails-claude-code/) |
| `migrate-to-shoehorn` | misc | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/misc/migrate-to-shoehorn/) |
| `scaffold-exercises` | misc | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/misc/scaffold-exercises/) |
| `setup-pre-commit` | misc | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/misc/setup-pre-commit/) |
| `grill-me` | productivity | 2 / 1 | [复用](../skills/productivity/grill-me/1.0.0/) |
| `grilling` | productivity | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/productivity/grilling/) |
| `handoff` | productivity | 2 / 1 | [复用](../skills/productivity/handoff/1.0.0/) |
| `teach` | productivity | 6 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/productivity/teach/) |
| `to-questionnaire` | productivity | 2 / 1 | [复用](../skills/productivity/to-questionnaire/1.0.0/) |
| `wait-what` | productivity | 2 / 1 | [完整候选包](../intake/mattpocock-all-2026-10-09/productivity/wait-what/) |
| `writing-for-agents` | productivity | 3 / 1 | [复用](../skills/productivity/writing-for-agents/1.0.0/) |

## 许可证与归属

所有包保留上游原文和完整 Matt Pocock MIT 许可。`pr/CREDITS.md` 原样保留；其 SKILL.md 元数据明确指向 HumanLayer 的 show-me。已在固定 HumanLayer 提交读取对应原文及仓库 MIT 许可，补入 `LICENSE-HumanLayer.txt`，具体来源、提交和哈希见 JSON 中 `thirdPartyAttribution`。没有将此项归属说明冒充运行或人工验收。

## 后续验收

选择可公开安装的技能时，先审查记录中的能力需求与依赖闭包，完成真实目的/边界/宿主测试，再新增相应 catalog manifest/review。现有不可变版本不覆盖；本次完整包收集不改变既有审核结果。
