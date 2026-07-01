# Stage Package Pattern

## When To Use

Use a stage package when the work has irreversible order, scientific claims, long-running work, multiple agents, or cross-file contracts. Use a single checklist when the work has one owner, one module, and no phase gate.

## Index Template

`00_INDEX.md` should contain:

- purpose and non-goals;
- active branch/worktree/version and forbidden push targets;
- current vs archive/historical boundary;
- required reading order;
- stage order table;
- dependency matrix;
- global hard gates;
- claim boundaries;
- debug and stop rules;
- reproducibility/artifact rules;
- final verification commands.

Keep the index concise. Link to contracts/specs instead of copying their full content.

## Stage Plan Template

Each `stage_<n>_<name>.md` should contain:

```text
# Stage <n>: <Name>

Objective:
Files likely touched later:
Inputs/contracts:
Required tests/checks:
Required artifacts:
Gate:
PASS criteria:
BLOCKED criteria:
Five-cycle debug rule:
Forbidden shortcuts:
Internal review:
```

Stage files may repeat only the rules needed for safe execution when an agent opens that file alone. Put broad shared policy in `00_INDEX.md`.

`Internal review` must answer: scope is bounded; prerequisites exist or are blocked; artifacts and checks are named; PASS/BLOCKED criteria are testable; no downstream stage is silently authorized.

## Contract/Spec Files

Create separate contract/spec files when values must not drift during implementation or training:

| Contract/spec | Use |
|---|---|
| `reward_contract.yaml` | reward/cost terms, signs, units, prohibited shaping advantages |
| `metric_spec.yaml` | primary metrics, ranking, infeasible-run handling |
| `scenario_spec.yaml` | train/validation/test split, seeds, leakage rules |
| `data_mapping_contract.json` | dataset-to-environment mapping |
| `physics_invariant_tests.md` | scientific invariants and tolerances |
| `statistical_analysis_plan.md` | paired unit, CI, tests, incomplete-run handling |

Do not hide scientific semantics inside run scripts when they belong in a contract.

## Gate Record Minimum

Every gate must record:

```text
scientific_claim
scope
metric
tolerance
observable_class
verdict
artifacts
allowed_next_actions
blocked_next_actions
```

Use only these verdicts unless the project defines stricter values:

```text
PASS
PROVISIONAL PASS
FAIL
INCONCLUSIVE
BLOCKED
NOT RUN
```

Diagnostic-only failures do not fail the whole plan unless they affect learning signal, safety semantics, evaluation validity, or a locked claim.

## Long-Goal Prompt Skeleton

Use this when handing the package to another agent:

```text
Start an unattended long-goal run in <worktree>.

Objective:
Execute the first incomplete required gate from <index>. Follow the causal chain:
contracts -> implementation/plumbing -> smoke -> pilot -> formal run -> separate evaluation -> report/claim pack.

First actions:
1. Run git status/branch/remote/HEAD and record dirty state.
2. Read AGENTS.md, README.md, <index>, required contracts/specs, then the target stage file.
3. Identify the first incomplete gate.

Hard gates:
- Do not start downstream work before prerequisite gates PASS.
- Do not change locked scientific semantics without explicit approval.
- On failure, run up to five distinct-hypothesis debug cycles, then mark BLOCKED with evidence.
- Before authorized commit/push, run the same smoke check set three consecutive times and record pass_count=3.

Artifacts:
Write live CSV/JSONL/stdout/checkpoints/TensorBoard for long runs.
Keep train/eval records separate.
Do not average failed or infeasible runs into performance means.
```

## Anti-Patterns

- A long plan with no index.
- Stage files that restate the same policy paragraphs.
- Metrics defined only in prose, not in a contract/spec.
- Old documents left in root as current-looking entrypoints.
- Gates that say "works" without claim, metric, tolerance, and artifacts.
- Long training before contract/plumbing/smoke gates.
- Manuscript claims stronger than the evidence package.
- Git submission after only one smoke pass when three were required.
