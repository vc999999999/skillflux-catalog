# Answer me with HTML 收录记录

上游：[QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html/tree/d0add7ec67fd51704321ec0295ede1563f8297be)，固定提交 `d0add7ec67fd51704321ec0295ede1563f8297be`，仓库包版本 `0.4.15`，MIT。

已收录 `skills/answer-me-with-html` 的完整四文件技能目录（入口、设置与视频引用、捆绑 CLI），补齐上游及第三方许可后共 9 个文件、510,949 bytes。目标为 [intake 候选包](../intake/qingyuna-answer-me-with-html-2026-10-08/answer-me-with-html/)。[机器可读记录](qingyuna-answer-me-with-html-2026-10-08.json) 保存文件 SHA-256、许可证来源和精确 npm tarball 完整性值。

技能将扩展 Markdown 转成可在本地浏览的 HTML 说明页，适合流程、比较、架构、排障结论；视频需要显式请求。它通过随包 `scripts/am.mjs` 完成布局，必须执行 Node.js 命令，不是单纯的写作提示。

## 为什么保留在 intake

- 需要 Node.js 20+ 和命令执行；默认写入 `~/.answer-me-with-html/`，还可能打开浏览器。
- CLI 默认在后台访问 GitHub 检查新版本；生成的页面可离线浏览，不代表生成流程默认完全离线。可用 `update_check off` 或 `AM_NO_UPDATE_CHECK` 关闭检查。
- 视频 `voice: auto` 在已有 `ELEVENLABS_API_KEY` 时使用 ElevenLabs，否则使用系统 TTS 或字幕；本地语音接口还有独立端点和可选凭据。视频导出可能需要 Chrome、Node.js 22+，MP4 还需 ffmpeg。
- 上游更新说明面向 `npx skills`、Claude 插件或 Git 安装，尚未适配 SkillFlux 的不可变版本与哈希机制。清理、更新和设置写入也需分别验证。

这些行为不符合当前 SkillFlux 无 shell/network/secrets 权限的安装范围；本次不创建虚假的兼容 manifest，不启用 always-on 规则，也不修改用户现有配置。

## 许可补齐与检查

捆绑脚本含 `marked`、`@dagrejs/dagre` 和图算法依赖。上游脚本末尾引用的 `dagre.esm.js.LEGAL.txt` 未包含在原技能目录。本次根据固定上游 `package-lock.json` 下载精确版本的公开 npm tarball，仅在内存读取许可文件，并验证 SHA-512 SRI；没有安装依赖或执行包代码。

新增许可文件来自 `marked@18.0.14`、`@dagrejs/dagre@3.1.1`、`@dagrejs/graphlib@4.0.5`。完整 `marked` 许可证同时保留其 Markdown 归属条款；Dagre 的原始 LEGAL 文件放在 `scripts/dagre.esm.js.LEGAL.txt`，其余许可放在 `third-party-licenses/`。上游四个技能文件保持逐字不变。

- 本地引用资源齐全，原文与文件哈希核验通过，SkillFlux 静态扫描通过。
- 该完整候选包接近现有 512 KiB 限制，后续版本仍须重新检查大小。
- 没有执行捆绑 CLI、生成页面、调用语音服务或开展真实宿主/人工验收；静态检查不构成运行验证或完整安全审计。
- 人工验收任务与所需能力已列在导入清单。未解决权限、更新所有权和实际宿主验证前，不进入 MCP 可安装索引。

更新检查应监测 `skills/answer-me-with-html`；CLI 捆绑脚本也在该目录内。

2026-10-09（Asia/Shanghai）完整性复核：固定提交中的整个原始 Skill 目录均已逐文件保留（正文、脚本与本地引用无遗漏），`upstreamFiles` 记录原始 Git blob SHA 和字节数，附加许可证仍由完整 `files` 哈希清单覆盖；独立运行工具与在线补充文档保持依赖说明，不混入 Skill 包。
