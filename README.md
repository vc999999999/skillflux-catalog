# SkillFlux Catalog

SkillFlux 的精选技能目录仓库。客户端（`skillflux` CLI / MCP）从此仓库拉取 `index.json`，
并把所有下载固定在解析到的 commit SHA 上，逐文件校验 sha256。

## 结构

```
skills/<id>/<version>/
├── skillflux.json          # 声明性清单：id、版本、入口、依赖、权限、宿主
├── skillflux.review.json   # 审核记录 + 绑定内容哈希的人工评测证据
└── SKILL.md 及其他内容文件
index.json                  # 由 `skillflux catalog build` 生成，客户端唯一入口
```

## 维护流程

修改技能内容后运行 `skillflux catalog build`（来自 [SkillFlux 主仓库](https://github.com/vc999999999/Skillflux_Cloudflare)），
提交生成的 `index.json`。CI 会运行 `skillflux catalog build --check`：`index.json` 与目录内容不一致即失败。

同一 `<id>/<version>` 目录内容不可变；内容变更必须新增版本目录。`skillflux.review.json`
中 `kind: "simulation"` 的评测不能使版本获得 qualified 资格。

## 状态

当前 9 个条目为开发种子（`needs-testing` 状态，simulation 证据）——它们**不是**已通过真人实测的
可安装版本。 client 搜索不会返回它们。真实合格版本将带有人工评测记录逐步发布。
