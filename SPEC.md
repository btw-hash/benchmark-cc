# benchmark-cc — Specification

## 1. Question

> What fraction of Claude Code's effective behavior comes from each layer of a `~/.claude/` configuration — CLAUDE.md, agents, skills, hooks — independently of any one user's project context?

Existing public benchmarks compare CC against competing tools (Codex, Cursor) or one CC version against another. None systematically isolate the marginal contribution of each config layer on the same task suite with content controlled for personal bias.

## 2. Hypotheses

| H# | Statement | If supported by data |
|---|---|---|
| H1 | Adding a generic CLAUDE.md (~30 lines) reduces output_tokens and turns vs. stock | CLAUDE.md is worth keeping even if you have nothing project-specific to say |
| H2 | Adding 10 generic agents (debugger, refactoring-specialist, ...) does not measurably improve quality on isolated coding tasks | Agents are only valuable when their description matches the task — irrelevant collection is dead weight |
| H3 | Adding 14 generic skills (TDD, systematic-debugging, ...) increases turns and cache_creation but improves scope_discipline / completeness scores | Skills change *how* the model approaches work; trade-off is latency for quality |
| H4 | Hooks (secrets-scan) add measurable per-Edit/Write latency with no quality impact on these tasks | Hook value is invisible until they fire on something dangerous |
| H5 | E_full > sum(B_md + C_md_agents + D_md_skills) — i.e. there is positive interaction between layers | Best practice is the combined stack, not picking one layer |
| H6 | cache_creation grows ~linearly with config size; cache_read stays roughly constant | Bigger configs are more expensive every cold session but identical on warm |

## 3. Experimental design

### 3.1 Independent variable

A single discrete variable: **setup**, with 6 levels.

| Level | CLAUDE.md | Agents | Skills | Hooks | Layers active |
|---|---|---|---|---|---|
| A_stock | — | — | — | — | 0 |
| B_md | generic 30-line | — | — | — | 1 |
| C_md_agents | generic | 10 generic | — | — | 2 |
| D_md_skills | generic | — | 14 generic | — | 2 |
| E_full | generic | 10 generic | 14 generic | secrets-scan | 4 |
| F_full_plus_domain | generic | 10 generic + 4 domain | 14 generic | secrets-scan | 4 + domain agents |

C and D both have **2 layers** but different ones — head-to-head agents vs skills marginal contribution. E vs F isolates **domain-specific agent value** on tasks where their domain matches (T6, T7).

### 3.2 Dependent variables (measured)

Per run, captured from `claude -p --output-format stream-json` final event + verification:

| Variable | Source | Type |
|---|---|---|
| `wall_ms` | runner.mjs timer | continuous (latency) |
| `duration_api_ms` | stream `result.duration_api_ms` | continuous (server-side time) |
| `num_turns` | stream `result.num_turns` | discrete (interaction depth) |
| `input_tokens` | stream `result.usage.input_tokens` | continuous (cost) |
| `output_tokens` | stream `result.usage.output_tokens` | continuous (cost) |
| `cache_read_input_tokens` | stream | continuous (cost — warm) |
| `cache_creation_input_tokens` | stream | continuous (cost — cold) |
| `total_cost_usd` | stream `result.total_cost_usd` | continuous (implied $) |
| `tool_calls` (per tool) | counted from `assistant` events with `tool_use` blocks | discrete |
| `files_touched` | count of `diff` blocks (filtered for build artifacts) | discrete |
| `passed` | exit code of `verify.ps1` | boolean |
| `quality.correctness` | LLM judge | ordinal 1-10 |
| `quality.completeness` | LLM judge | ordinal 1-10 |
| `quality.scope_discipline` | LLM judge | ordinal 1-10 |
| `quality.code_quality` | LLM judge | ordinal 1-10 |

### 3.3 Controlled variables

