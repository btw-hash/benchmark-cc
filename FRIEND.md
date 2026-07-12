# Instructions — second runner

You got a zip file (`benchmark-cc-friend.zip`). Here's what to do.

## Prereqs

- Windows + PowerShell 7+
- Claude Code `>= 2.1.119` (`claude --version`)
- Node.js 20+
- You've run `claude /login` so your subscription auth is set up

## 1. Unzip

Extract `benchmark-cc-friend.zip` anywhere (e.g. `C:\benchmark-cc\`). Open VS Code in that folder, or any PowerShell terminal in it.

## 2. Verify prereqs

```powershell
./setup.ps1
```

Should print version checks and "Ready". If it fails — fix what it complains about.

## 3. Add your personal Claude Code setup to the comparison

```powershell
./bootstrap-personal.ps1 -Runner <yourname>
```

Replace `<yourname>` with a short identifier (lowercase, e.g. `bob`). This copies your `~/.claude/` into a local-only folder so the benchmark can run **against your real config**. The folder is gitignored / not pushed anywhere — it stays on your machine. The script scans for secrets and warns if any are found.

See `PERSONAL.md` for what gets copied and what doesn't.

## 4. Run the benchmark

```powershell
node runner.mjs --runner <yourname> --samples 5
```

This runs **5 setups × 13 tasks × 5 samples ≈ 335 runs** on your machine (plus your personal slot = ~400). On Max 20× ≈ 15-20 hours elapsed. On Max 5× ≈ 2-3 days with rate-limit pauses. On Pro tier — drop `--samples 5` (use `--samples 1`) or this will take a week.

Pipeline auto-resumes if you Ctrl+C or it hits rate limit. Existing rows in `results/runs_<yourname>.jsonl` are skipped on re-run.

## 5. Package your results

```powershell
./package-my-results.ps1 -Runner <yourname>
```

Produces `../benchmark-results-<yourname>.zip` (in the parent folder). Send this file back to whoever gave you the benchmark zip — Telegram / email / Google Drive / whatever.

The zip contains:
- `results/runs_<yourname>.jsonl` — the numbers (tokens, time, pass/fail)
- `runs/<yourname>/` — diffs + stream transcripts (for the LLM judge to read)

It does **NOT** contain your personal Claude Code config or credentials.

## Troubleshooting

- `Not logged in · Please run /login` — your auth wasn't picked up. Run `claude` interactively once, then re-run `runner.mjs`.
- Run hangs mid-task — Ctrl+C, re-run. Existing rows are skipped.
- A specific (setup, task) consistently fails — that's a finding, not a bug. Leave it.
- You realise mid-run you want to stop — Ctrl+C. Your partial `results/runs_<yourname>.jsonl` is still valid. Just package and send what you have.

## Privacy summary

- Your `~/.claude/.credentials.json` — never leaves your machine.
- Your `~/.claude/` config (CLAUDE.md, agents, skills, memory) — copied into `setups/G_<yourname>_personal/`, **stays local** unless you explicitly opt to share.
- What you DO send back: only result numbers + the code diffs the agent produced. No personal config.
