# Personal setup slots

This benchmark compares generic baseline configs (A_stock → F_full_plus_domain) against **your own personal Claude Code setup**. The personal slot is the headline comparison — generic configs are reference points.

## How it works

- `setups/G_<runner>_personal/.claude/` — one slot per runner. Each owns their own. **Gitignored by default.**
- `./bootstrap-personal.ps1 -Runner <name>` copies your `~/.claude` into the slot, strips runtime state, scans for secrets, and leaves it local-only.
- `node runner.mjs --runner <name>` auto-includes any `G_*_personal/` slot present in `setups/`.

## Privacy modes

### Mode 1 — local-only (default)

```powershell
./bootstrap-personal.ps1 -Runner alice
node runner.mjs --runner alice --samples 5
```

Your personal config is on **your machine only**. `git push` excludes it. Results (`results/runs_alice.jsonl`, `runs/alice/...`) **do** get pushed and show how your config performed — but the config itself stays private.

Bob can't run **against** your config in this mode (he doesn't have it), but he can still see your numbers.

### Mode 2 — shared (opt-in)

```powershell
./bootstrap-personal.ps1 -Runner alice -Commit
```

Scans for secrets, prompts you to confirm, then `git add -f` + commit. After `git push`, Bob can pull your setup and run against it on his machine. This gives both of you n=10 samples per `(G_alice, task)` cell instead of n=5.

**Use this only if** your CLAUDE.md / memory doesn't contain anything sensitive. The script blocks if it finds known secret patterns (API keys, OAuth tokens, GitHub tokens) but doesn't catch every kind of sensitive content. Review the diff before committing.

## What gets copied by bootstrap

| Path | Included | Why |
|---|---|---|
| `~/.claude/CLAUDE.md` | ✅ | The prose layer |
| `~/.claude/settings.json` | ✅ | Hooks, permissions |
| `~/.claude/agents/` | ✅ | Your subagent collection |
| `~/.claude/skills/` | ✅ | Your skill collection |
| `~/.claude/hooks/` | ✅ | Your hook scripts |
| `~/.claude/projects/**/memory/*.md` | ✅ | Memory files |
| `~/.claude/projects/**/*.jsonl` | ❌ | Session transcripts (sensitive, irrelevant to benchmark) |
| `~/.claude/.credentials.json` | ❌ | Bootstrapped separately, gitignored, never in G_*/ |
| `~/.claude/sessions/`, `file-history/`, `backups/` | ❌ | CC runtime state |

## Headline comparisons

After both runners (alice + bob) prog through their G slots:

| Comparison | Tells you |
|---|---|
| `A_stock` vs `G_alice` | What does your entire personal stack add over zero config? |
| `E_full` (generic best-practice) vs `G_alice` | Is your personalization beating a public best-practice setup? |
| `G_alice` vs `G_bob` | Whose setup wins on these tasks? |
| `G_alice` on M-tests | Are *your* CLAUDE.md rules followed by Opus, or ignored? |
| `G_alice` on M5_multiturn_memory | Does your memory dir actually get loaded and used? |

The first one (`A vs G`) is the ROI on having any setup at all. The third (`G_alice vs G_bob`) is the bragging-rights question.

## Limitations

- **Cross-machine portability:** If `G_alice/` references absolute paths like `c:/AI/scripts/...` in hooks, those hooks **will silently fail** on Bob's machine. This counts as a portability finding — your setup is or isn't portable, and the benchmark reveals it.
- **Memory project specificity:** If your MEMORY.md is full of `feedback_courseai_*` and `project_my_assistant_*`, none of it will help on isolated benchmark tasks. That's expected — Phase 2 M-tests probe CLAUDE.md adherence, not memory recall. The exception is `M5_multiturn_memory` which probes cross-turn retention regardless of memory file content.
- **Secret scanning is regex-based.** It catches obvious key patterns. It does NOT catch: hardcoded business names, employer names, private project codenames, personal email addresses. Review before sharing.