| Control | How enforced |
|---|---|
| Model | `--model claude-opus-4-7` on every run |
| Permission mode | `--permission-mode bypassPermissions` on every run |
| CC version | `setup.ps1` warns if `< 2.1.119`; both runners must run identical major+minor |
| OS | Windows + PowerShell 7+ (both runners) |
| Task starting state | Each run copies `tasks/<T>/repo/` into a fresh worktree; no inter-run contamination |
| Auth | Each runner's `~/.claude/.credentials.json` is copied into each setup config dir per run; never committed |
| Prompt | Identical `prompts/<T>/prompt.md` for both runners |
| Judge | Single instance, single rubric, identical model — same person runs `judge.mjs` over combined results |

### 3.4 Nuisance variables (acknowledged, not eliminated)

| Source | Why it's there | Mitigation |
|---|---|---|
| Network latency | Each runner's connection differs | Report `wall_ms` per-runner; aggregate only tokens/quality (network-independent) |
| Model temperature / sampling | Opus 4.7 is not deterministic | Two runners × same setup × same task = noise floor estimate; quality deltas smaller than noise floor → not significant |
| CC version drift mid-run | New auto-update during run | `setup.ps1` pins; recommended to disable autoupdate (env `DISABLE_AUTOUPDATER=1`) before starting |
| Cache state at session start | Cold vs warm | Reported separately (`cache_creation` vs `cache_read`) instead of summed |

### 3.5 Sample

- **Tasks (T):** 12 (5 isolated + 4 M-probes + 2 domain + 1 long-context)
- **Setups (S):** 6 (F runs only on domain tasks; others on all 5 base setups)
- **Runners (R):** 2

Per-runner matrix size: 62. Across runners: **124 runs**.

| Phase | Tasks | Setups | Subtotal/runner |
|---|---|---|---|
| 1 (isolated) | 5 | 5 (A–E) | 25 |
| 2 (M* rule probes) | 4 | 5 (A–E) | 20 |
| 3 (domain) | 2 | 6 (A–F) | 12 |
| 4 (long-context) | 1 | 5 (A–E) | 5 |

Each (S, T) cell has n=2 observations — enough to estimate variance, not enough for inferential statistics. Findings remain descriptive. For inference, would need n≥30 per cell — out of scope for this MVP.

Per-task setup whitelist mechanism: a task may include a `.setups` file (one setup name per line). If absent, defaults exclude `F_full_plus_domain` (which is only active for tasks that explicitly opt-in — T6 and T7).

## 4. Tasks

### 4.1 Phase 1 — isolated coding (5)

Heterogeneous mix surfacing different config strengths.

| ID | Type | Language | What it probes | Verify |
|---|---|---|---|---|
| `T1_bug` | bug fix | Python | Trivial fix (3 LOC). Measures setup *overhead*: if E_full takes 4× tokens of A_stock for this, the surplus isn't earning quality. | pytest green |
| `T2_lru` | implementation | TypeScript | O(1) data structure from spec. Tests algorithmic reasoning + adherence to complexity constraint. | vitest green |
| `T3_refactor` | refactor | Python | Behavior-preserving cleanup of nested if/else. Tests scope discipline. | pytest green |
| `T4_crud` | feature | Express/JS | Multi-requirement endpoint with validation. Tests requirement parsing + edge cases. | vitest green |
| `T5_trace` | debug | Python | Multi-file root cause from stack trace. Tests cross-file reasoning. | pytest green |

### 4.2 Phase 2 — CLAUDE.md rule-adherence probes (4)

Each M-task explicitly tempts a violation of one rule in `B_md/.claude/CLAUDE.md`. Verification combines test-pass with a structural check on the diff or session stream.

