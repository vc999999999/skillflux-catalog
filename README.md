# SkillFlux Catalog

SkillFlux 的精选技能目录仓库。客户端（`skillflux` CLI / MCP）从此仓库拉取 `index.json`，
并把所有下载固定在解析到的 commit SHA 上，逐文件校验 sha256。

## 目录结构

```
skills/
└── <category>/              # 能力分类（与 manifest 的 category 字段一致，kebab-case）
    └── <id>/                # 技能 ID（全局唯一，kebab-case）
        └── <version>/       # 语义化版本；目录内容不可变
            ├── skillflux.json          # 声明性清单：名称、入口、依赖、权限、宿主、发布说明
            ├── skillflux.review.json   # 审核记录 + 绑定内容哈希的人工评测
            ├── SKILL.md                # 技能入口正文
            ├── agents/openai.yaml      # （可选）宿主界面声明
            └── LICENSE.txt             # （第三方导入时）上游许可证全文
index.json                   # 由 `skillflux catalog .` 生成，客户端唯一入口
imports/                     # 固定上游提交的导入清单、文件哈希和验收任务
intake/                      # 尚不符合当前权限模型的候选包，不进入客户端索引
```

规划规则：
- **分类目录是强制的**，且必须与 `skillflux.json` 的 `category` 一致（builder 校验，不一致即报错）。
- **技能 ID 全局唯一**，跨分类不重复；同一 ID 永远在同一分类目录下。
- **版本目录内容不可变**；任何内容变更（哪怕一个字符）必须新增版本目录。
- **第三方导入的技能必须捆绑上游 LICENSE.txt**，publisher 字段注明来源。

## 当前内容

| 分类 | 技能 | 状态 |
| --- | --- | --- |
| productivity | grill-me、grilling（来自 [mattpocock/skills](https://github.com/mattpocock/skills)，MIT，逐字导入） | ✅ qualified，四宿主实测 |
| development / product / data / research | 7 个开发种子 | needs-testing（simulation 证据，不可安装） |
| development / productivity | codebase-design、domain-modeling、writing-for-agents、handoff、to-questionnaire | needs-testing（Matt Pocock 原文导入，待人工与宿主验收，不可安装） |

2026-10-08 的筛选理由、固定来源和待验收任务见 [Matt Pocock 收录记录](imports/mattpocock-2026-10-08.md)。
`tdd`、`diagnosing-bugs`、`prototype` 的完整候选包保存在 `intake/`，它们涉及命令或 Git 操作，
需要先解决与当前权限模型的兼容问题；不会通过填写 `shell: false` 来掩盖实际能力需求。

## 其他来源与候选

以下来源已收录，供发现、溯源与更新检查；尚未授予 MCP 安装资格。

| 来源 | 本次保留的内容 | 收录记录 |
| --- | --- | --- |
| morluto/rea | reverse-engineer-anything 完整指令候选包；依赖独立 REA MCP/CLI 及分析工具 | [来源、能力与校验](imports/morluto-rea-2026-10-08.md) |
| QingYunA/answer-me-with-html | 完整技能、捆绑 CLI、上游和第三方许可；涉及命令、后台更新与可选语音服务 | [来源、能力与校验](imports/qingyuna-answer-me-with-html-2026-10-08.md) |
| K-Dense-AI/scientific-agent-skills | 科研库来源、候选清单及 scientific-critical-thinking 完整候选包 | [来源、能力与校验](imports/scientific-agent-skills-2026-10-08.md) |
| brycewang-stanford/Auto-Empirical-Research-Skills | 多来源合集登记、许可差异与三个优先候选指针；未批量复制异构许可内容 | [来源与许可审查](imports/auto-empirical-research-skills-2026-10-08.md) |

每个来源的 `imports/*.json` 都保存固定 GitHub 提交、待监测上游路径、收录范围和能力限制。
`intake/` 内容不进入 `index.json`，静态检查不等于已运行验证，也不替代人工验收。

## 维护流程

新增技能版本后运行 `skillflux catalog .`（来自 [SkillFlux 主仓库](https://github.com/vc999999999/Skillflux_Cloudflare)），
提交生成的 `index.json`。CI 会运行 `skillflux catalog --check .`：`index.json` 与目录内容不一致即失败。

`skillflux.review.json` 中 `kind: "simulation"` 的评测不能使版本获得 qualified 资格；只有
`kind: "human"` 且 contentHash 绑定当前内容的评测才能发布可安装版本。撤销 = 将 review status
改为 `revoked` 并重建 index，依赖它的合格版本派生状态随之失效。

## 信任模型

免签名：信任根为 GitHub 账号（2FA + 分支保护）+ commit SHA 钉扎 + 逐文件 sha256 + CI 一致性检查。
