# Stage-Gated Plan Builder Skill

<p align="right"><strong>English</strong> | <a href="README_zh.md">简体中文</a></p>

Create compact, execution-ready multi-stage planning packages with explicit gates, contracts, stop rules, and validation.

This repository is the Git-backed source mirror for the skill. Repository documentation belongs here; lean installed runtime copies should contain only files needed by the skill itself.

## Table Of Contents

- [Purpose](#purpose)
- [Repository Map](#repository-map)
- [How To Use](#how-to-use)
- [Core Contracts](#core-contracts)
- [Resource Index](#resource-index)
- [Validation Commands](#validation-commands)
- [Maintenance Notes](#maintenance-notes)
- [Language Parity](#language-parity)

## Purpose

Use this skill when a project needs a staged plan package rather than a loose checklist: long-goal prompts, scientific experiments, review-response roadmaps, multi-agent handoffs, or work with phase gates and evidence contracts.

The intended output shape is:

```text
1 index + n short stage plans + n contract/spec files + explicit gates
```

## Repository Map

| Path | Role |
|---|---|
| [`SKILL.md`](SKILL.md) | Entry point, hard gates, routing, workflow, and verification |
| [`references/`](references/) | Loadable planning patterns, lessons, and final gates |
| [`scripts/audit_skill.py`](scripts/audit_skill.py) | Deterministic skill audit |
| [`agents/openai.yaml`](agents/openai.yaml) | Skill listing metadata |
| [`README.md`](README.md) | English repository navigation |
| [`README_zh.md`](README_zh.md) | Simplified Chinese repository navigation |

## How To Use

1. Read [`SKILL.md`](SKILL.md).
2. Load only the routed reference for the task.
3. Prefer a checklist when the work is narrow enough.
4. If a staged package is justified, write the index first, then stage plans, then contracts/specs.
5. Before handoff, run the final gates and audit script.

## Core Contracts

- Do not create a staged package when one checklist is enough.
- The index is the source of truth for branch/worktree/version, stage order, hard gates, and claim boundaries.
- Stage files stay short: objective, touched files, checks, artifacts, PASS/BLOCKED criteria, and debug rule.
- Contracts/specs freeze metrics, scenarios, rewards, interfaces, schemas, or statistical rules before execution.
- A docs plan must not authorize implementation, training, cleanup, commit, or push unless the user explicitly asks.

## Resource Index

### References

| File | Role |
|---|---|
| [`stage-package-pattern.md`](references/stage-package-pattern.md) | Plan package layout, index template, stage template, contracts, long-goal prompt guidance |
| [`lessons-learned.md`](references/lessons-learned.md) | Reusable planning lessons from difficult handoffs and long-run cleanup |
| [`final-quality-gates.md`](references/final-quality-gates.md) | Final readiness audit for staged plan packages |

### Scripts

| File | Role |
|---|---|
| [`audit_skill.py`](scripts/audit_skill.py) | Checks required files, frontmatter, routing sections, and metadata |

## Validation Commands

```powershell
python C:\Users\Admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
python scripts\audit_skill.py .
```

## Maintenance Notes

- Keep [`SKILL.md`](SKILL.md) as a compact router; put detailed patterns in [`references/`](references/).
- Update README files when hard gates, references, scripts, or expected outputs change.
- Keep repository-only documentation in this Git mirror, not in lean installed runtime copies.
- Update [`README.md`](README.md) and [`README_zh.md`](README_zh.md) together.

## Language Parity

[`README_zh.md`](README_zh.md) is the Simplified Chinese counterpart of this file. The two READMEs should keep the same sections, claims, commands, and maintenance expectations.
