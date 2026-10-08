# Auto-Empirical Research Skills 来源收录

上游：[brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/tree/9fa87d86e34d6c9a1c7cdb0db755c83c780537a0)，固定提交 `9fa87d86e34d6c9a1c7cdb0db755c83c780537a0`。
机器可读来源与更新基线见 [收录清单](auto-empirical-research-skills-2026-10-08.json)。

## 本次为来源收录

该仓库包含实证研究流程、原作者技能、其他项目的镜像合集及一个 Git 子模块，涵盖 Python、R、Stata、因果推断、论文写作与复现。
固定提交的 [`catalog/skills.json`](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/9fa87d86e34d6c9a1c7cdb0db755c83c780537a0/catalog/skills.json) 声明 **77 个合集、1,107 条技能记录**。
另按该提交未截断 Git 树计数得到 1,172 个 `SKILL.md`（其中 1,168 个位于 `skills/`），未递归展开 `skills/69-Paper-WorkFlow` 子模块。
这两个数字的口径不同，不将描述中的 “23,000+” 当作已复制或已审核的技能数。

## 许可与来源

根 [LICENSE](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/9fa87d86e34d6c9a1c7cdb0db755c83c780537a0/LICENSE) 声明 CC BY-SA 4.0；这不是所有镜像技能的统一许可证。
上游 [许可与来源审计](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/9fa87d86e34d6c9a1c7cdb0db755c83c780537a0/docs/LICENSE_AUDIT.md) 明列 MIT、Apache、GPL、AGPL、非商业、混合和未知许可，并将 25 个合集的许可列为 `UNKNOWN`。
这是上游自报的审计线索，不替代对原作者仓库、文件和固定提交的逐项核验。

本次保留来源链接和审核记录，没有批量复制内容、执行安装器或递归拉取子模块。与 K-Dense 等已收录来源重叠的合集将优先回到原作者仓库核对，避免生成重复技能和模糊更新来源。

## 优先候选

我们选择性阅读了 `skills/50-brycewang-aer-skills/` 下三个候选的完整入口，并确认该合集本地 [LICENSE](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/9fa87d86e34d6c9a1c7cdb0db755c83c780537a0/skills/50-brycewang-aer-skills/LICENSE) 为 MIT。该合集声明来自 [brycewang-stanford/AER-skills](https://github.com/brycewang-stanford/AER-skills)；本次没有将镜像提交冒充原作者仓库提交。

| 候选路径（位于上述合集 `skills/` 下） | 价值 | 导入前需要核对 |
| --- | --- | --- |
| `aer-preregistration` | 在收集数据前整理预分析计划、主要结果和统计功效假设 | PAP 模板、共享参考资料和方法技能；不能因生成草稿就擅自登记研究；研究类型与政策判断需要专业验证 |
| `aer-identification` | 为因果识别方法和诊断准备结构化讨论 | 关联方法资料、StatsPAI/统计工具及真实数据计算；不能把示例阈值或方法建议当通用保证 |
| `aer-replication` | 整理数据与代码来源、运行说明及表图对应关系 | 共享模板、复现环境、依赖和数据许可；生成 README 不等于独立复现通过，上传研究材料仍需任务授权 |

这些是候选指针，不是已导入的可安装包。完整依赖、方法判断、材料授权及目标宿主尚未验收，未生成 SkillFlux manifest 或 human 评测。

## 后续导入要求

逐项固定原作者或镜像版本，保留完整许可、共享引用与依赖，再用公开或合成数据做人工目的与边界验证。
涉及脚本、网络、密钥、登记、上传或远程平台的操作必须明确声明与宿主授权；不能用 `shell: false` 隐藏实际能力需求。
只有完成 catalog 的人工及宿主门禁后，才能开放相应技能的 MCP 安装。
