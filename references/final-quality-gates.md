# Final Quality Gates

Before calling a staged plan package ready:

1. The active version/branch/worktree mapping is unambiguous.
2. Current entrypoints are obvious from root `README.md`, root `AGENTS.md`, and the package index.
3. Legacy plans are archived or clearly labeled historical.
4. The index has stage order, dependency matrix, hard gates, claim boundaries, and final verification.
5. Every stage has objective, likely touched files, required checks, artifacts, gate, PASS/BLOCKED criteria, and debug rule.
6. Every locked metric, reward, scenario, data mapping, schema, or statistical rule is in a contract/spec file.
7. No stage authorizes downstream work before prerequisite gates.
8. Stop conditions distinguish failed gates, blocked external state, destructive ambiguity, and completed work.
9. Long-running work requires live CSV/JSONL/stdout, TensorBoard when applicable, checkpoints, manifests, and separate evaluation records.
10. Unsupported claims are explicitly prohibited.
11. A text search for old version labels, old entrypoints, and old primary metrics has been reviewed.
12. `git diff --check` or the project equivalent has passed.

If any item fails, report the smallest patch needed instead of broad refactoring.
