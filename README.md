# benchmark-cc

A/B testing harness for Claude Code configurations. Compares 5 generic setups across 5 isolated tasks, measuring tokens, wall-time, tool usage, and quality (LLM-judged).

## Results at a glance

One runner, 7 setups, 13 tasks, 390 runs. Full tables: [report.md](report.md).

| Setup | Avg quality (/10) | Pass rate | Avg time (s) | Avg cost ($) |
|---|---|---|---|---|
| `A_stock` (no config) | 9.44 | 60/65 | 54.3 | 0.25 |
| `B_md` (CLAUDE.md only) | 9.53 | 60/65 | 51.0 | 0.26 |
| `E_full` (public best practice) | 9.45 | 60/65 | 51.4 | 0.27 |
| `G_alice_personal` (a real personal setup) | 9.50 | 55/55 | 62.8 | 0.30 |

On isolated coding tasks the configuration layers moved judged quality by less than
0.1 points. The personal setup passed all of its runs and cost about 20% more per run
than the empty baseline.

**Goal:** measure what each *layer* of `~/.claude/` configuration contributes — CLAUDE.md, agents, skills, hooks — on identical tasks, with no personal/project content. Results are reproducible across machines.

## Setups

Generic baseline (A-F) are reference points, all committed and public. **Personal slots (G_*_personal) are the headline comparison — each runner uses their own.** See `PERSONAL.md`.

