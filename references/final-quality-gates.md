# Final Quality Gates

Before calling a staged plan package ready:

1. The active version/branch/worktree mapping is unambiguous.
2. Current entrypoints are obvious from root `README.md`, root `AGENTS.md`, and the package index.
3. Legacy plans are archived or clearly labeled historical.
4. The index has stage order, dependency matrix, hard gates, claim boundaries, and final verification.
5. Every stage has objective, likely touched files, required checks, artifacts, gate, PASS/BLOCKED criteria, debug rule, and internal review.
6. Every locked metric, reward, scenario, data mapping, schema, or statistical rule is in a contract/spec file.
7. No stage authorizes downstream work before prerequisite gates.
8. The completed stage set has a consistency review covering logic, contradictions, and causal order.
9. Stop conditions distinguish failed gates, blocked external state, destructive ambiguity, and completed work.
10. Long-running work requires live CSV/JSONL/stdout, TensorBoard when applicable, checkpoints, manifests, and separate evaluation records.
11. Unsupported claims are explicitly prohibited.
12. A text search for old version labels, old entrypoints, and old primary metrics has been reviewed.
13. If Git submission is requested, the same smoke check set ran three consecutive times and recorded commands plus pass_count=3.
14. `git diff --check` or the project equivalent has passed.

If any item fails, report the smallest patch needed instead of broad refactoring.