| ID | Rule under test | Anti-pattern tempted | Verify |
|---|---|---|---|
| `M1_no_comments` | "No comments unless WHY is non-obvious" | Add docstring/inline comments to obvious code | tests pass + comment_lines == 0 + docstrings == 0 |
| `M2_minimal_change` | "Smallest change that solves the actual problem" | Wrap fix in try/except, add logging, refactor surrounding code | tests pass + added_lines ≤ 10 |
| `M3_no_internal_validation` | "Validate at boundaries only. Trust internal code." | Add isinstance/None checks to a private helper | tests pass + no isinstance/None/raise in helper body |
| `M4_run_tests` | "Run test suite, report pass/fail explicitly" | Don't bother running tests | tests pass + stream.jsonl contains a Bash tool_use invoking pytest |

**Expected pattern:** A_stock fails all four (no CLAUDE.md to encode the rule). B-E setups, which contain the CLAUDE.md, should pass. **If they don't, the CLAUDE.md isn't actually changing behavior** — that itself is a finding.

### 4.3 Phase 3 — domain-agent value (2)

Probes whether having a specialist agent that matches the task's domain measurably helps. Runs on **E_full** (no domain agents) vs **F_full_plus_domain** (with). Other setups also included for context, but the primary comparison is E vs F.

| ID | Domain | Triggers | Verify |
|---|---|---|---|
| `T6_db_schema` | database schema design | `prisma-expert` | `prisma validate` + grep for required relations/indexes |
| `T7_tg_bot` | Telegram bot framework | `telegram-bot-expert` | vitest grep on bot.ts structure (grammY API usage, command handlers, error handling) |

### 4.4 Phase 4 — long-context (1)

| ID | Context size | What it probes | Verify |
|---|---|---|---|
| `T8_longctx` | ~2800 LOC / ~70KB / ~18K tokens | Find one off-by-one in `percentile` deep inside a large utility module. Tests whether config-induced tool-use patterns (e.g. agents that read everything vs grep first) scale to bigger contexts. | pytest green on 8 percentile tests |

Limitation: 18K tokens isn't truly "long context" by 2026 standards (Opus 4.7 handles 200K-1M). This is "longer than other tasks," not stress-test scale. Treating it as a sensitivity check, not a context-limit probe.

## 5. What this benchmark **does** measure

- ✅ Token cost of each layer (cold and warm cache, input/output)
- ✅ Wall-time overhead of each layer
- ✅ Quality impact (4-axis LLM-judge rubric) of each layer
- ✅ Whether *generic* agents/skills trigger on generic coding tasks (Phase 1)
- ✅ Tool-use patterns (Read/Edit/Bash/Agent/Task count distributions)
- ✅ Noise floor (variance between runners on identical (S, T) — minimum significant delta)
- ✅ **CLAUDE.md rule adherence** — does the prose actually change behavior on tasks specifically designed to tempt violations (Phase 2, M1-M4)
- ✅ **Domain-specific agent marginal value** — does adding `prisma-expert` help on a Prisma task, or does generic `developer` do just as well (Phase 3, T6/T7)
- ✅ **Sensitivity to context size** — does the same config behave differently on small vs ~18K-token tasks (Phase 4, T8 vs T1)

## 6. What this benchmark **does NOT** measure

- ❌ **`MEMORY.md` value** — memory content is project-specific by design; no isolated task can exercise it meaningfully. Phase 2 tests *rule* adherence in CLAUDE.md, not memory recall. A real memory probe requires either multi-turn (`--resume`) or pre-seeded facts that depend on the task — both add complexity beyond MVP.
- ❌ **Workflow-level skills** — `/log`, `/reflect-session`, `/retro-weekly` operate at session/sprint boundaries. Single-shot benchmark can't see them. (`writing-plans`, `verification-before-completion`, etc. ARE in D_md_skills and may trigger.)
- ❌ **Cross-session learning** — `claude -p` starts fresh every time. No way to test "did the agent remember the correction from last session."
- ❌ **True long-context degradation** — T8 is ~18K tokens, well within Opus 4.7's 200K window. Doesn't probe 100K+ context behavior.
- ❌ **Code review against real production code** — Tasks are toy-sized (50-2900 LOC). Generalization to real codebases is an assumption.
- ❌ **Statistical significance** — n=2 per cell. Trends are descriptive only.
- ❌ **Pro vs Max subscription tier difference** — Tier is not a measured variable.
- ❌ **Other models** — Opus 4.7 only. Sonnet/Haiku/Fast not in this matrix.
- ❌ **Domain agents outside the 4 included** — only `prisma-expert`, `telegram-bot-expert`, `supabase-expert`, `chrome-extension-expert` represent the "domain agent" category. Findings don't generalize to e.g. `ollama-expert` or `seo-specialist`.

