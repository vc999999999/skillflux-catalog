# 实证研究技能：完整选中目录与共享资源

来源固定为 [Auto-Empirical-Research-Skills @ 9fa87d8](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/tree/9fa87d86e34d6c9a1c7cdb0db755c83c780537a0)。
本次实际复制该仓库 `skills/50-brycewang-aer-skills/` 中有明确 **MIT** 许可证的部分，不将外围异构许可证合集混入。
该镜像声明原作者来源为 `brycewang-stanford/AER-skills`；本次固定的是镜像提交，没有冒充原作者仓库的提交。

## 选中内容

完整目录单元位于 [`intake/auto-empirical-research-skills-2026-10-09/aer-skills/`](../intake/auto-empirical-research-skills-2026-10-09/aer-skills/)。

| 技能 | 角色与用途 | 上游目录的全部文件 |
| --- | --- | --- |
| `aer-preregistration` | 主选：预分析计划、结果指标与功效假设 | 入口、宿主声明、PAP 模板，共 3 个 |
| `aer-identification` | 主选：识别策略、估计方法与诊断 | 入口、宿主声明、估计器手册，共 3 个 |
| `aer-replication` | 主选：复现包、数据来源与运行说明 | 入口、宿主声明、复现清单，共 3 个 |
| `aer-robustness` | 支持：前两者直接引用的稳健性方法 | 完整 3 个文件 |
| `aer-statspai` | 支持：识别与稳健性技能引用的工具绑定 | 完整 2 个文件 |
| `aer-tables-figures` | 支持：StatsPAI 分支引用的表图规则 | 完整 3 个文件 |

还保留了原相对结构下的实际共享资源：

- 三种语言的完整 `templates/python/`、`templates/r/`、`templates/stata/`，包括依赖声明与入口脚本。
- 完整 `examples/replication-package-skeleton/`，包括 Stata 脚本、来源与表图登记模板、目录占位和原模板许可证。
- 功效、Lee bounds、Sun–Abraham、敏感性、DML、staggered DiD、LP-DiD、Oster 八个相关示例目录及公共 `_aer_numeric_check.py`。
- `references.bib`、方法参考、术语表、设计原则、来源登记、两份论文示例表、`scaffold_project.py` 与 StatsPAI 工具清单。
- 根 MIT 许可证和每个选中技能目录的完整许可证副本。

整个单元共 **105 个文件、411,564 字节**。不要仅复制三个 `SKILL.md`，也不要移动共享目录，否则原文相对路径和模板脚本的资源定位会失效。

## 可核对的完整性

[机器可读清单](auto-empirical-research-skills-complete-2026-10-09.json) 为每个完整技能记录 `sourcePath`、`target`、`upstreamFiles`（Git blob SHA 与大小）及 SHA-256。
collection 记录覆盖全部 **99 个原文件**及 6 个许可证副本，同时明确是选中子集，未声称复制整个 MIT 合集或整个 AERS 仓库。

全部原文件均与固定 Git 树逐字节核对。六个技能的原始目录文件库存完整；选中技能实际调用的本地模板、示例和辅助脚本已保留。
术语表中指向其他写作、审稿、投稿或合集维护文档的 14 处“另见”导航保留原文，清单的 `optionalRelatedContent` 给出固定上游地址，未把这些扩展导航当作本次已收录技能。

## 执行与审核状态

Python、R、Stata、统计软件包和可选 StatsPAI MCP 是外部运行条件。本次没有执行上游脚本、安装这些环境或接入服务。
`scaffold_project.py --replace` 有删除并重建目标目录的分支，登记研究及 openICPSR 上传也属于实际外部操作；收录源码没有执行或授权这些行为。

六个独立技能目录通过现有文本扫描；整个共享单元有 105 个文件，超过当前 MCP 的 64 文件安装限制。
它作为完整 `intake` 目录保存，尚无 SkillFlux 安装 manifest、人工方法验证或宿主安装证据。生成文档不等于研究已登记、复现已通过或期刊已接受。
