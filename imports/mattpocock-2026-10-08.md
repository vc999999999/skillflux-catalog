# Matt Pocock 技能收录记录

上游：[mattpocock/skills](https://github.com/mattpocock/skills/tree/b0618bc436ad893b3c5e84e55fba86586d34a404)，固定提交 `b0618bc436ad893b3c5e84e55fba86586d34a404`，MIT。
本次按任务实用性、与现有库的重复程度、引用完整性和宿主能力需求筛选。
机器可读来源、逐文件 SHA-256 与候选能力声明见 [导入清单](mattpocock-2026-10-08.json)。

## 本次加入待验收目录

| 技能 | 值得收录的原因 | 人工目的测试 | 重点边界测试 |
| --- | --- | --- | --- |
| codebase-design | 为接口设计、模块拆分、可测试性提供统一方法，也支撑后续 TDD | 为三个不同折扣调用方设计共享金额计算接口，保留各方策略 | 用户只要求设计时不实施重构；替换测试需有任务授权；多方案分支需要并行代理 |
| domain-modeling | 澄清 Customer/User 等混淆概念，维护词汇表和必要 ADR | 为订单记录下单操作员、向买方组织开票，更新现有词汇表 | 尊重既有词义；未决定的业务规则先澄清；避免把实现细节写进词汇表或滥建 ADR |
| writing-for-agents | 改善 AGENTS.md、技能说明的触发条件、引用与完成标准 | 将重复的旧指引改成仅 UI 任务读取设计指南，部署由用户请求触发 | 保留用户约束；仅修改授权文档；不借整理文档扩大部署权限 |
| handoff | 为长任务切换会话提供简短、可继续的交接 | 把包含已完成工作、证据路径和未完成验证的会话写成交接文档 | 必须显式调用；写入系统临时目录；去除敏感信息；引用已有成果而不整段复制 |
| to-questionnaire | 把无法单方决定的需求转成可交给客户填写的问卷 | 澄清接收人的角色及需要取得的决策后生成问卷 | 必须显式调用；先明确接收人与所需信息；只生成本地文件，不自动发送 |

这五项使用 SkillFlux 独立版本号 `1.0.0`，并非上游发布版本号。原始 `SKILL.md`、所有引用资源、
`agents/openai.yaml` 均逐字复制，并随每项附上上游完整 `LICENSE.txt`。声明的四种宿主是待验收目标，
不构成兼容性结论。当前 `status: needs-testing`、`evaluation.kind: simulation`，MCP 不提供安装。

## 保留在 intake 的三个候选

| 技能 | 用途 | 当前不能直接发布的原因 |
| --- | --- | --- |
| tdd | 红、绿、重构循环，面向行为设计测试 | 实際流程运行测试命令；设计模块时需 codebase-design；文末 code-review 是可选建议，不绑定同名的 SkillFlux 种子 |
| diagnosing-bugs | 先复现再缩小故障范围，形成可验证诊断 | 可能运行 shell、curl、浏览器或 git bisect；HITL 脚本模板需要单独审阅执行边界 |
| prototype | 用可抛弃的逻辑或 UI 原型验证假设 | 两个分支均要求 Git 分支和实施问题中的指针记录（可为本地记录）；UI 分支另需任务运行器，不能声明为无需这些能力 |

当前客户端 `scanPermissions` 拒绝 shell、network、secrets 权限。静态扫描通过只能说明文件格式和规则检查通过，
不能证明运行这些流程不需要相关能力。上述完整原文和许可证保存在 `intake/mattpocock-2026-10-08/`，
没有 `skillflux.json`，不进入 `index.json`。后续需要明确权限含义、实现与宿主授权的配合，再决定是否导入或做单独标明的适配版本。

## 没有重复或整包搬运的部分

- 现有 `grill-me`、`grilling` 已入库，保留原有审核版本。上游 `grilling` 本次提交有文字变化，不能覆盖旧的 `1.0.0`。
- 上游 `code-review` 与库中种子 ID 重名，且依赖问题跟踪及并行代理，后续单独处理映射。
- `to-spec`、`to-tickets`、`triage`、`wayfinder`、`implement`、`implement-spec`、`ask-matt` 属于相互关联的工程流程，应整体检查依赖与外部操作。
- `grill-with-docs`、`retro` 分别依赖 grilling/domain-modeling 和 writing-for-agents，适合基础技能验收后再加。
- `pr` 的 CREDITS.md 列出第三方段落来源，需核对该部分的许可和归属后再导入。
- `in-progress`、宿主专属钩子、环境与凭据配置类暂不纳入首批。

## 已完成的检查

- 八个包均与固定上游目录逐文件比对一致，许可证完整，本地 Markdown 资源引用齐全，自动扫描通过。
- 原有九条目录记录的内容与审核结果保持不变；五个新增条目均为 needs-testing，三个 intake 未入索引。
- 五项技能各完成一个隔离 Codex AI 预演，产物满足相应样例的目的与范围约束。完整输入、输出、哈希和未覆盖分支见 [设计与文档预演](evidence/mattpocock-2026-10-08/design-docs.json) 和 [交接与问卷预演](evidence/mattpocock-2026-10-08/handoff-questionnaire.json)。这些是 simulation，不是人工或四宿主验收。

## 发布验收

1. 人工在隔离项目中完成上表目的测试及边界测试，保留实际输入、输出、失败项与证据位置。
2. 对 manifest 中每个宿主验证真实 MCP 安装、正文读取和资源读取，包括 handoff/to-questionnaire 的显式触发限制。
3. 只在真实完成后写 `kind: human`，用当前内容的 `contentHash` 绑定证据。AI 预演不能替代这一步。
4. 有内容或 manifest 改动时创建新版本；只有审核 sidecar 可补充新的评测证据。
5. 全部通过后再设 `status: approved`，重建并检查索引：`skillflux catalog .`、`skillflux catalog --check .`。

本次是目录内容更新，不涉及 npm 客户端代码或 npm 发布。
