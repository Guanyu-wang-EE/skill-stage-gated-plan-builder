# Stage-Gated Plan Builder 技能

<p align="right"><a href="README.md">English</a> | <strong>简体中文</strong></p>

用于创建紧凑、可执行的多阶段计划包，包含明确的 gate、contract、stop rule 与验证路径。

本仓库是该技能的 Git 源镜像。仓库文档保留在这里；精简的安装运行副本只应包含技能本身执行所需文件。

## 目录

- [用途](#用途)
- [仓库地图](#仓库地图)
- [如何使用](#如何使用)
- [核心契约](#核心契约)
- [资源索引](#资源索引)
- [验证命令](#验证命令)
- [维护说明](#维护说明)
- [语言一致性](#语言一致性)

## 用途

当项目需要阶段化计划包而不是松散 checklist 时使用该技能：long-goal prompt、科学实验、review-response roadmap、多 agent 交接，或任何带 phase gate 与 evidence contract 的工作。

预期输出形态是：

```text
1 index + n short stage plans + n contract/spec files + explicit gates
```

## 仓库地图

| 路径 | 作用 |
|---|---|
| [`SKILL.md`](SKILL.md) | 入口、硬门、路由、工作流与验证 |
| [`references/`](references/) | 可按需加载的计划模式、经验教训与最终 gate |
| [`scripts/audit_skill.py`](scripts/audit_skill.py) | 确定性技能审计脚本 |
| [`agents/openai.yaml`](agents/openai.yaml) | 技能列表元数据 |
| [`README.md`](README.md) | 英文仓库导航 |
| [`README_zh.md`](README_zh.md) | 简体中文仓库导航 |

## 如何使用

1. 阅读 [`SKILL.md`](SKILL.md)。
2. 只加载当前任务路由到的 reference。
3. 若窄任务用 checklist 足够，不创建阶段计划包。
4. 若确实需要阶段计划包，先写 index，再写 stage plans，最后写 contracts/specs。
5. 交接前运行 final gates 与 audit script。

## 核心契约

- 一个 checklist 足够时，不创建 staged package。
- index 是 branch/worktree/version、stage order、hard gates 与 claim boundaries 的唯一来源。
- stage 文件保持短：objective、touched files、checks、artifacts、PASS/BLOCKED criteria 与 debug rule。
- contracts/specs 在执行前冻结 metrics、scenarios、rewards、interfaces、schemas 或 statistical rules。
- docs plan 不得授权 implementation、training、cleanup、commit 或 push，除非用户明确要求。

## 资源索引

### 参考文件

| 文件 | 作用 |
|---|---|
| [`stage-package-pattern.md`](references/stage-package-pattern.md) | 计划包布局、index 模板、stage 模板、contracts 与 long-goal prompt 指引 |
| [`lessons-learned.md`](references/lessons-learned.md) | 从困难交接与长运行清理中提炼的可复用计划经验 |
| [`final-quality-gates.md`](references/final-quality-gates.md) | 阶段计划包的最终 readiness audit |

### 脚本

| 文件 | 作用 |
|---|---|
| [`audit_skill.py`](scripts/audit_skill.py) | 检查必需文件、frontmatter、routing sections 与 metadata |

## 验证命令

```powershell
python C:\Users\Admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
python scripts\audit_skill.py .
```

## 维护说明

- 保持 [`SKILL.md`](SKILL.md) 为紧凑路由器；详细模式放入 [`references/`](references/)。
- 当 hard gates、references、scripts 或预期输出变化时，同步更新 README。
- 仅把仓库文档保留在该 Git 镜像中，不放入精简安装运行副本。
- 同步更新 [`README.md`](README.md) 与 [`README_zh.md`](README_zh.md)。

## 语言一致性

[`README.md`](README.md) 是本文档的英文对应版本。两份 README 应保持相同章节、声明、命令与维护预期。
