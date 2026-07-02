# Lessons Learned For Stage-Gated Planning

These lessons are generalized from real multi-agent planning cleanup work. Apply them when turning a messy repo, review response, or long-run handoff into a staged plan.

## 1. Version Names Are Scientific State, Not Decoration

If branch name, project version, and internal plan label disagree, fix the routing before implementation. The index must state:

- active branch/worktree;
- historical backup branches;
- forbidden push targets;
- which docs are authoritative.

Ambiguous labels make agents push to the wrong branch or treat a backup snapshot as the active plan.

## 2. Root Entrypoints Beat Deep Docs

Agents often read root `README.md`, root `AGENTS.md`, and obvious root plans before deep docs. If old plans remain in root, they will be treated as current even if a newer folder exists.

Keep root clean:

- root README points to the active index;
- root AGENTS gives routing and archive boundary;
- old plans move to archive or are clearly labeled historical;
- manuscript drafts and evidence notes say when they are superseded.

## 3. Do Not Let Old Metrics Coexist As Primaries

When a new plan supersedes an old metric or scenario assumption, write an explicit override rule. Otherwise future agents may report both as primary evidence.

Good override wording:

```text
For the new paper-facing matrix, metric A/B/C supersede old metric X.
Old metric X remains diagnostic unless explicitly re-approved.
```

## 4. Contracts Freeze Meaning Before Work Starts

Long training before contract freeze creates expensive but scientifically unusable artifacts. Freeze these before smoke/pilot/formal runs:

- reward/cost signs and units;
- primary metrics and ranking;
- scenario seeds and leakage rules;
- data mapping;
- physics invariants;
- statistical analysis plan.

## 5. Gate Failure Blocks Advancement, Not the Whole Goal

A failed gate should not make the agent stop immediately. It should trigger bounded debugging:

```text
reproduce -> first incorrect value -> one hypothesis -> one minimal test -> one minimal patch -> retest
```

After five distinct failed hypotheses, mark `BLOCKED` with evidence. Do not loop indefinitely or skip the gate.

## 6. Smoke Evidence Is Not Formal Evidence

A smoke run proves wiring, file writes, and round-trip checkpoints. It does not prove convergence, superiority, feasibility distribution, or paper-level performance.

Plans should explicitly separate:

- smoke;
- pilot;
- formal training;
- held-out evaluation;
- report/claim pack.

## 7. Necessary Repetition Is Different From Bloat

Keep shared rules in the index and contracts. Repeat only the small local context a stage agent needs to avoid dangerous mistakes when it opens one stage file alone.

Useful repetition:

- prerequisite gates;
- forbidden shortcuts;
- exact stage PASS/BLOCKED criteria;
- artifact names.

Bad repetition:

- copying the whole index into every stage file;
- duplicating metric formulas across multiple files;
- maintaining stale pasted versions of generated files.

## 8. Long-Goal Prompts Should Be Causal, Not Encyclopedic

A good handoff prompt points to the right files and states the causal chain:

```text
contracts -> plumbing -> smoke -> pilot -> formal -> evaluation -> report
```

Do not repeat every stage detail in the prompt when the files already contain it. Repetition in the prompt should emphasize gates, stop rules, and reproducibility duties.

## 9. Archive Does Not Mean Delete Evidence

Do not destroy old plans, failed runs, or manuscript notes when they may be useful history. Move them to archive and label their role. Preserve evidence; remove it only from the current execution path.

## 10. Claims Need Negative Space

A plan must say what cannot be claimed until evidence exists. Examples:

- no reward superiority from shaped training rewards;
- no fairness claim from diagnostic settlement code;
- no feeder-feasible claim from voltage-only screens;
- no scalability claim from fixed small cases;
- no algorithm superiority from single-seed or smoke evidence.

Unsupported claims should be blocked in the index, stage files, and final claim pack.

## 11. Reproducibility Is A Live-Run Property

For long-running RL/scientific work, final-only plots are too late. Require live artifacts:

- `progress.csv`;
- `episodes.csv`;
- `updates.csv`;
- `stdout.log`;
- TensorBoard events;
- checkpoints/latest and checkpoints/best;
- config, command, commit, manifest, diagnostics.

Training and evaluation records must stay separate.

## 12. The Best Plan Is Still Small

The target is not "many files". The target is enough structure that another agent cannot reasonably:

- start at the wrong entrypoint;
- skip prerequisite gates;
- compare incompatible metrics;
- treat diagnostics as claims;
- lose failed-run evidence;
- push to the wrong branch.

Use the smallest index/stage/contract package that prevents those failures.

## 13. Critic Review And Handoff Prompt Are First-Class Files

For nontrivial packages, do not bury the final critique inside a stage paragraph. A separate `PLAN_CRITIC_REVIEW.md` makes completeness, logic, contradictions, causal order, risks, evidence paths, and smallest required patch visible at the package root.

For unattended or multi-agent work, do not rely on chat history as the handoff. A separate `LONG_GOAL_PROMPT.md` should point to the worktree, index, reading order, first incomplete gate, hard gates, failure rule, and expected artifacts. Keep it causal and short; let the index and stage files carry the details.