| Setup | CLAUDE.md | Agents | Skills | Hooks | Source / purpose |
|---|---|---|---|---|---|
| `A_stock` | — | — | — | — | Empty baseline |
| `B_md` | generic 30-line | — | — | — | CLAUDE.md alone |
| `C_md_agents` | generic | 10 from [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | — | — | + agents |
| `D_md_skills` | generic | — | 14 from [obra/superpowers](https://github.com/obra/superpowers) | — | + skills |
| `E_full` | generic | + agents | + skills | secrets-scan | Full generic best-practice |
| `F_full_plus_domain` | generic | + 4 domain experts | + skills | secrets-scan | Domain-agent value (T6/T7 only) |
| `G_<runner>_personal` | yours | yours | yours | yours | **Your real `~/.claude`** — bootstrap with `./bootstrap-personal.ps1` |

Comparisons that matter:
- `A_stock` vs `G_alice_personal` → does your entire setup beat zero config?
- `E_full` (public best-practice) vs `G_alice_personal` → does personalization beat the generic stack?
- `G_alice` vs `G_bob` → whose setup wins on these tasks?

**Generic agents:** `debugger`, `code-reviewer`, `reviewer`, `refactoring-specialist`, `developer`, `test-engineer`, `tester`, `prompt-engineer`, `security-engineer`, `performance-engineer`.

**Generic skills:** `brainstorming`, `writing-plans`, `executing-plans`, `verification-before-completion`, `test-driven-development`, `systematic-debugging`, `using-superpowers`, `requesting-code-review`, `receiving-code-review`, `finishing-a-development-branch`, `subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees`, `writing-skills`.

**Generic CLAUDE.md** (`setups/B_md/.claude/CLAUDE.md`): ~30 lines on think-first / simplicity / surgical edits / explicit success criteria / code defaults / verification. No project specifics.

## Tasks

### Phase 1 — isolated coding tasks (5)
- `T1_bug` — Python off-by-one in pytest-covered util
- `T2_lru` — Implement LRU cache (TypeScript) with provided test suite
- `T3_refactor` — Clean up deeply nested order-processing function, preserve behavior
- `T4_crud` — Add `PATCH /users/:id` to mini Express app, validation included
- `T5_trace` — Debug from stack trace, multi-file type-coercion root cause

### Phase 2 — CLAUDE.md rule-adherence probes (5)

Each M-task tempts a specific anti-pattern that violates a rule in `B_md/CLAUDE.md`. Setup A_stock (no CLAUDE.md) should systematically violate; B-E should adhere.

- `M1_no_comments` — adds a simple function; probe rule: "No comments unless WHY is non-obvious"
- `M2_minimal_change` — fixes one failing test; probe rule: "Smallest change that solves the actual problem"
- `M3_no_internal_validation` — adds a private helper; probe rule: "Validate at boundaries only. Trust internal code."
- `M4_run_tests` — fixes a bug; probe rule: "Run test suite, report pass/fail explicitly" (checked by stream-scan for pytest invocation)
- `M5_multiturn_memory` — **real 2-turn session via `--resume`**. Turn 1: state 6 project constraints. Turn 2: write notes.md from memory. Probes cross-turn fact retention.

### Phase 3 — domain-agent tasks (2, run on E and F only)

- `T6_db_schema` — Prisma schema design with indexes (triggers `prisma-expert` if present)
- `T7_tg_bot` — grammY Telegram bot with command handlers (triggers `telegram-bot-expert`)

### Phase 4 — long-context (1)

- `T8_longctx` — bug fix in a ~2800-line synthetic Python module (~70KB / ~18K tokens of code)

### Run count

| Phase | Tasks | Setups per task | Subtotal (per runner) |
|---|---|---|---|
| 1 | 5 | 5 (A–E) | 25 |
| 2 (M*) | 5 | 5 (A–E) | 25 |
| 3 (T6/T7) | 2 | 6 (A–F) | 12 |
| 4 (T8) | 1 | 5 (A–E) | 5 |
| **Total per runner** | **13** | | **67** |

With `--samples 5` (recommended for variance estimation): **335 runs per runner**, **670 across both**.
With `--samples 1` (smoke / quick look): **134 total**.

## Prerequisites

- Windows + PowerShell 7+
- Claude Code `>= 2.1.119` recommended (older versions had a known quality regression — see Anthropic's April 2026 disclosure)
- Node.js 20+
- Git
- Claude Pro / Max subscription (run `claude /login` once before starting)

## Quickstart (no git required)

Two flows: with git (collaboration via GitHub) or zip-only (send file → run → send results back).

### Zip-only flow (recommended for ad-hoc 2-person run)

**You (owner):**

```powershell
./setup.ps1
./bootstrap-personal.ps1 -Runner alice            # your ~/.claude → G_alice_personal (local)
node runner.mjs --runner alice --samples 5        # ~15-20h on Max 20×
./package-for-friend.ps1                          # creates ../benchmark-cc-friend.zip
# Send ../benchmark-cc-friend.zip to friend via Telegram/email/drive
```

**Friend:** (instructions also in `FRIEND.md` inside the zip)

```powershell
# extract benchmark-cc-friend.zip somewhere
./setup.ps1
./bootstrap-personal.ps1 -Runner bob
node runner.mjs --runner bob --samples 5
./package-my-results.ps1 -Runner bob              # creates ../benchmark-results-bob.zip
# Send back to you
```

**You (after receiving friend's zip):**

```powershell
./import-friend-results.ps1 -ZipPath path/to/benchmark-results-bob.zip
node judge.mjs                                    # judges both runners
node merge.mjs                                    # outputs report.md
```

### Git flow

```powershell
git clone <repo-url>
cd benchmark-cc
./setup.ps1
./bootstrap-personal.ps1 -Runner <yourname>
node runner.mjs --runner <yourname> --samples 5
git add results/ runs/ && git commit -m "<yourname> run" && git push
```

After both runners push, one of you runs `node judge.mjs && node merge.mjs && git add results/ report.md && git push`.

Drop `--samples 5` for a quick smoke run (`--samples 1`).

After both runners push:

```powershell
node judge.mjs                       # LLM-judges all rows
node merge.mjs                       # outputs report.md
```

## Subscription tier — expected wall-clock

| Tier | 62 runs (one runner) |
|---|---|
| Pro (~45 msg / 5h) | ~1 week |
| Max 5× (~225 msg / 5h) | ~1-2 days |
| Max 20× (~900 msg / 5h) | ~3-5 hours |

`runner.mjs` auto-resumes on rate limit; existing rows are skipped on re-run.

## Why this exists

Existing public benchmarks compare CC against Codex/Cursor, or compare CC version-to-version. None systematically isolate the contribution of each `~/.claude/` config layer on the same task suite with content controlled for personal bias.

Question this answers: **what fraction of Claude Code's effective behavior comes from CLAUDE.md vs agents vs skills vs hooks** — independently of any one user's project context.

## Privacy & attribution

All configs in this repo are generic. No author's personal CLAUDE.md, memory, or project context. Each runner's `~/.claude/.credentials.json` is gitignored and never leaves their machine.

**Sources:**
- `setups/D_md_skills/.claude/skills/` and `setups/E_full/.claude/skills/` — verbatim from [obra/superpowers](https://github.com/obra/superpowers) (MIT)
- `setups/C_md_agents/.claude/agents/` and `setups/E_full/.claude/agents/` — selected agents from [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) (MIT)
- `setups/B_md/.claude/CLAUDE.md` — original, 30 lines of generic engineering practices
- Domain agents in `setups/F_full_plus_domain/.claude/agents/` (prisma-expert, telegram-bot-expert, supabase-expert, chrome-extension-expert) — from `~/.claude/agents/`, scanned and verified to contain no personal/project references
