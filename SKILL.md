---
name: stage-gated-plan-builder
description: Create compact, execution-ready multi-stage planning packages with one index, short stage plans, contract/spec files, scientific gates, stop/debug rules, and reproducibility handoffs. Use when designing or auditing staged project plans, long-goal prompts, RL/scientific experiment plans, review-response roadmaps, or any workflow that needs phase gates and evidence contracts.
---

# Stage-Gated Plan Builder

## Overview

Use this skill to turn a messy project, review response, experiment campaign, or long-goal request into a small executable planning package:

```text
1 index + n short stage plans + n contract/spec files + explicit gates
```

Prefer the smallest package that prevents mis-execution. Do not create a multi-stage plan when a single checklist is enough.

## Hard Gates

- Read existing `AGENTS.md`, `README.md`, current indexes, and nearest project instructions before drafting or editing a plan.
- Define the active branch/worktree/version and the archive/historical boundary in the index.
- Every stage must have a gate, owner scope, likely touched files, required artifacts, verification commands, PASS/BLOCKED criteria, and stop/debug behavior.
- Put shared rules in the index or contracts, not repeated prose inside every stage file.
- Separate contract/spec files from stage plans when metrics, scenarios, rewards, interfaces, schemas, or statistical rules must stay stable.
- Do not authorize implementation, training, destructive cleanup, commit, or push from a docs plan unless the user explicitly asks.
- Do not claim scientific, performance, fairness, safety, or feasibility conclusions that the gates do not support.

## Reference Routing

| User task | Load |
|---|---|
| Create or revise a staged plan package | `references/stage-package-pattern.md` |
| Generate a concise long-goal prompt from the plan package | `references/stage-package-pattern.md` |
| Summarize, transfer, or harden lessons from a prior planning conversation | `references/lessons-learned.md` |
| Audit readiness, contradictions, old-entry routing, or completion claims | `references/final-quality-gates.md` |
| Validate this skill folder after edits | `scripts/audit_skill.py` |

## Minimal Workflow

1. **Triage YAGNI:** If the task is one narrow change, write a checklist instead of a staged package.
2. **Freeze routing:** Name active branch/worktree/version, forbidden targets, archive boundary, and reading order.
3. **Define causal order:** Sort stages by dependency, not topic preference. Contracts and plumbing precede smoke; smoke precedes pilot; pilot precedes formal runs.
4. **Write the index first:** It is the source of truth for branch mapping, stage order, hard gates, and claim boundaries.
5. **Write short stage files:** One objective, likely touched files, required tests, required artifacts, PASS/BLOCKED criteria, and debug rule.
6. **Write contract/spec files:** Freeze metrics, scenarios, schemas, reward/cost semantics, statistical analysis, or interface contracts.
7. **Add gate records:** Each scientific gate states claim, scope, metric, tolerance, observable class, verdict, artifacts, allowed next actions, and blocked next actions.
8. **Audit before handoff:** Check for duplicate/conflicting entrypoints, stale version labels, missing gates, and unsupported claims.
9. **Capture lessons:** When the plan came from a difficult conversation or failed long run, write the reusable lessons into the package or prompt, not just the abstract structure.

## Output Shape

Prefer this layout:

```text
docs/<plan_name>/
  00_INDEX.md
  stage_0_<name>.md
  stage_1_<name>.md
  ...
  <domain>_contract.yaml
  <metric_or_schema>_spec.yaml
  statistical_analysis_plan.md
```

If legacy notes must be kept, move or label them as archive/history and point the current index away from them.

## Verification

After editing this skill:

```powershell
python C:\Users\Admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\Admin\.codex\skills\stage-gated-plan-builder
python C:\Users\Admin\.codex\skills\stage-gated-plan-builder\scripts\audit_skill.py C:\Users\Admin\.codex\skills\stage-gated-plan-builder
```