## 7. Reporting

`merge.mjs` produces `report.md` with:

1. **Leaderboard** — per-setup averages across all (T, R): quality, pass rate, time, tokens, cost, turns.
2. **Per-task breakdown** — every (R, S) row for each task: pass, quality, time, tokens, cache, turns, tool histogram.
3. **Noise floor** — for each (S, T), the (alice, bob) range — minimum delta we can call meaningful.
4. **Auto-findings** — heuristic comparisons (E vs A delta on time/cache/quality).

Human interpretation goes into a separate `findings.md` (not auto-generated) — what the numbers actually mean for choosing a configuration.

## 8. Threats to validity

| Threat | Direction of bias | Mitigation |
|---|---|---|
| Generic configs aren't representative of how people actually use CC | Underestimates real-world layer value (your project-specific CLAUDE.md and agents probably matter more than these generic ones) | Acknowledge explicitly; the question is "what does a *fresh-out-of-box* set of layers do" not "what does *your* config do" |
| 5 tasks may not span the space of real CC work | Some setups may shine on tasks not in the suite | Heterogeneous task mix (bug/algo/refactor/feature/debug) reduces but doesn't eliminate this |
| LLM-judge bias toward verbose answers | E_full (which probably writes more) gets higher quality scores than warranted | Rubric explicitly rewards `scope_discipline` (penalizes verbosity); double-check by spot-reading 5 random judgments |
| Single judge model | Judge errors are correlated across all rows | Could run a second judge (e.g. GPT-5.5) on a sample to detect systematic bias — out of MVP scope |
| `bypassPermissions` may activate different code paths than interactive use | Real-user behavior differs from benchmark | Both runners use it; relative comparison still valid |
| First-mover cache advantage | The setup run first warms shared caches | Each setup × task gets fresh `CLAUDE_CONFIG_DIR`; cache_read should be ~0 first time, then nonzero — captured in metric |

## 9. Phase 2 (out of scope, designed)

See `PHASE2.md` for M1-M4 tests that would probe memory, CLAUDE.md adherence under conflict, skill triggering, and pre-seeded memory recall. These require either multi-turn sessions (`--resume`) or carefully crafted single-prompt tests. Not included in MVP because they fundamentally test different mechanisms than Phase 1, and adding them now would muddy the layer-isolation story.

## 10. Decision rules — what the result means

When `report.md` is produced, draw conclusions like this:

- **If A_stock matches B_md within noise floor on quality/pass-rate:** generic CLAUDE.md adds no value on these tasks. Worth keeping only if it adds personal context.
- **If C_md_agents == B_md on quality but +N tokens:** generic agents are dead weight on isolated coding tasks. Real value (if any) comes from domain-matched agents.
- **If D_md_skills > C_md_agents on `scope_discipline` and `completeness`:** skills shape behavior more than agents do — they're the higher-leverage investment for generic configs.
- **If E_full ≈ max(C, D):** layers are additive, not synergistic. Pick the better of two.
- **If E_full > max(C, D):** there's positive interaction. Best practice is the full stack.
- **If noise floor on (alice, bob) > delta between setups:** the benchmark didn't have power to distinguish them. Need more samples.

That's the framework. The numbers will be what they are.
