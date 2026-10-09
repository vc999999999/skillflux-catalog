# 科研方法技能：完整目录补齐

来源固定为 [K-Dense-AI/scientific-agent-skills @ 92ace75](https://github.com/K-Dense-AI/scientific-agent-skills/tree/92ace75ac21efe19a620434e0ca4e356081fe807)，MIT。
本次实际复制完整技能目录及脚本，不再只保留来源链接。旧 `2026-10-08` 的候选文件没有覆盖或修改。

## 完整目录单元

[`intake/scientific-agent-skills-2026-10-09/collection/`](../intake/scientific-agent-skills-2026-10-09/collection/) 保留原始 `skills/<id>/` 布局和根 `LICENSE.md`：

| 技能 | 角色 | 上游目录的全部文件 |
| --- | --- | --- |
| `scientific-critical-thinking` | 主选：研究论证与证据评估 | 入口 + 8 个参考文件，共 9 个 |
| `scientific-brainstorming` | 主选：科研构思、排序与决策记录 | 入口 + 5 个参考文件 + 4 个 Python 脚本，共 10 个 |
| `scientific-schematics` | 支持：critical-thinking 明确引用的可选绘图分支 | 入口 + 2 个参考文件 + 3 个脚本，共 6 个 |

每个技能目录额外附上原许可证的 `LICENSE.txt`。整个单元共 **29 个文件、376,999 字节**。
使用时应保留整个 collection 的结构：这样 critical-thinking 中的 `skills/scientific-schematics/scripts/generate_schematic.py` 引用有实际文件。

逐文件 SHA-256、Git blob SHA、大小和原路径见 [机器可读清单](scientific-agent-skills-complete-2026-10-09.json)。
`inventoryScope: complete-skill-directory` 的记录与固定上游树逐项比对；collection 记录覆盖全部复制的原文件和额外许可证，明确只选择这三个目录。

## 文件齐全与执行条件

- Python、`requests`、OpenRouter API 和密钥属于运行环境，不作为第三方软件环境捆绑进源码包。上游绘图脚本会在参数和环境变量未提供密钥时查找当前目录及父目录的 `.env`；本次只审阅和复制，没有运行或读取用户的 `.env`。
- brainstorming 向 hypothesis-generation、experimental-design、statistical-power、literature-review、statistical-analysis 的交接属于其他任务技能，没有宣称它们已安装。
- 三个完整技能目录的内部相对 Markdown 链接均存在。额外的联网文献核对、付费绘图和数据外发仍需实际宿主能力及相应任务授权。

## 验证状态

全部 **26 个原文件** 与固定 Git 树的 blob SHA 和大小一致；新增的三个许可证副本与根 MIT 内容一致。
没有执行上游脚本、安装依赖、调用付费服务或做人工/宿主实测。

当前文件扫描器在 `scientific-brainstorming/references/responsible_ai.md` 的禁止事项列表中命中 `safety-bypass` 规则；清单保留失败结果和原文，未修改扫描器或文本来绕过检查。
因此这些内容以完整 `intake` 包收录，未提供 `skillflux.json`，不宣称获得 MCP 安装资格。
