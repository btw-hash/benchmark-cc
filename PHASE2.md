# Phase 2 — memory & depth tests (not yet implemented)

Phase 1 (T1-T5) measures CLAUDE.md / agents / skills / hooks on code tasks. It does **not** meaningfully measure memory contribution, because:

- `claude -p` runs single-shot — no cross-session continuity.
- `MEMORY.md` content is project-specific; isolated tasks don't touch it.
- Domain-specific skills/agents (e.g. `prisma-expert`, `telegram-bot-expert`) won't fire on generic code tasks.

Phase 2 adds four targeted probes:

## M1_recall — long-context retention

Single prompt with a relevant fact buried 4-5 turns of "work" before the final question.

- Setup: prompt opens with "Note: this codebase uses header `X-Tenant: acme` on every outbound request." Then 4 unrelated steps. Final step: "Add a call to `/api/foo`."
- Verify: diff contains the header.
- Probes: how well long-context attention holds across distractors.

## M2_convention — CLAUDE.md adherence

Repo with a CLAUDE.md saying: "All errors return `Result<T, E>`. Never `throw`."

- Task: "Add `divide(a, b)` to `math.ts` with sane error handling."
- Verify: no `throw` in diff; `Result` type used.
- Probes: whether each setup's CLAUDE.md propagates project rules to the active session.

## M3_skill_trigger — skill discoverability

Prompt phrased to match a generic skill trigger ("help me plan a zero-downtime DB migration" → `writing-plans` or `brainstorming`).

- Verify: scan `stream.jsonl` for a `Skill()` tool use with the expected name.
- Probes: does the setup's skill list make the right skill discoverable? Setup A (no skills) fails by design.

## M4_memory_recall — memory injection

Pre-seed `setups/<s>/.claude/projects/.../memory/MEMORY.md` with: "Our deploy command is `make ship-prod`."

- Task: "Deploy this branch."
- Verify: diff or final message mentions `make ship-prod`, not invented commands.
- Probes: does the setup actually load and use memory? Setup A (no memory dir) fails by design.

## Implementation notes

- Each M-test is one task dir under `tasks/M*/`, with `prompt.md`, `verify.ps1` or `verify.mjs` (some verify by stream-grep, not file diff), and seed assets where needed.
- `runner.mjs` needs no changes — these are normal single-shot runs.
- `judge.mjs` rubric stays the same; quality dimensions are still informative.
