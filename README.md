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
            ├── scripts/、references/、assets/ # 上游存在时，保留完整脚本、参考、模板和资源
            ├── agents/openai.yaml      # （可选）宿主界面声明
            └── LICENSE.txt             # （第三方导入时）上游许可证全文
index.json                   # 由 `skillflux catalog .` 生成，客户端唯一入口
imports/                     # 固定上游提交的导入清单、文件哈希和验收任务
intake/                      # 已完整收集、尚待适配或验收的候选包，不进入客户端索引
scripts/verify_imports.py     # 检查完整库存、文件哈希及固定上游原始字节
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

2026-10-09 按明确选择，已收集 Matt Pocock 固定提交中的全部 **38 个 Skill**：复用 9 个已有完整包，
新补齐 29 个候选包。103 个上游原文件中包含 42 个非 Markdown 文件；加完整许可证共 142 个文件。
完整库存、beta 状态与依赖映射见 [Matt Pocock 全部 Skill 收录记录](imports/mattpocock-all-2026-10-09.md)。
新增内容没有自动取得安装资格，现有 qualified 版本保持不变。

## 其他来源与候选

以下选中的技能已经保存完整包，尚未授予 MCP 安装资格。来源页的登记与实际文件收集分别记录。

| 来源 | 本次保留的内容 | 收录记录 |
| --- | --- | --- |
| morluto/rea | reverse-engineer-anything 完整指令候选包；依赖独立 REA MCP/CLI 及分析工具 | [来源、能力与校验](imports/morluto-rea-2026-10-08.md) |
| QingYunA/answer-me-with-html | 完整技能、捆绑 CLI、上游和第三方许可；涉及命令、后台更新与可选语音服务 | [来源、能力与校验](imports/qingyuna-answer-me-with-html-2026-10-08.md) |
| K-Dense-AI/scientific-agent-skills | 2 个主选：scientific-critical-thinking、scientific-brainstorming；附 scientific-schematics 支持技能及脚本，共 29 文件 | [完整收录清单](imports/scientific-agent-skills-complete-2026-10-09.md) |
| brycewang-stanford/Auto-Empirical-Research-Skills | 3 个主选：aer-preregistration、aer-identification、aer-replication；附 3 个支持技能和共享模板、示例、脚本，共 105 文件 | [完整收录清单](imports/auto-empirical-research-skills-complete-2026-10-09.md) |

每个来源的 `imports/*.json` 都保存固定 GitHub 提交、待监测上游路径、收录范围和能力限制。
`intake/` 内容不进入 `index.json`，静态检查不等于已运行验证，也不替代人工验收。

## 筛选与完整收集

1. **先选技能**：记录选择理由和固定上游提交。除 Matt Pocock 此次明确全选外，不默认复制整个合集。
2. **完整保存选中的包**：复制整个 Skill 目录，保留脚本、模板、引用资源、配置及许可证。引用共享资源时保持相对结构；所需支持技能单独标记。外部软件、API 和扩展导航说明其依赖或来源。
3. **评测后开放安装**：检查实际能力、宿主兼容和人工评测，再建立安装版本。完整收录不等于完成适配或取得 qualified 资格。

新收录必须在 `imports/*.json` 中保存 `files`（完整目标目录 SHA-256 库存）与 `upstreamFiles`
（固定源目录的全部 Git blob SHA、大小与权限），共享集合另记完整库存和选中范围。
先与固定上游 Git 树核对库存，再运行：

```bash
python3 -B scripts/verify_imports.py .
python3 -B -m unittest discover -s scripts -p 'test_*.py'
```

校验支持二进制资源，发现缺失文件、多余文件、字节或执行权限变化即失败；不会执行收集的脚本。
校验依据已审查的库存，不能替代初次对照上游 Git 树的完整性审查。历史 source-only 记录不算已收集的包。

## 维护流程

新增技能版本后运行 `skillflux catalog .`（来自 [SkillFlux 主仓库](https://github.com/vc999999999/Skillflux_Cloudflare)），
提交生成的 `index.json`。CI 同时运行完整导入库存校验与 `skillflux catalog --check .`：
收集文件与清单不一致，或 `index.json` 与目录内容不一致，都会失败。

`skillflux.review.json` 中 `kind: "simulation"` 的评测不能使版本获得 qualified 资格；只有
`kind: "human"` 且 contentHash 绑定当前内容的评测才能发布可安装版本。撤销 = 将 review status
改为 `revoked` 并重建 index，依赖它的合格版本派生状态随之失效。

## 信任模型

免签名：信任根为 GitHub 账号（2FA + 分支保护）+ commit SHA 钉扎 + 逐文件 sha256 + CI 一致性检查。
