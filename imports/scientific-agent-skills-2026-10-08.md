# Scientific Agent Skills 来源收录

上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/92ace75ac21efe19a620434e0ca4e356081fe807)，固定提交 `92ace75ac21efe19a620434e0ca4e356081fe807`。
机器可读来源及更新基线见 [收录清单](scientific-agent-skills-2026-10-08.json)。

## 收录范围

这是科研技能集合，涉及科研方法、数据分析、生物化学、数据库访问和科研写作。完整 Git 树没有截断；在 `skills/` 下逐项计得 **177 个 `SKILL.md`**，与该提交 README 的数量一致。根许可证为 [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/LICENSE.md)，单独的资源或工具仍需检查其许可与使用条件。

本次将整个仓库作为可发现来源收录，未将上游的 “validated” 宣称转换成 SkillFlux 的人工审核结论，也未安装 177 项技能。我们选择性阅读了 README、许可证和下列四个技能的入口；没有运行上游脚本或安装上游依赖。

| 优先候选 | 用途 | 需要继续核对的能力与边界 |
| --- | --- | --- |
| `skills/scientific-critical-thinking` | 评估论证、偏差、因果解释与证据质量 | 核心分析无需网络；可选绘图指向另一个技能，涉及 Python、OpenRouter 与 API 密钥；有联网核对引用的分支 |
| `skills/scientific-brainstorming` | 组织科研问题、独立构思、评估方案并记录决策 | 可选 Python 3.11+ 本地辅助脚本；与假设生成、研究设计、文献及统计技能存在交接，构思不能证明科学结论 |
| `skills/experimental-design` | 在收集数据前设计随机化、分组和实验布局 | Python 3.12+、NumPy、pandas、pydoe；安装包可能联网；样本量与后续分析交给其他技能 |
| `skills/peer-review` | 形成有依据的审稿草稿和问题清单 | Python 3.11+ 本地脚本；审稿材料的处理需要与期刊政策、保密授权及实际 AI 宿主相符 |

## 完整候选包

`scientific-critical-thinking` 的入口和全部 8 个附属 Markdown 文件逐字保留在
[`intake/scientific-agent-skills-2026-10-08/scientific-critical-thinking/`](../intake/scientific-agent-skills-2026-10-08/scientific-critical-thinking/)，附上上游完整 MIT `LICENSE.txt`。
目录内部资源齐全，但可选 `scientific-schematics` 分支不在包内；本次没有把这一分支假装成无需命令、网络或密钥的能力。

因此该包没有 `skillflux.json`，不进入 MCP 索引。自动文件扫描与逐文件 SHA-256 比对只能证明本次原文和文件检查结果，不能证明科学方法正确、宿主兼容或任务执行通过。机器可读清单记录具体结果。

## 下一步验收

1. 先决定保留完整的外部工具分支，还是另做明确标识的纯文本适配版本；适配不能覆盖原文与现有版本。
2. 针对有缺失数据、混杂、重复样本、探索性分析等公开或合成案例，人工验证输出能区分证据、推断与建议，且不捏造结果。
3. 验证条件分支不会在用户仅要求文字评估时调用付费 API、传输未发表资料或读取密钥。
4. 资源和能力闭合后，再做真实宿主安装、读取及内容哈希绑定评测。达到 catalog 的 human gate 前不开放安装。
