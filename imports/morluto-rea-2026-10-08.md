# REA 收录记录

上游：[morluto/rea](https://github.com/morluto/rea/tree/c701376777212ec9acfd10c97f45b1eaf0c885c6)，固定提交 `c701376777212ec9acfd10c97f45b1eaf0c885c6`，MIT。

已收录 `reverse-engineer-anything` 的完整技能指令目录：`SKILL.md` 和五个本地 references，加上完整上游许可证，共 7 个文件、29,846 bytes。原始目录为 `skill-src/reverse-engineer-anything`，目标为 [intake 候选包](../intake/morluto-rea-2026-10-08/reverse-engineer-anything/)。[机器可读记录](morluto-rea-2026-10-08.json) 保存逐文件 SHA-256、能力要求、外部文档固定链接和待验收任务。

此技能适合分析二进制、JavaScript/Electron 分发产物、托管程序集、软件包及指定运行行为，强调区分静态观察、推断和未知。不应用于普通源码仓库架构阅读。

## 为什么保留在 intake

技能正文明确指出：安装技能指令不会注册 REA MCP、安装分析引擎或给当前会话添加工具。实际使用依赖 REA MCP 或 `rea-agents` CLI，部分任务另需 Hopper、Ghidra、IDA、JADX/Java、Binwalk/Unblob、Chrome 等。MCP 注册、产物提取、浏览器/进程观察及运行目标都存在独立能力与授权要求，不能填写 `shell: false`、空网络权限后假装满足 SkillFlux 当前的能力边界。

本次只保存上游技能包和来源资料，没有整包复制 REA 工程、安装引擎、执行 setup/doctor、注册 MCP 或运行目标。技能中指向上游文档的外链原文保留，固定提交对应链接记在导入清单中；外部提供者仍是独立依赖。

## 验证与后续

- 原始六个技能文件逐字保存，完整 MIT 许可证随附，五个本地引用资源齐全。
- SkillFlux 文件格式、大小、路径和内容模式扫描通过；这不是对 REA 工程或提供者的完整安全审计。
- 没有建立 `skillflux.json`，不会进入 MCP 可安装索引；没有人工或宿主运行验证。
- 下一步应在用户自有样例上验证实际 MCP 工具、证据及边界，并明确宿主授权如何配合，再创建适配版本或安装集成。

更新检查应监测上游目录 `skill-src/reverse-engineer-anything`。运行工具的版本与技能元数据版本独立；即使技能目录未变，升级 REA 服务仍需检查实际工具清单。
