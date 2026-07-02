import pathlib
import re
import sys


REQUIRED = [
    "SKILL.md",
    "references/stage-package-pattern.md",
    "references/lessons-learned.md",
    "references/final-quality-gates.md",
    "scripts/audit_skill.py",
    "agents/openai.yaml",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> None:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[1]
    for rel in REQUIRED:
        if not (root / rel).exists():
            fail(f"missing {rel}")

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    if "TODO" in skill:
        fail("SKILL.md still contains TODO")
    if not re.search(r"^---\nname: stage-gated-plan-builder\ndescription: .+\n---", skill, re.S):
        fail("invalid SKILL.md frontmatter")
    for needle in ["## Hard Gates", "## Reference Routing", "## Verification"]:
        if needle not in skill:
            fail(f"missing {needle}")
    for needle in ["internal review", "three consecutive", "logical consistency", "PLAN_CRITIC_REVIEW.md", "LONG_GOAL_PROMPT.md"]:
        if needle not in skill:
            fail(f"missing stage-gate control: {needle}")

    pattern = (root / "references/stage-package-pattern.md").read_text(encoding="utf-8")
    for needle in ["Internal review:", "Plan Critic Review File", "LONG_GOAL_PROMPT.md", "pass_count=3"]:
        if needle not in pattern:
            fail(f"stage-package-pattern missing {needle}")

    gates = (root / "references/final-quality-gates.md").read_text(encoding="utf-8")
    for needle in ["internal review", "PLAN_CRITIC_REVIEW.md", "LONG_GOAL_PROMPT.md", "logic, contradictions, and causal order", "pass_count=3"]:
        if needle not in gates:
            fail(f"final-quality-gates missing {needle}")

    meta = (root / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$stage-gated-plan-builder" not in meta:
        fail("default_prompt must mention $stage-gated-plan-builder")

    print("stage_gated_plan_builder_audit_pass")


if __name__ == "__main__":
    main()
