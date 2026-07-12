# benchmark-cc — report

Runners: alice | Setups: 7 | Tasks: 13 | Total runs: 390

## Setup compositions

What is actually inside each setup — to interpret quality/cost deltas in context.

| Setup | CLAUDE.md (lines) | Agents (count) | Skills (count) | Hooks | Total size (KB) | Source |
|---|---|---|---|---|---|---|
| A_stock | — | 0 | 0 | 0 | 3096 | empty baseline |
| B_md | 28 | 0 | 0 | 0 | 3153 | generic 30-line CLAUDE.md (original) |
| C_md_agents | 28 | 10 | 0 | 0 | 3060 | agents from github.com/affaan-m/everything-claude-code (MIT) |
| D_md_skills | 28 | 0 | 14 | 0 | 3511 | skills from github.com/obra/superpowers (MIT) |
| E_full | 28 | 10 | 14 | 1 | 3578 | B + C + D + secrets-scan hook |
| F_full_plus_domain | 28 | 14 | 14 | 1 | 830 | E + 4 domain experts (prisma/telegram/supabase/chrome-ext) |
| G_alice_personal | 66 | 38 | 46 | 2 | 3509 | personal config (runner-owned, gitignored) |

### Agent / skill rosters

**C_md_agents**
- agents (10): architect, build-error-resolver, code-architect, code-explorer, code-reviewer, code-simplifier, comment-analyzer, doc-updater, e2e-runner, harness-optimizer

**D_md_skills**
- skills (14): brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills

**E_full**
- agents (10): architect, build-error-resolver, code-architect, code-explorer, code-reviewer, code-simplifier, comment-analyzer, doc-updater, e2e-runner, harness-optimizer
- skills (14): brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills

**F_full_plus_domain**
- agents (14): architect, build-error-resolver, chrome-extension-expert, code-architect, code-explorer, code-reviewer, code-simplifier, comment-analyzer, doc-updater, e2e-runner, harness-optimizer, prisma-expert, supabase-expert, telegram-bot-expert
- skills (14): brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills

**G_alice_personal**
- agents (38): 3d-scene-designer, accessibility-tester, api-tester, architect, boss, brand-identity-designer, business-analyst, carousel-growth-engine, chrome-extension-expert, code-reviewer, content-creator, debugger, dependency-manager, developer, devops-automator, git-workflow-manager, image-prompt-engineer, instagram-curator, motion-designer, n8n-editor, ollama-expert, performance-engineer, prisma-expert, product-manager, prompt-engineer, qa-engineer, refactoring-specialist, reviewer, security-engineer, seo-specialist, supabase-expert, technical-writer, telegram-bot-expert, test-engineer, tester, ux-designer, visual-storyteller, worker
- skills (46): accessibility-audit, agent-route, antigravity, audit, backup-memory, brainstorming, bundle-analyze, check-types, db-migrate, deploy, deps-audit, dispatching-parallel-agents, env-check, executing-plans, finishing-a-development-branch, frontend-design, git-pr, haikufy, improve-claude-md, lighthouse, log, new-project, notion-sync, obsidian-check, onboard, prune-memory, receiving-code-review, refactor, reflect-session, requesting-code-review, retro-weekly, security-scan, sprint-report, standup, subagent-driven-development, systematic-debugging, telegram-publish, test-all, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, waterfall, writing-plans, writing-skills, yt-transcript

## Leaderboard (by setup)

| Setup | Avg quality (/10) | Pass rate | Avg time (s) | Avg input | Avg output | Avg cache_r | Avg cache_w | Avg cost ($) | Avg turns |
|---|---|---|---|---|---|---|---|---|---|
| A_stock | 9.44 | 60/65 | 54.3 | 10 | 2138 | 204857 | 15699 | 0.25 | 6.4 |
| B_md | 9.53 | 60/65 | 51.0 | 10 | 2005 | 208133 | 16272 | 0.26 | 6.3 |
| C_md_agents | 9.49 | 60/65 | 53.5 | 11 | 1897 | 227281 | 16806 | 0.27 | 6.7 |
| D_md_skills | 9.52 | 60/65 | 51.6 | 10 | 2015 | 206063 | 17515 | 0.26 | 6.5 |
| E_full | 9.45 | 60/65 | 51.4 | 11 | 1973 | 222513 | 16860 | 0.27 | 6.6 |
| F_full_plus_domain | 9.32 | 5/10 | 52.9 | 12 | 1724 | 281787 | 18568 | 0.30 | 7.9 |
| G_alice_personal | 9.50 | 55/55 | 62.8 | 10 | 1894 | 236450 | 21528 | 0.30 | 6.3 |

## Per-task results

### M1_no_comments

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.8 | 29.4 | 10/846 | 195190/13606 | $0.20 | 6 | B2R2W1 |
| alice | A_stock | ✓ | 9.5 | 29.1 | 10/729 | 195117/13523 | $0.20 | 6 | B2R2W1 |
| alice | A_stock | ✓ | 9.5 | 31.6 | 10/1086 | 195930/13844 | $0.21 | 6 | B2R2W1 |
| alice | A_stock | ✓ | 9.5 | 28.1 | 10/749 | 195113/13527 | $0.20 | 6 | B2R2W1 |
| alice | A_stock | ✓ | 9.5 | 25.1 | 10/783 | 195119/13533 | $0.20 | 6 | B2R2W1 |
| alice | B_md | ✓ | 9.5 | 32.8 | 10/887 | 198180/14243 | $0.21 | 6 | B2R2W1 |
| alice | B_md | ✓ | 9.5 | 28.2 | 10/976 | 198299/14323 | $0.21 | 6 | B2R2W1 |
| alice | B_md | ✓ | 9.5 | 30.2 | 10/938 | 198222/14300 | $0.21 | 6 | B2R2W1 |
| alice | B_md | ✓ | 9.5 | 27.9 | 10/1046 | 198383/14407 | $0.22 | 6 | B2R2W1 |
| alice | B_md | ✓ | 9.8 | 29.9 | 11/1157 | 234379/14591 | $0.24 | 7 | B2G1R2W1 |
| alice | C_md_agents | ✓ | 9.5 | 29.9 | 10/1197 | 180167/37590 | $0.36 | 6 | B2R2W1 |
| alice | C_md_agents | ✓ | 9.5 | 35.7 | 10/827 | 202877/14066 | $0.21 | 6 | B2R2W1 |
| alice | C_md_agents | ✓ | 9.5 | 28.7 | 10/866 | 202917/14111 | $0.21 | 6 | B2R2W1 |
| alice | C_md_agents | ✓ | 9.8 | 30.6 | 10/946 | 203051/14182 | $0.21 | 6 | B2R2W1 |
| alice | C_md_agents | ✓ | 9.5 | 29.2 | 10/962 | 203017/14213 | $0.22 | 6 | B2R2W1 |
| alice | D_md_skills | ✓ | 9.5 | 26.8 | 10/833 | 200931/14707 | $0.21 | 6 | B2R2W1 |
| alice | D_md_skills | ✓ | 9.8 | 28.8 | 10/1044 | 201503/14971 | $0.22 | 6 | B2R2W1 |
| alice | D_md_skills | ✓ | 9.5 | 31.6 | 10/876 | 201131/14789 | $0.22 | 6 | B2R2W1 |
| alice | D_md_skills | ✓ | 9.8 | 31.4 | 10/870 | 200888/14789 | $0.22 | 6 | B2R2W1 |
| alice | D_md_skills | ✓ | 9.5 | 25.4 | 10/810 | 200923/14695 | $0.21 | 6 | B2R2W1 |
| alice | E_full | ✓ | 9.5 | 34.7 | 10/1742 | 206946/15588 | $0.25 | 6 | B2R2W1 |
| alice | E_full | ✓ | 9.5 | 28.1 | 10/981 | 206561/14866 | $0.22 | 6 | B2R2W1 |
| alice | E_full | ✓ | 9.5 | 30.7 | 10/1100 | 206871/14997 | $0.23 | 6 | B2R2W1 |
| alice | E_full | ✓ | 9.5 | 28.3 | 10/1016 | 206401/14910 | $0.22 | 6 | B2R2W1 |
| alice | E_full | ✓ | 9.5 | 40.7 | 10/1255 | 206632/15142 | $0.23 | 6 | B2R2W1 |
| alice | G_alice_personal | ✓ | 9.5 | 38.1 | 10/998 | 215565/44259 | $0.41 | 6 | B2R2W1 |
| alice | G_alice_personal | ✓ | 9.8 | 32.5 | 10/805 | 240978/17741 | $0.25 | 6 | B2R2W1 |
| alice | G_alice_personal | ✓ | 9.5 | 35.3 | 10/858 | 240898/17795 | $0.25 | 6 | B2R2W1 |
| alice | G_alice_personal | ✓ | 9.5 | 30.4 | 10/728 | 240742/17677 | $0.25 | 6 | B2R2W1 |
| alice | G_alice_personal | ✓ | 9.5 | 38.7 | 10/1354 | 241363/18289 | $0.27 | 6 | B2R2W1 |

### M2_minimal_change

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.8 | 27.9 | 10/954 | 197154/14150 | $0.21 | 6 | B2R2E1 |
| alice | A_stock | ✓ | 9.8 | 26.5 | 10/884 | 197101/14085 | $0.21 | 6 | B2R2E1 |
| alice | A_stock | ✓ | 9.8 | 34.2 | 10/893 | 196433/13896 | $0.21 | 6 | B2G1R1E1 |
| alice | A_stock | ✓ | 9.8 | 29.5 | 10/981 | 197185/14180 | $0.21 | 6 | B2R2E1 |
| alice | A_stock | ✓ | 9.8 | 26.6 | 10/840 | 196332/13840 | $0.21 | 6 | B2G1R1E1 |
| alice | B_md | ✓ | 9.8 | 26.1 | 10/990 | 198232/14329 | $0.21 | 6 | B2R2E1 |
| alice | B_md | ✓ | 9.8 | 30.2 | 10/884 | 199291/14455 | $0.21 | 6 | B2G1R1E1 |
| alice | B_md | ✓ | 9.8 | 31.4 | 11/973 | 234831/14750 | $0.23 | 7 | B3R2E1 |
| alice | B_md | ✓ | 9.8 | 28.4 | 10/870 | 199985/14663 | $0.21 | 6 | B2R2E1 |
| alice | B_md | ✓ | 9.5 | 29.4 | 10/849 | 199933/14633 | $0.21 | 6 | B2R2E1 |
| alice | C_md_agents | ✓ | 9.8 | 26.7 | 10/912 | 204144/14385 | $0.22 | 6 | B2G1R1E1 |
| alice | C_md_agents | ✓ | 9.8 | 26.8 | 10/888 | 204773/14560 | $0.22 | 6 | B2R2E1 |
| alice | C_md_agents | ✓ | 9.8 | 30.7 | 10/900 | 203670/14375 | $0.21 | 6 | B3R1E1 |
| alice | C_md_agents | ✓ | 9.5 | 28.1 | 10/969 | 204854/14644 | $0.22 | 6 | B2R2E1 |
| alice | C_md_agents | ✓ | 9.8 | 29.6 | 10/996 | 204894/14663 | $0.22 | 6 | B2R2E1 |
| alice | D_md_skills | ✓ | 9.5 | 34.4 | 10/1269 | 203891/15612 | $0.23 | 6 | B2R2E1 |
| alice | D_md_skills | ✓ | 9.5 | 26.8 | 10/901 | 202032/15013 | $0.22 | 6 | B2G1R1E1 |
| alice | D_md_skills | ✓ | 9.8 | 26.8 | 10/876 | 202750/15212 | $0.22 | 6 | B2R2E1 |
| alice | D_md_skills | ✓ | 9.8 | 33.5 | 10/955 | 201637/15074 | $0.22 | 6 | B3R1E1 |
| alice | D_md_skills | ✓ | 9.8 | 31.8 | 11/1060 | 238332/15433 | $0.24 | 7 | B3R2E1 |
| alice | E_full | ✓ | 9.5 | 33.7 | 10/958 | 208193/15287 | $0.22 | 6 | B2R2E1 |
| alice | E_full | ✓ | 9.8 | 31.5 | 10/989 | 208232/15321 | $0.23 | 6 | B2R2E1 |
| alice | E_full | ✓ | 9.5 | 31.3 | 10/994 | 208233/15320 | $0.23 | 6 | B2R2E1 |
| alice | E_full | ✓ | 9.8 | 41.3 | 10/981 | 208192/15272 | $0.22 | 6 | B2R2E1 |
| alice | E_full | ✓ | 9.8 | 28.8 | 10/951 | 208193/15282 | $0.22 | 6 | B2R2E1 |
| alice | G_alice_personal | ✓ | 9.8 | 38.1 | 10/901 | 242898/18528 | $0.26 | 6 | B2R2E1 |
| alice | G_alice_personal | ✓ | 9.8 | 41.0 | 10/1020 | 241841/18368 | $0.26 | 6 | B3R1E1 |
| alice | G_alice_personal | ✓ | 9.8 | 38.5 | 9/816 | 198645/18196 | $0.23 | 5 | B2R1E1 |
| alice | G_alice_personal | ✓ | 9.5 | 40.2 | 10/959 | 241766/18320 | $0.26 | 6 | B3R1E1 |
| alice | G_alice_personal | ✓ | 9.8 | 42.9 | 10/1032 | 242424/18439 | $0.26 | 6 | B2G1R1E1 |

### M3_no_internal_validation

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.8 | 34.3 | 9/879 | 160418/13560 | $0.19 | 6 | B2R2E1 |
| alice | A_stock | ✓ | 9.0 | 32.0 | 10/877 | 194981/13525 | $0.20 | 6 | B2R2E1 |
| alice | A_stock | ✓ | 9.0 | 31.8 | 10/877 | 194973/13523 | $0.20 | 6 | B2R2E1 |
| alice | A_stock | ✓ | 9.0 | 31.4 | 10/873 | 194957/13519 | $0.20 | 6 | B2R2E1 |
| alice | A_stock | ✓ | 9.0 | 25.4 | 9/636 | 160078/13261 | $0.18 | 5 | R2E1B1 |
| alice | B_md | ✓ | 9.0 | 31.3 | 10/865 | 197876/14099 | $0.21 | 6 | B2R2E1 |
| alice | B_md | ✓ | 9.8 | 21.2 | 8/490 | 126659/13531 | $0.16 | 4 | R1E1B1 |
| alice | B_md | ✓ | 9.0 | 24.2 | 9/786 | 162544/13997 | $0.19 | 5 | R2E1B1 |
| alice | B_md | ✓ | 9.8 | 24.2 | 9/796 | 162614/14007 | $0.19 | 5 | R2E1B1 |
| alice | B_md | ✓ | 9.0 | 30.0 | 10/872 | 197904/14106 | $0.21 | 6 | B2R2E1 |
| alice | C_md_agents | ✓ | 9.0 | 25.4 | 9/803 | 166585/13891 | $0.19 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 9.3 | 30.0 | 10/886 | 202692/13994 | $0.21 | 6 | B2R2E1 |
| alice | C_md_agents | ✓ | 9.0 | 39.6 | 9/768 | 166109/13724 | $0.19 | 5 | B2R1E1 |
| alice | C_md_agents | ✓ | 9.0 | 32.2 | 10/882 | 202692/13994 | $0.21 | 6 | B2R2E1 |
| alice | C_md_agents | ✓ | 9.0 | 28.4 | 10/876 | 202676/13989 | $0.21 | 6 | B2R2E1 |
| alice | D_md_skills | ✓ | 9.0 | 22.0 | 8/598 | 128907/14397 | $0.17 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 9.8 | 25.6 | 9/824 | 164695/14583 | $0.19 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 9.0 | 21.5 | 8/522 | 128359/14123 | $0.17 | 4 | R1E1B1 |
| alice | D_md_skills | ✓ | 9.0 | 30.2 | 8/696 | 128517/14294 | $0.17 | 4 | R1E1B1 |
| alice | D_md_skills | ✓ | 9.0 | 23.1 | 8/604 | 128919/14403 | $0.17 | 5 | R2E1B1 |
| alice | E_full | ✓ | 9.0 | 23.4 | 9/629 | 169341/14511 | $0.19 | 5 | R2E1B1 |
| alice | E_full | ✓ | 9.0 | 28.0 | 9/859 | 169266/14601 | $0.20 | 5 | R2E1B1 |
| alice | E_full | ✓ | 9.0 | 28.4 | 10/884 | 206029/14653 | $0.22 | 6 | B2R2E1 |
| alice | E_full | ✓ | 9.0 | 24.9 | 9/829 | 169308/14573 | $0.20 | 5 | R2E1B1 |
| alice | E_full | ✓ | 9.0 | 26.8 | 9/835 | 169290/14564 | $0.20 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.0 | 39.8 | 10/883 | 240739/17927 | $0.25 | 6 | B2R2E1 |
| alice | G_alice_personal | ✓ | 9.0 | 36.8 | 9/839 | 197590/17862 | $0.23 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.3 | 32.5 | 8/642 | 154546/17706 | $0.20 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.0 | 36.9 | 9/792 | 197608/17818 | $0.23 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.3 | 41.0 | 10/880 | 240743/17929 | $0.25 | 6 | B2R2E1 |

### M4_run_tests

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 10.0 | 25.0 | 8/564 | 125213/13083 | $0.16 | 5 | R2E1B1 |
| alice | A_stock | ✓ | 10.0 | 22.1 | 8/470 | 124699/12828 | $0.15 | 4 | R1E1B1 |
| alice | A_stock | ✓ | 10.0 | 23.4 | 8/569 | 125233/13095 | $0.16 | 5 | R2E1B1 |
| alice | A_stock | ✓ | 10.0 | 28.7 | 8/589 | 125239/13108 | $0.16 | 5 | R2E1B1 |
| alice | A_stock | ✓ | 10.0 | 25.7 | 8/560 | 125199/13078 | $0.16 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 23.6 | 8/571 | 126989/13676 | $0.16 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 22.7 | 8/594 | 127005/13699 | $0.16 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 26.4 | 8/570 | 126989/13675 | $0.16 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 24.2 | 9/594 | 162049/13658 | $0.18 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 24.7 | 9/612 | 162067/13685 | $0.18 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 25.5 | 8/601 | 130249/13587 | $0.17 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 21.8 | 8/572 | 130206/13555 | $0.16 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 21.6 | 8/571 | 130202/13553 | $0.16 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 22.9 | 8/591 | 130226/13573 | $0.17 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 24.5 | 8/584 | 130214/13564 | $0.17 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 10.0 | 22.9 | 8/624 | 128717/14275 | $0.17 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 10.0 | 28.5 | 8/713 | 128864/14371 | $0.17 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 10.0 | 27.8 | 8/596 | 128645/14247 | $0.17 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 10.0 | 22.5 | 8/618 | 128698/14278 | $0.17 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 10.0 | 27.9 | 8/836 | 129103/14494 | $0.18 | 5 | R2E1B1 |
| alice | E_full | ✓ | 10.0 | 24.6 | 8/572 | 132172/14200 | $0.17 | 5 | R2E1B1 |
| alice | E_full | ✓ | 10.0 | 23.8 | 8/604 | 132230/14248 | $0.17 | 5 | R2E1B1 |
| alice | E_full | ✓ | 10.0 | 23.8 | 8/603 | 132223/14240 | $0.17 | 5 | R2E1B1 |
| alice | E_full | ✓ | 10.0 | 22.7 | 8/595 | 132223/14238 | $0.17 | 5 | R2E1B1 |
| alice | E_full | ✓ | 10.0 | 24.6 | 8/595 | 132215/14232 | $0.17 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 10.0 | 28.8 | 8/565 | 154260/17486 | $0.20 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 10.0 | 31.3 | 8/592 | 154281/17508 | $0.20 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 10.0 | 29.9 | 8/577 | 154300/17511 | $0.20 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 10.0 | 33.3 | 8/587 | 154283/17509 | $0.20 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 10.0 | 28.6 | 8/582 | 154282/17510 | $0.20 | 5 | R2E1B1 |

### M5_multiturn_memory

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 10.0 | 81.2 | 14/4236 | 202654/16610 | $0.31 | 6 | W2B1R1 |
| alice | A_stock | ✓ | 10.0 | 99.3 | 13/5981 | 167603/18231 | $0.35 | 5 | W2R1 |
| alice | A_stock | ✓ | 10.0 | 73.7 | 13/4209 | 164897/16501 | $0.29 | 5 | W2R1 |
| alice | A_stock | ✓ | 10.0 | 98.1 | 16/5890 | 266278/32988 | $0.49 | 8 | W4R2 |
| alice | A_stock | ✓ | 10.0 | 71.6 | 15/3927 | 241232/16428 | $0.32 | 7 | W2B1G1R1 |
| alice | B_md | ✓ | 10.0 | 63.7 | 13/3589 | 165519/16481 | $0.28 | 5 | G1R1W1 |
| alice | B_md | ✓ | 10.0 | 72.6 | 14/4302 | 206014/17149 | $0.32 | 6 | W2B1R1 |
| alice | B_md | ✓ | 10.0 | 66.7 | 13/3646 | 165537/16457 | $0.28 | 5 | G1R1W1 |
| alice | B_md | ✓ | 10.0 | 65.6 | 13/3832 | 166413/16694 | $0.28 | 5 | G1R1W1 |
| alice | B_md | ✓ | 10.0 | 75.2 | 16/4467 | 285071/18041 | $0.37 | 8 | R2W2B1G1 |
| alice | C_md_agents | ✓ | 10.0 | 98.8 | 16/5910 | 282883/34705 | $0.51 | 9 | W4R2B1 |
| alice | C_md_agents | ✓ | 10.0 | 69.8 | 14/4242 | 206420/17651 | $0.32 | 6 | R2B1W1 |
| alice | C_md_agents | ✓ | 10.0 | 77.1 | 15/4557 | 250948/18125 | $0.35 | 7 | R2W2B1 |
| alice | C_md_agents | ✓ | 10.0 | 59.4 | 13/3135 | 169160/16024 | $0.26 | 5 | G1R1W1 |
| alice | C_md_agents | ✓ | 10.0 | 61.4 | 13/2758 | 167659/15614 | $0.25 | 5 | B1R1W1 |
| alice | D_md_skills | ✓ | 10.0 | 89.3 | 16/5238 | 271844/34854 | $0.49 | 8 | R2W4 |
| alice | D_md_skills | ✓ | 10.0 | 74.8 | 13/4145 | 166844/17410 | $0.30 | 5 | B1R1W1 |
| alice | D_md_skills | ✓ | 10.0 | 48.9 | 13/2205 | 165989/15732 | $0.24 | 5 | B1R1W1 |
| alice | D_md_skills | ✓ | 10.0 | 82.3 | 16/5070 | 288313/19271 | $0.39 | 8 | R2W3B1 |
| alice | D_md_skills | ✓ | 10.0 | 73.7 | 13/3147 | 167824/16701 | $0.27 | 5 | G1R1W1 |
| alice | E_full | ✓ | 10.0 | 110.0 | 16/6035 | 286206/36059 | $0.52 | 9 | W4R2B1 |
| alice | E_full | ✓ | 10.0 | 63.3 | 13/3099 | 170369/16642 | $0.27 | 5 | B1R1W1 |
| alice | E_full | ✓ | 10.0 | 76.5 | 15/4516 | 255679/18863 | $0.36 | 7 | R2W2B1 |
| alice | E_full | ✓ | 10.0 | 72.2 | 13/3873 | 173424/17371 | $0.29 | 5 | G1R1W1 |
| alice | E_full | ✓ | 10.0 | 59.6 | 14/2951 | 210531/16428 | $0.28 | 6 | W2B1R1 |
| alice | G_alice_personal | ✓ | 10.0 | 72.3 | 13/2079 | 197873/18963 | $0.27 | 5 | B1R1W1 |
| alice | G_alice_personal | ✓ | 10.0 | 103.4 | 14/5190 | 251067/22044 | $0.39 | 6 | W2G1R1 |
| alice | G_alice_personal | ✓ | 10.0 | 71.4 | 14/3076 | 245089/20032 | $0.32 | 6 | W2B1R1 |
| alice | G_alice_personal | ✓ | 10.0 | 64.1 | 13/2305 | 198395/19166 | $0.28 | 5 | G1R1W1 |
| alice | G_alice_personal | ✓ | 10.0 | 88.9 | 15/3551 | 290444/20641 | $0.36 | 7 | W2B1G1R1 |

### T1_bug

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.8 | 30.1 | 9/865 | 162861/14616 | $0.20 | 5 | R1B2E1 |
| alice | A_stock | ✓ | 9.8 | 24.3 | 9/768 | 161326/13818 | $0.19 | 5 | R2E1B1 |
| alice | A_stock | ✓ | 9.8 | 23.5 | 8/712 | 126545/13799 | $0.17 | 5 | R2E1B1 |
| alice | A_stock | ✓ | 9.8 | 24.5 | 8/647 | 126475/13733 | $0.17 | 5 | R2E1B1 |
| alice | A_stock | ✓ | 10.0 | 25.3 | 9/781 | 161353/14061 | $0.19 | 5 | R2E1B1 |
| alice | B_md | ✓ | 9.8 | 28.9 | 9/784 | 163402/14422 | $0.19 | 5 | R2E1B1 |
| alice | B_md | ✓ | 9.8 | 30.4 | 9/748 | 163145/14510 | $0.19 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 25.5 | 9/715 | 163116/14221 | $0.19 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 25.7 | 9/742 | 163148/14239 | $0.19 | 5 | R2E1B1 |
| alice | B_md | ✓ | 10.0 | 26.8 | 9/905 | 163323/14651 | $0.20 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 9.8 | 23.3 | 8/729 | 131499/14268 | $0.17 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 27.2 | 9/758 | 167708/14269 | $0.19 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 24.8 | 8/695 | 131522/14248 | $0.17 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 33.7 | 9/806 | 167761/14322 | $0.19 | 5 | R2E1B1 |
| alice | C_md_agents | ✓ | 10.0 | 32.5 | 9/774 | 167714/14280 | $0.19 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 10.0 | 27.6 | 8/794 | 130094/15014 | $0.18 | 5 | R2E1B1 |
| alice | D_md_skills | ✓ | 9.8 | 33.7 | 8/1343 | 132913/16571 | $0.20 | 6 | R2B2E1 |
| alice | D_md_skills | ✓ | 9.8 | 27.7 | 8/855 | 132212/16091 | $0.19 | 6 | R2B2E1 |
| alice | D_md_skills | ✓ | 10.0 | 32.4 | 8/984 | 132425/16205 | $0.19 | 6 | R2B2E1 |
| alice | D_md_skills | ✓ | 9.8 | 26.3 | 8/920 | 130368/15139 | $0.18 | 5 | R2E1B1 |
| alice | E_full | ✓ | 10.0 | 28.5 | 8/887 | 133874/15090 | $0.18 | 5 | R2E1B1 |
| alice | E_full | ✓ | 9.8 | 27.0 | 8/817 | 135724/16021 | $0.19 | 6 | R2B2E1 |
| alice | E_full | ✓ | 9.8 | 28.0 | 8/906 | 133939/15120 | $0.18 | 5 | R2E1B1 |
| alice | E_full | ✓ | 10.0 | 37.5 | 8/1095 | 135990/16295 | $0.20 | 6 | R2B2E1 |
| alice | E_full | ✓ | 9.8 | 26.0 | 9/781 | 170360/14955 | $0.20 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.8 | 36.3 | 9/756 | 198197/18064 | $0.23 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.8 | 38.9 | 9/767 | 199645/18781 | $0.24 | 5 | R1B2E1 |
| alice | G_alice_personal | ✓ | 9.8 | 43.1 | 9/745 | 198205/18058 | $0.23 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.8 | 34.3 | 8/689 | 155137/18022 | $0.21 | 5 | R2E1B1 |
| alice | G_alice_personal | ✓ | 9.8 | 35.2 | 8/845 | 157410/19195 | $0.22 | 6 | R2B2E1 |

### T2_lru

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.5 | 58.2 | 11/1356 | 235082/15175 | $0.25 | 7 | B3R2W1 |
| alice | A_stock | ✓ | 9.5 | 48.6 | 11/1293 | 235062/15144 | $0.25 | 7 | B3R2W1 |
| alice | A_stock | ✓ | 9.3 | 56.4 | 11/1323 | 235072/15149 | $0.25 | 7 | B3R2W1 |
| alice | A_stock | ✓ | 9.5 | 54.1 | 11/1340 | 235075/15147 | $0.25 | 7 | B3R2W1 |
| alice | A_stock | ✓ | 9.5 | 49.9 | 11/1323 | 235095/15141 | $0.25 | 7 | B3R2W1 |
| alice | B_md | ✓ | 9.3 | 56.9 | 11/1319 | 237711/15582 | $0.25 | 7 | B3R2W1 |
| alice | B_md | ✓ | 9.5 | 47.7 | 10/1278 | 202126/15491 | $0.23 | 6 | R2W1B2 |
| alice | B_md | ✓ | 9.5 | 45.4 | 11/1382 | 215800/37962 | $0.38 | 7 | B3R2W1 |
| alice | B_md | ✓ | 9.5 | 36.8 | 10/1394 | 202637/15653 | $0.23 | 6 | R2E1B2 |
| alice | B_md | ✓ | 9.5 | 39.4 | 12/1458 | 275183/15865 | $0.27 | 8 | B3R3W1 |
| alice | C_md_agents | ✓ | 9.5 | 40.5 | 12/1493 | 259428/39104 | $0.41 | 8 | B3R3W1 |
| alice | C_md_agents | ✓ | 9.8 | 44.6 | 11/1296 | 244385/15619 | $0.25 | 7 | B3R2W1 |
| alice | C_md_agents | ✓ | 9.5 | 52.3 | 13/1633 | 322073/16169 | $0.30 | 9 | R3B3G1W1 |
| alice | C_md_agents | ✓ | 9.5 | 59.0 | 11/1310 | 244437/15634 | $0.25 | 7 | B3R2W1 |
| alice | C_md_agents | ✓ | 9.5 | 49.3 | 10/1411 | 208041/15656 | $0.24 | 6 | R2W1B2 |
| alice | D_md_skills | ✓ | 9.3 | 47.5 | 9/1146 | 169611/16113 | $0.21 | 6 | R2W1B2 |
| alice | D_md_skills | ✓ | 9.5 | 47.6 | 9/1474 | 170416/16484 | $0.23 | 6 | R2W1B2 |
| alice | D_md_skills | ✓ | 9.5 | 42.9 | 9/1168 | 167843/16099 | $0.21 | 5 | R2W1B1 |
| alice | D_md_skills | ✓ | 9.5 | 55.4 | 10/1393 | 206072/16365 | $0.24 | 6 | R2E1B2 |
| alice | D_md_skills | ✓ | 9.3 | 45.7 | 10/1357 | 205990/16315 | $0.24 | 6 | R2W1B2 |
| alice | E_full | ✓ | 9.5 | 47.0 | 11/1310 | 248376/16290 | $0.26 | 7 | B3R2W1 |
| alice | E_full | ✓ | 9.5 | 51.2 | 9/1500 | 175482/16629 | $0.23 | 7 | R3W1B2 |
| alice | E_full | ✓ | 9.5 | 44.4 | 10/1260 | 211122/16205 | $0.24 | 6 | R2W1B2 |
| alice | E_full | ✓ | 9.5 | 53.8 | 11/1416 | 250032/16497 | $0.26 | 7 | R3W1B2 |
| alice | E_full | ✓ | 9.5 | 48.3 | 11/1363 | 248354/16327 | $0.26 | 7 | B3R2W1 |
| alice | G_alice_personal | ✓ | 9.5 | 61.6 | 10/1290 | 218868/45387 | $0.43 | 6 | R2E1B2 |
| alice | G_alice_personal | ✓ | 9.5 | 70.0 | 9/1526 | 202472/19568 | $0.26 | 8 | R2B3G1W1 |
| alice | G_alice_personal | ✓ | 9.3 | 60.6 | 10/1371 | 245231/19176 | $0.28 | 6 | R2W1B2 |
| alice | G_alice_personal | ✓ | 9.5 | 75.8 | 11/1377 | 288288/19253 | $0.30 | 7 | B3R2W1 |
| alice | G_alice_personal | ✓ | 9.5 | 61.8 | 9/1350 | 202917/19315 | $0.26 | 7 | R3W1B2 |

### T3_refactor

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.8 | 29.1 | 8/1020 | 129682/15538 | $0.19 | 5 | R2W1B1 |
| alice | A_stock | ✓ | 9.8 | 40.3 | 9/1057 | 164831/15553 | $0.21 | 5 | R2W1B1 |
| alice | A_stock | ✓ | 9.8 | 30.9 | 8/999 | 129659/15486 | $0.19 | 5 | R2W1B1 |
| alice | A_stock | ✓ | 9.8 | 37.6 | 8/1035 | 129653/15522 | $0.19 | 5 | R2W1B1 |
| alice | A_stock | ✓ | 9.8 | 29.1 | 8/985 | 129628/15489 | $0.19 | 5 | R2W1B1 |
| alice | B_md | ✓ | 9.8 | 31.6 | 8/1099 | 131044/16006 | $0.19 | 5 | R2W1B1 |
| alice | B_md | ✓ | 9.8 | 36.0 | 8/1038 | 130990/15964 | $0.19 | 5 | R2W1B1 |
| alice | B_md | ✓ | 9.8 | 35.3 | 9/1238 | 166784/16137 | $0.22 | 5 | R2W1B1 |
| alice | B_md | ✓ | 9.8 | 33.3 | 10/1208 | 202209/16136 | $0.23 | 6 | B2R2W1 |
| alice | B_md | ✓ | 9.8 | 31.5 | 8/1114 | 131110/16042 | $0.19 | 5 | R2W1B1 |
| alice | C_md_agents | ✓ | 10.0 | 42.0 | 10/1279 | 207733/16202 | $0.24 | 6 | B2R2W1 |
| alice | C_md_agents | ✓ | 9.8 | 33.7 | 10/1197 | 207544/16126 | $0.24 | 6 | B2R2W1 |
| alice | C_md_agents | ✓ | 9.8 | 34.5 | 9/1263 | 171337/16140 | $0.22 | 5 | R2W1B1 |
| alice | C_md_agents | ✓ | 10.0 | 30.5 | 8/1145 | 134753/16077 | $0.20 | 5 | R2W1B1 |
| alice | C_md_agents | ✓ | 9.8 | 37.2 | 10/1214 | 207669/16128 | $0.24 | 6 | B2R2W1 |
| alice | D_md_skills | ✓ | 9.8 | 33.0 | 8/1094 | 133092/16691 | $0.20 | 5 | R2W1B1 |
| alice | D_md_skills | ✓ | 9.8 | 58.6 | 15/2196 | 258613/20307 | $0.31 | 8 | S1R2B2W1 |
| alice | D_md_skills | ✓ | 9.8 | 55.7 | 9/2027 | 174315/17993 | $0.25 | 6 | R2B2W1 |
| alice | D_md_skills | ✓ | 9.8 | 56.4 | 8/2491 | 135123/18048 | $0.24 | 5 | R2W1B1 |
| alice | D_md_skills | ✓ | 9.8 | 36.6 | 8/1323 | 133336/16925 | $0.21 | 5 | R2W1B1 |
| alice | E_full | ✓ | 9.8 | 30.0 | 8/1034 | 136641/16670 | $0.20 | 5 | R2W1B1 |
| alice | E_full | ✓ | 9.8 | 35.6 | 10/1158 | 210891/16732 | $0.24 | 6 | B2R2W1 |
| alice | E_full | ✓ | 9.8 | 35.7 | 9/1290 | 174069/16812 | $0.23 | 5 | R2W1B1 |
| alice | E_full | ✓ | 9.8 | 32.8 | 9/1234 | 173923/16754 | $0.22 | 5 | R2W1B1 |
| alice | E_full | ✓ | 9.8 | 37.5 | 9/1132 | 173858/16677 | $0.22 | 5 | R2W1B1 |
| alice | G_alice_personal | ✓ | 9.8 | 49.2 | 10/1207 | 244968/19735 | $0.28 | 6 | B2R2W1 |
| alice | G_alice_personal | ✓ | 9.8 | 47.7 | 8/1072 | 158680/19574 | $0.23 | 5 | R2W1B1 |
| alice | G_alice_personal | ✓ | 9.8 | 45.9 | 9/1242 | 201895/19794 | $0.26 | 7 | G2R2W1B1 |
| alice | G_alice_personal | ✓ | 10.0 | 69.7 | 10/1663 | 249420/20662 | $0.30 | 7 | B3R2W1 |
| alice | G_alice_personal | ✓ | 9.8 | 52.4 | 10/1231 | 245546/19834 | $0.28 | 6 | B2R2W1 |

### T4_crud

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.0 | 64.2 | 11/1384 | 236398/15461 | $0.25 | 7 | B3R2E1 |
| alice | A_stock | ✓ | 8.8 | 63.8 | 11/1295 | 236387/15420 | $0.25 | 7 | B3R2E1 |
| alice | A_stock | ✓ | 9.0 | 53.4 | 9/1418 | 166968/15736 | $0.22 | 7 | R3E1B2 |
| alice | A_stock | ✓ | 8.5 | 58.1 | 9/1833 | 167862/16138 | $0.23 | 7 | R3E1B2 |
| alice | A_stock | ✓ | 8.5 | 72.0 | 11/2150 | 237902/16242 | $0.27 | 7 | B3R2E1 |
| alice | B_md | ✓ | 8.8 | 49.7 | 9/1479 | 168820/16182 | $0.22 | 7 | R3E1B2 |
| alice | B_md | ✓ | 8.8 | 66.8 | 9/1629 | 169205/16276 | $0.23 | 7 | R3E1B2 |
| alice | B_md | ✓ | 9.0 | 70.3 | 10/1844 | 204452/16360 | $0.25 | 6 | R2E1B2 |
| alice | B_md | ✓ | 9.0 | 74.8 | 11/1448 | 239241/15972 | $0.26 | 7 | B3R2E1 |
| alice | B_md | ✓ | 9.0 | 63.8 | 10/1493 | 204134/16128 | $0.24 | 6 | R2E1B2 |
| alice | C_md_agents | ✓ | 8.8 | 64.3 | 11/1755 | 246171/16273 | $0.27 | 7 | B3R2E1 |
| alice | C_md_agents | ✓ | 9.0 | 61.2 | 11/1438 | 245576/15975 | $0.26 | 7 | B3R2E1 |
| alice | C_md_agents | ✓ | 9.0 | 73.6 | 11/1352 | 245441/15939 | $0.26 | 7 | B3R2E1 |
| alice | C_md_agents | ✓ | 8.5 | 65.1 | 11/1401 | 245549/15938 | $0.26 | 7 | B3R2E1 |
| alice | C_md_agents | ✓ | 8.8 | 59.4 | 9/1638 | 173720/16360 | $0.23 | 7 | R3E1B2 |
| alice | D_md_skills | ✓ | 9.0 | 73.4 | 8/1604 | 133474/16875 | $0.21 | 6 | R3E1B1 |
| alice | D_md_skills | ✓ | 8.8 | 66.5 | 9/1824 | 172610/17182 | $0.24 | 7 | R3E1B2 |
| alice | D_md_skills | ✓ | 9.5 | 70.9 | 10/1954 | 208576/17315 | $0.26 | 6 | R2E1B2 |
| alice | D_md_skills | ✓ | 8.8 | 70.3 | 8/1704 | 133886/17162 | $0.22 | 7 | R3E1B2 |
| alice | D_md_skills | ✓ | 8.8 | 68.2 | 9/1825 | 172465/17243 | $0.24 | 7 | R3E1B2 |
| alice | E_full | ✓ | 9.0 | 71.5 | 10/1930 | 213577/17280 | $0.26 | 6 | R2E1B2 |
| alice | E_full | ✓ | 8.8 | 71.7 | 10/1324 | 212499/16733 | $0.24 | 6 | R2E1B2 |
| alice | E_full | ✓ | 9.0 | 67.2 | 9/1466 | 175975/16847 | $0.23 | 7 | R3E1B2 |
| alice | E_full | ✓ | 8.8 | 71.8 | 12/1479 | 288812/16884 | $0.29 | 8 | B3R3E1 |
| alice | E_full | ✓ | 8.8 | 72.3 | 9/1432 | 175785/16880 | $0.23 | 7 | R3E1B2 |
| alice | G_alice_personal | ✓ | 8.8 | 101.2 | 9/1556 | 204222/20085 | $0.27 | 7 | R3E1B2 |
| alice | G_alice_personal | ✓ | 8.8 | 94.8 | 14/1654 | 204462/20302 | $0.27 | 7 | R3E1B2 |
| alice | G_alice_personal | ✓ | 8.5 | 95.6 | 9/1348 | 203825/19890 | $0.26 | 7 | R3E1B2 |
| alice | G_alice_personal | ✓ | 8.8 | 105.5 | 9/1664 | 204228/20173 | $0.27 | 7 | R3E1B2 |
| alice | G_alice_personal | ✓ | 9.0 | 94.4 | 16/1317 | 290118/19828 | $0.30 | 7 | B3R2E1 |

### T5_trace

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.0 | 135.1 | 13/7263 | 316816/21863 | $0.48 | 9 | B3R3E2 |
| alice | A_stock | ✓ | 9.0 | 306.2 | 12/22441 | 300204/36755 | $0.94 | 8 | B3R3E1 |
| alice | A_stock | ✓ | 8.3 | 149.1 | 13/8378 | 324491/16554 | $0.48 | 9 | B3R3E2 |
| alice | A_stock | ✓ | 8.5 | 133.5 | 13/7221 | 317107/21706 | $0.48 | 9 | B3R3E2 |
| alice | A_stock | ✓ | 8.8 | 156.4 | 13/8917 | 318734/23495 | $0.53 | 9 | B3R3E2 |
| alice | B_md | ✓ | 9.3 | 161.7 | 12/9888 | 290937/24598 | $0.55 | 8 | B3R3E1 |
| alice | B_md | ✓ | 8.8 | 184.8 | 12/12806 | 296962/27419 | $0.64 | 8 | B3R3E1 |
| alice | B_md | ✓ | 9.3 | 203.7 | 12/12564 | 288599/27366 | $0.63 | 8 | B3R3E1 |
| alice | B_md | ✓ | 9.3 | 122.8 | 13/6826 | 320088/21793 | $0.47 | 9 | B3R3E2 |
| alice | B_md | ✓ | 8.8 | 112.9 | 13/6011 | 318855/20996 | $0.44 | 9 | B3R3E2 |
| alice | C_md_agents | ✓ | 9.3 | 127.6 | 12/7091 | 290194/21788 | $0.46 | 8 | B3R3E1 |
| alice | C_md_agents | ✓ | 8.5 | 180.0 | 16/7958 | 461575/23839 | $0.58 | 12 | B5R4E2 |
| alice | C_md_agents | ✓ | 8.5 | 121.9 | 13/6782 | 333138/21615 | $0.47 | 9 | B4R3E1 |
| alice | C_md_agents | ✓ | 7.5 | 110.2 | 13/4975 | 325980/19900 | $0.41 | 9 | B3R3E2 |
| alice | C_md_agents | ✓ | 9.3 | 208.5 | 13/10578 | 344907/25547 | $0.60 | 9 | B4R3E1 |
| alice | D_md_skills | ✓ | 9.3 | 144.9 | 13/8600 | 340134/24014 | $0.54 | 9 | B4R3E1 |
| alice | D_md_skills | ✓ | 9.3 | 109.6 | 13/6087 | 324587/21729 | $0.45 | 9 | B3R3E2 |
| alice | D_md_skills | ✓ | 9.0 | 259.1 | 12/17366 | 303007/32896 | $0.79 | 8 | B3R3E1 |
| alice | D_md_skills | ✓ | 9.0 | 121.8 | 14/5302 | 362054/21045 | $0.45 | 10 | B3G1R3E2 |
| alice | D_md_skills | ✓ | 9.0 | 87.8 | 13/3817 | 322567/19414 | $0.38 | 9 | B3R3E2 |
| alice | E_full | ✓ | 9.3 | 153.1 | 12/9831 | 299024/25263 | $0.55 | 8 | B3R3E1 |
| alice | E_full | ✓ | 7.8 | 146.5 | 14/7566 | 379830/23545 | $0.53 | 10 | B3R4E2 |
| alice | E_full | ✓ | 8.8 | 93.8 | 13/3335 | 329236/19004 | $0.37 | 9 | B3R3E2 |
| alice | E_full | ✓ | 8.5 | 185.5 | 13/12265 | 351518/27791 | $0.66 | 9 | B4R3E1 |
| alice | E_full | ✓ | 8.5 | 157.3 | 14/8063 | 376080/23813 | $0.54 | 10 | B3G1R3E2 |
| alice | G_alice_personal | ✓ | 9.0 | 195.7 | 12/11263 | 320052/56035 | $0.79 | 8 | B3R3E1 |
| alice | G_alice_personal | ✓ | 9.3 | 232.3 | 14/13799 | 451530/32622 | $0.77 | 10 | B3R3E2A1 |
| alice | G_alice_personal | ✓ | 9.3 | 142.6 | 12/6435 | 341359/25014 | $0.49 | 8 | B3R3E1 |
| alice | G_alice_personal | ✓ | 9.0 | 124.2 | 13/4072 | 384033/22747 | $0.44 | 9 | B3R3E2 |
| alice | G_alice_personal | ✓ | 9.0 | 135.8 | 13/4243 | 384946/23034 | $0.44 | 9 | B3R3E2 |

### T6_db_schema

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✗ | 10.0 | 149.8 | 12/1465 | 271760/15518 | $0.27 | 8 | G1R2E1B3 |
| alice | A_stock | ✗ | 9.5 | 52.8 | 10/1493 | 197653/14678 | $0.23 | 6 | G1R2E1B1 |
| alice | A_stock | ✗ | 9.5 | 59.8 | 10/1404 | 197253/14589 | $0.23 | 6 | G1R2E1B1 |
| alice | A_stock | ✗ | 9.5 | 58.9 | 10/1771 | 197534/14784 | $0.24 | 6 | G1R2E1B1 |
| alice | A_stock | ✗ | 9.5 | 47.2 | 10/1193 | 197482/14676 | $0.22 | 6 | G1R2E1B1 |
| alice | B_md | ✗ | 9.5 | 90.0 | 12/1982 | 274676/15897 | $0.29 | 8 | B4R2E1 |
| alice | B_md | ✗ | 9.5 | 51.4 | 10/1213 | 199458/14865 | $0.22 | 6 | G1R2E1B1 |
| alice | B_md | ✗ | 9.5 | 56.7 | 10/1479 | 199758/15296 | $0.23 | 6 | G1R2E1B1 |
| alice | B_md | ✗ | 9.5 | 63.0 | 10/1696 | 199720/15139 | $0.24 | 6 | G1R2E1B1 |
| alice | B_md | ✗ | 10.0 | 113.2 | 14/1929 | 350157/16630 | $0.33 | 10 | B5R3E1 |
| alice | C_md_agents | ✗ | 9.3 | 156.1 | 15/2818 | 401418/17498 | $0.38 | 11 | G1R2E1B6 |
| alice | C_md_agents | ✗ | 10.0 | 105.6 | 13/2084 | 321571/16494 | $0.32 | 9 | G1R2E1B3P1 |
| alice | C_md_agents | ✗ | 10.0 | 113.1 | 14/2209 | 360217/16539 | $0.34 | 10 | B4R3E1P1 |
| alice | C_md_agents | ✗ | 9.5 | 51.8 | 10/1415 | 205359/15072 | $0.23 | 6 | G1R2E1B1 |
| alice | C_md_agents | ✗ | 9.5 | 81.4 | 11/2019 | 243429/15897 | $0.27 | 7 | G1R2E1B2 |
| alice | D_md_skills | ✗ | 9.5 | 50.0 | 10/1394 | 202931/15813 | $0.24 | 6 | G1R2E1B1 |
| alice | D_md_skills | ✗ | 9.5 | 53.1 | 10/1463 | 203355/15798 | $0.24 | 6 | G1R2E1B1 |
| alice | D_md_skills | ✗ | 9.5 | 94.7 | 16/2321 | 437546/18088 | $0.39 | 12 | B6R3E1P1 |
| alice | D_md_skills | ✗ | 9.5 | 63.0 | 15/2108 | 395364/17474 | $0.36 | 11 | B6R3E1 |
| alice | D_md_skills | ✗ | 9.8 | 63.5 | 13/2335 | 318794/17284 | $0.33 | 9 | B4R3E1 |
| alice | E_full | ✗ | 9.3 | 61.7 | 15/2179 | 405235/17166 | $0.37 | 11 | G2R3E1B4 |
| alice | E_full | ✗ | 9.5 | 32.5 | 9/1266 | 170135/14924 | $0.21 | 5 | G1R1E1B1 |
| alice | E_full | ✗ | 10.0 | 62.5 | 15/2169 | 403347/16985 | $0.36 | 11 | B6R3E1 |
| alice | E_full | ✗ | 10.0 | 73.0 | 13/2361 | 327064/17476 | $0.33 | 9 | G1R2E1B4 |
| alice | E_full | ✗ | 9.5 | 32.6 | 10/1360 | 208191/15514 | $0.24 | 6 | G1R2E1B1 |
| alice | F_full_plus_domain | ✗ | 9.3 | 75.6 | 15/2751 | 385036/41274 | $0.52 | 11 | B6R3E1 |
| alice | F_full_plus_domain | ✗ | 9.5 | 33.8 | 10/1364 | 209610/15463 | $0.24 | 6 | G1R2E1B1 |
| alice | F_full_plus_domain | ✗ | 9.5 | 44.3 | 10/1593 | 209558/15602 | $0.24 | 6 | G1R2E1B1 |
| alice | F_full_plus_domain | ✗ | 9.5 | 46.8 | 11/1543 | 248569/15834 | $0.26 | 7 | G1R2E1B2 |
| alice | F_full_plus_domain | ✗ | 9.5 | 65.7 | 13/2080 | 327930/17019 | $0.32 | 9 | G1R2E1B4 |

### T7_tg_bot

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 8.8 | 59.8 | 13/1826 | 306801/15410 | $0.30 | 9 | B4R3W1 |
| alice | A_stock | ✓ | 9.3 | 54.2 | 13/1900 | 307030/15504 | $0.30 | 9 | B3G1R3W1 |
| alice | A_stock | ✓ | 8.8 | 51.7 | 12/1834 | 271761/15351 | $0.28 | 8 | B3R3W1 |
| alice | A_stock | ✓ | 8.8 | 42.0 | 12/1503 | 270371/15007 | $0.27 | 8 | B3R3W1 |
| alice | A_stock | ✓ | 8.5 | 44.2 | 13/1573 | 306399/15186 | $0.29 | 9 | B3G1R3W1 |
| alice | B_md | ✓ | 8.5 | 53.4 | 12/1436 | 273562/15446 | $0.27 | 8 | B3R3W1 |
| alice | B_md | ✓ | 9.3 | 46.1 | 12/1382 | 273310/15356 | $0.27 | 8 | B3R3W1 |
| alice | B_md | ✓ | 9.3 | 45.4 | 13/1529 | 309905/15543 | $0.29 | 9 | B3G1R3W1 |
| alice | B_md | ✓ | 9.3 | 43.2 | 12/1464 | 273518/15427 | $0.27 | 8 | B3R3W1 |
| alice | B_md | ✓ | 9.5 | 63.0 | 14/2035 | 347787/16169 | $0.33 | 10 | B3G1R4W1 |
| alice | C_md_agents | ✓ | 9.3 | 45.2 | 12/1442 | 280674/15444 | $0.27 | 8 | B3R3W1 |
| alice | C_md_agents | ✓ | 9.0 | 53.5 | 13/1613 | 320039/15900 | $0.30 | 9 | B3R4W1 |
| alice | C_md_agents | ✓ | 9.3 | 44.6 | 13/1413 | 319637/15724 | $0.29 | 9 | B3R4W1 |
| alice | C_md_agents | ✓ | 9.3 | 44.7 | 13/1620 | 318284/15708 | $0.30 | 9 | B3G1R3W1 |
| alice | C_md_agents | ✓ | 9.0 | 49.8 | 13/1658 | 318330/15664 | $0.30 | 9 | B3G1R3W1 |
| alice | D_md_skills | ✓ | 9.0 | 42.9 | 12/1454 | 278277/16130 | $0.28 | 8 | B3R3W1 |
| alice | D_md_skills | ✓ | 9.3 | 49.9 | 12/1693 | 279553/16324 | $0.28 | 8 | B3R3W1 |
| alice | D_md_skills | ✓ | 9.0 | 45.6 | 12/1390 | 278177/16059 | $0.27 | 8 | B3R3W1 |
| alice | D_md_skills | ✓ | 9.3 | 51.1 | 12/1397 | 278161/16043 | $0.27 | 8 | B3R3W1 |
| alice | D_md_skills | ✓ | 9.0 | 39.4 | 12/1349 | 278195/16062 | $0.27 | 8 | B3R3W1 |
| alice | E_full | ✓ | 9.3 | 45.1 | 12/1471 | 285296/16110 | $0.28 | 8 | B3R3W1 |
| alice | E_full | ✓ | 9.3 | 45.6 | 13/1622 | 323628/16306 | $0.30 | 9 | B3G1R3W1 |
| alice | E_full | ✓ | 8.8 | 86.0 | 14/2072 | 363369/17124 | $0.34 | 10 | B3G1R4W1 |
| alice | E_full | ✓ | 9.5 | 49.4 | 13/1367 | 324763/16288 | $0.30 | 9 | B3R4W1 |
| alice | E_full | ✓ | 9.3 | 66.3 | 13/1926 | 324688/16681 | $0.32 | 9 | B3R4W1 |
| alice | F_full_plus_domain | ✓ | 9.3 | 50.3 | 12/1804 | 288329/16304 | $0.29 | 8 | B3R3W1 |
| alice | F_full_plus_domain | ✓ | 9.0 | 51.3 | 12/1653 | 287403/16186 | $0.29 | 8 | B3R3W1 |
| alice | F_full_plus_domain | ✓ | 9.5 | 60.6 | 12/1336 | 286894/15901 | $0.28 | 8 | B3R3W1 |
| alice | F_full_plus_domain | ✓ | 9.3 | 52.0 | 12/1627 | 287436/16084 | $0.29 | 8 | B3R3W1 |
| alice | F_full_plus_domain | ✓ | 9.0 | 48.4 | 12/1487 | 287109/16011 | $0.28 | 8 | B3R3W1 |

### T8_longctx

| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |
|---|---|---|---|---|---|---|---|---|---|
| alice | A_stock | ✓ | 9.5 | 35.4 | 10/982 | 199821/14961 | $0.22 | 6 | B3R1E1 |
| alice | A_stock | ✓ | 9.3 | 34.7 | 10/1146 | 200108/15106 | $0.22 | 6 | B2G1R1E1 |
| alice | A_stock | ✓ | 9.3 | 28.7 | 10/1010 | 200286/15200 | $0.22 | 6 | B2G1R1E1 |
| alice | A_stock | ✓ | 9.5 | 34.1 | 10/1013 | 199929/15028 | $0.22 | 6 | B2G1R1E1 |
| alice | A_stock | ✓ | 9.5 | 31.4 | 11/1158 | 236907/15184 | $0.24 | 7 | B4R1E1 |
| alice | B_md | ✓ | 9.5 | 36.5 | 10/1190 | 202719/15802 | $0.23 | 6 | B2G1R1E1 |
| alice | B_md | ✓ | 9.8 | 31.3 | 10/1255 | 202641/15700 | $0.23 | 6 | B2G1R1E1 |
| alice | B_md | ✓ | 9.8 | 30.1 | 10/1098 | 202683/15704 | $0.23 | 6 | B2G1R1E1 |
| alice | B_md | ✓ | 9.3 | 28.6 | 10/1058 | 202494/15575 | $0.23 | 6 | B2G1R1E1 |
| alice | B_md | ✓ | 9.5 | 30.0 | 10/1018 | 202224/15494 | $0.22 | 6 | B2G1R1E1 |
| alice | C_md_agents | ✓ | 9.8 | 32.4 | 10/1148 | 208046/15702 | $0.23 | 6 | B2G1R1E1 |
| alice | C_md_agents | ✓ | 9.3 | 33.4 | 10/1189 | 208081/15760 | $0.23 | 6 | B2G1R1E1 |
| alice | C_md_agents | ✓ | 9.5 | 33.3 | 11/1174 | 246201/15702 | $0.25 | 7 | B2G2R1E1 |
| alice | C_md_agents | ✓ | 9.5 | 32.6 | 10/1089 | 208013/15672 | $0.23 | 6 | B2G1R1E1 |
| alice | C_md_agents | ✓ | 9.5 | 31.5 | 11/1234 | 244823/15847 | $0.25 | 7 | B3G1R1E1 |
| alice | D_md_skills | ✓ | 9.8 | 36.4 | 10/1346 | 206225/16610 | $0.24 | 6 | B2G1R1E1 |
| alice | D_md_skills | ✓ | 9.5 | 34.1 | 10/1115 | 205723/16239 | $0.23 | 6 | B2G1R1E1 |
| alice | D_md_skills | ✓ | 9.5 | 42.2 | 12/2094 | 286641/17967 | $0.31 | 8 | B2G2R2E1 |
| alice | D_md_skills | ✓ | 9.5 | 32.3 | 10/1236 | 206738/16470 | $0.24 | 6 | B2G1R1E1 |
| alice | D_md_skills | ✓ | 9.8 | 37.9 | 16/1698 | 214390/53180 | $0.48 | 7 | T1B2G1R1E1 |
| alice | E_full | ✓ | 9.3 | 36.8 | 10/1179 | 211646/16462 | $0.24 | 6 | B2G1R1E1 |
| alice | E_full | ✓ | 9.3 | 31.1 | 10/1057 | 211255/16294 | $0.23 | 6 | B2G1R1E1 |
| alice | E_full | ✓ | 9.5 | 35.5 | 11/1573 | 252061/17414 | $0.27 | 7 | B2G1R2E1 |
| alice | E_full | ✓ | 9.5 | 31.9 | 10/1084 | 210975/16126 | $0.23 | 6 | B2G1R1E1 |
| alice | E_full | ✓ | 9.3 | 36.0 | 10/1217 | 211763/16515 | $0.24 | 6 | B2G1R1E1 |
| alice | G_alice_personal | ✓ | 9.3 | 39.4 | 11/1284 | 263972/45692 | $0.45 | 7 | B4R1E1 |
| alice | G_alice_personal | ✓ | 9.3 | 41.2 | 10/1220 | 245445/19357 | $0.27 | 6 | B2G1R1E1 |
| alice | G_alice_personal | ✓ | 9.8 | 54.4 | 13/1743 | 380562/20147 | $0.36 | 9 | B3G2E2R1 |
| alice | G_alice_personal | ✓ | 9.3 | 47.9 | 10/1075 | 245947/19373 | $0.27 | 6 | B2G1R1E1 |
| alice | G_alice_personal | ✓ | 9.3 | 54.1 | 13/1760 | 380530/20123 | $0.36 | 9 | B3G2E2R1 |

## M-test rule bias check

Surfacing cases where the verify rule may have penalized actually-good code (`rule_wrong`) or where high `code_quality` coexists with `passed=false` (a sign the rule is too strict).

| Setup | Task | Sample | Passed | Code quality | Judge rule_call |
|---|---|---|---|---|---|
| A_stock | M1_no_comments | 1 | ✓ | 9 | rule_correct |
| A_stock | M1_no_comments | 2 | ✓ | 9 | rule_correct |
| A_stock | M1_no_comments | 3 | ✓ | 9 | rule_correct |
| A_stock | M1_no_comments | 4 | ✓ | 9 | rule_correct |
| A_stock | M1_no_comments | 5 | ✓ | 9 | rule_correct |
| B_md | M1_no_comments | 1 | ✓ | 9 | rule_correct |
| B_md | M1_no_comments | 2 | ✓ | 9 | rule_correct |
| B_md | M1_no_comments | 3 | ✓ | 9 | rule_correct |
| B_md | M1_no_comments | 4 | ✓ | 9 | rule_correct |
| B_md | M1_no_comments | 5 | ✓ | 9 | rule_correct |
| C_md_agents | M1_no_comments | 1 | ✓ | 9 | rule_correct |
| C_md_agents | M1_no_comments | 2 | ✓ | 9 | rule_correct |
| C_md_agents | M1_no_comments | 3 | ✓ | 9 | rule_correct |
| C_md_agents | M1_no_comments | 4 | ✓ | 9 | rule_correct |
| C_md_agents | M1_no_comments | 5 | ✓ | 9 | rule_correct |
| D_md_skills | M1_no_comments | 1 | ✓ | 9 | rule_correct |
| D_md_skills | M1_no_comments | 2 | ✓ | 9 | rule_correct |
| D_md_skills | M1_no_comments | 3 | ✓ | 9 | rule_correct |
| D_md_skills | M1_no_comments | 4 | ✓ | 9 | rule_correct |
| D_md_skills | M1_no_comments | 5 | ✓ | 9 | rule_correct |
| E_full | M1_no_comments | 1 | ✓ | 9 | rule_correct |
| E_full | M1_no_comments | 2 | ✓ | 9 | rule_correct |
| E_full | M1_no_comments | 3 | ✓ | 9 | rule_correct |
| E_full | M1_no_comments | 4 | ✓ | 9 | rule_correct |
| E_full | M1_no_comments | 5 | ✓ | 9 | rule_correct |
| G_alice_personal | M1_no_comments | 1 | ✓ | 9 | rule_correct |
| G_alice_personal | M1_no_comments | 2 | ✓ | 9 | rule_correct |
| G_alice_personal | M1_no_comments | 3 | ✓ | 9 | rule_correct |
| G_alice_personal | M1_no_comments | 4 | ✓ | 9 | rule_correct |
| G_alice_personal | M1_no_comments | 5 | ✓ | 9 | rule_correct |
| A_stock | M2_minimal_change | 1 | ✓ | 9 | rule_correct |
| A_stock | M2_minimal_change | 2 | ✓ | 9 | rule_correct |
| A_stock | M2_minimal_change | 3 | ✓ | 9 | rule_correct |
| A_stock | M2_minimal_change | 4 | ✓ | 9 | rule_correct |
| A_stock | M2_minimal_change | 5 | ✓ | 9 | rule_correct |
| B_md | M2_minimal_change | 1 | ✓ | 9 | rule_correct |
| B_md | M2_minimal_change | 2 | ✓ | 9 | rule_correct |
| B_md | M2_minimal_change | 3 | ✓ | 9 | rule_correct |
| B_md | M2_minimal_change | 4 | ✓ | 9 | rule_correct |
| B_md | M2_minimal_change | 5 | ✓ | 9 | rule_correct |
| C_md_agents | M2_minimal_change | 1 | ✓ | 9 | rule_correct |
| C_md_agents | M2_minimal_change | 2 | ✓ | 9 | rule_correct |
| C_md_agents | M2_minimal_change | 3 | ✓ | 9 | rule_correct |
| C_md_agents | M2_minimal_change | 4 | ✓ | 9 | rule_correct |
| C_md_agents | M2_minimal_change | 5 | ✓ | 9 | rule_correct |
| D_md_skills | M2_minimal_change | 1 | ✓ | 9 | rule_correct |
| D_md_skills | M2_minimal_change | 2 | ✓ | 9 | rule_correct |
| D_md_skills | M2_minimal_change | 3 | ✓ | 9 | rule_correct |
| D_md_skills | M2_minimal_change | 4 | ✓ | 9 | rule_correct |
| D_md_skills | M2_minimal_change | 5 | ✓ | 9 | rule_correct |
| E_full | M2_minimal_change | 1 | ✓ | 9 | rule_correct |
| E_full | M2_minimal_change | 2 | ✓ | 9 | rule_correct |
| E_full | M2_minimal_change | 3 | ✓ | 9 | rule_correct |
| E_full | M2_minimal_change | 4 | ✓ | 9 | rule_correct |
| E_full | M2_minimal_change | 5 | ✓ | 9 | rule_correct |
| G_alice_personal | M2_minimal_change | 1 | ✓ | 9 | rule_correct |
| G_alice_personal | M2_minimal_change | 2 | ✓ | 9 | rule_correct |
| G_alice_personal | M2_minimal_change | 3 | ✓ | 9 | rule_correct |
| G_alice_personal | M2_minimal_change | 4 | ✓ | 9 | rule_correct |
| G_alice_personal | M2_minimal_change | 5 | ✓ | 9 | rule_correct |
| A_stock | M3_no_internal_validation | 1 | ✓ | 9 | rule_correct |
| A_stock | M3_no_internal_validation | 2 | ✓ | 7 | rule_correct |
| A_stock | M3_no_internal_validation | 3 | ✓ | 7 | rule_correct |
| A_stock | M3_no_internal_validation | 4 | ✓ | 7 | rule_correct |
| A_stock | M3_no_internal_validation | 5 | ✓ | 7 | neutral |
| B_md | M3_no_internal_validation | 1 | ✓ | 7 | rule_correct |
| B_md | M3_no_internal_validation | 2 | ✓ | 9 | rule_correct |
| B_md | M3_no_internal_validation | 3 | ✓ | 7 | rule_correct |
| B_md | M3_no_internal_validation | 4 | ✓ | 9 | rule_correct |
| B_md | M3_no_internal_validation | 5 | ✓ | 7 | rule_correct |
| C_md_agents | M3_no_internal_validation | 1 | ✓ | 7 | rule_wrong |
| C_md_agents | M3_no_internal_validation | 2 | ✓ | 8 | rule_correct |
| C_md_agents | M3_no_internal_validation | 3 | ✓ | 7 | rule_correct |
| C_md_agents | M3_no_internal_validation | 4 | ✓ | 7 | rule_correct |
| C_md_agents | M3_no_internal_validation | 5 | ✓ | 7 | rule_correct |
| D_md_skills | M3_no_internal_validation | 1 | ✓ | 7 | rule_correct |
| D_md_skills | M3_no_internal_validation | 2 | ✓ | 9 | rule_correct |
| D_md_skills | M3_no_internal_validation | 3 | ✓ | 7 | rule_correct |
| D_md_skills | M3_no_internal_validation | 4 | ✓ | 7 | rule_correct |
| D_md_skills | M3_no_internal_validation | 5 | ✓ | 7 | rule_correct |
| E_full | M3_no_internal_validation | 1 | ✓ | 7 | rule_correct |
| E_full | M3_no_internal_validation | 2 | ✓ | 7 | rule_correct |
| E_full | M3_no_internal_validation | 3 | ✓ | 7 | rule_correct |
| E_full | M3_no_internal_validation | 4 | ✓ | 7 | rule_correct |
| E_full | M3_no_internal_validation | 5 | ✓ | 7 | rule_correct |
| G_alice_personal | M3_no_internal_validation | 1 | ✓ | 7 | rule_correct |
| G_alice_personal | M3_no_internal_validation | 2 | ✓ | 7 | rule_correct |
| G_alice_personal | M3_no_internal_validation | 3 | ✓ | 8 | rule_correct |
| G_alice_personal | M3_no_internal_validation | 4 | ✓ | 7 | rule_correct |
| G_alice_personal | M3_no_internal_validation | 5 | ✓ | 8 | neutral |
| A_stock | M4_run_tests | 1 | ✓ | 10 | neutral |
| A_stock | M4_run_tests | 3 | ✓ | 10 | rule_correct |
| A_stock | M4_run_tests | 4 | ✓ | 10 | rule_correct |
| B_md | M4_run_tests | 2 | ✓ | 10 | rule_correct |
| B_md | M4_run_tests | 4 | ✓ | 10 | rule_correct |
| B_md | M4_run_tests | 5 | ✓ | 10 | rule_correct |
| C_md_agents | M4_run_tests | 1 | ✓ | 10 | rule_correct |
| C_md_agents | M4_run_tests | 3 | ✓ | 10 | rule_correct |
| C_md_agents | M4_run_tests | 4 | ✓ | 10 | rule_correct |
| C_md_agents | M4_run_tests | 5 | ✓ | 10 | rule_correct |
| D_md_skills | M4_run_tests | 2 | ✓ | 10 | rule_correct |
| D_md_skills | M4_run_tests | 3 | ✓ | 10 | rule_correct |
| D_md_skills | M4_run_tests | 4 | ✓ | 10 | rule_correct |
| D_md_skills | M4_run_tests | 5 | ✓ | 10 | rule_correct |
| E_full | M4_run_tests | 1 | ✓ | 10 | rule_correct |
| E_full | M4_run_tests | 2 | ✓ | 10 | rule_correct |
| E_full | M4_run_tests | 3 | ✓ | 10 | rule_correct |
| E_full | M4_run_tests | 4 | ✓ | 10 | rule_correct |
| E_full | M4_run_tests | 5 | ✓ | 10 | rule_correct |
| G_alice_personal | M4_run_tests | 1 | ✓ | 10 | rule_correct |
| G_alice_personal | M4_run_tests | 2 | ✓ | 10 | rule_correct |
| G_alice_personal | M4_run_tests | 3 | ✓ | 10 | rule_correct |
| G_alice_personal | M4_run_tests | 4 | ✓ | 10 | rule_correct |
| G_alice_personal | M4_run_tests | 5 | ✓ | 10 | rule_correct |

**Summary:** 1/114 M-runs flagged as `rule_wrong` by judge. 

## Within-cell variance (across samples, same runner+setup+task)

Estimates how much one setup × task varies on repeat runs. Effect sizes smaller than this aren't reliable.

| Cell | n | Quality mean ± stdev | Time mean ± stdev (s) | Tokens out range |
|---|---|---|---|---|
| alice|A_stock|M1_no_comments | 5 | 9.55 ± 0.11 | 28.7 ± 2.3 | 729–1086 |
| alice|B_md|M1_no_comments | 5 | 9.55 ± 0.11 | 29.8 ± 2.0 | 887–1157 |
| alice|C_md_agents|M1_no_comments | 5 | 9.55 ± 0.11 | 30.8 ± 2.8 | 827–1197 |
| alice|D_md_skills|M1_no_comments | 5 | 9.60 ± 0.14 | 28.8 ± 2.7 | 810–1044 |
| alice|E_full|M1_no_comments | 5 | 9.50 ± 0.00 | 32.5 ± 5.3 | 981–1742 |
| alice|G_alice_personal|M1_no_comments | 5 | 9.55 ± 0.11 | 35.0 ± 3.6 | 728–1354 |
| alice|A_stock|M2_minimal_change | 5 | 9.75 ± 0.00 | 28.9 ± 3.2 | 840–981 |
| alice|B_md|M2_minimal_change | 5 | 9.70 ± 0.11 | 29.1 ± 2.0 | 849–990 |
| alice|C_md_agents|M2_minimal_change | 5 | 9.70 ± 0.11 | 28.4 ± 1.8 | 888–996 |
| alice|D_md_skills|M2_minimal_change | 5 | 9.65 ± 0.14 | 30.7 ± 3.6 | 876–1269 |
| alice|E_full|M2_minimal_change | 5 | 9.65 ± 0.14 | 33.3 ± 4.8 | 951–994 |
| alice|G_alice_personal|M2_minimal_change | 5 | 9.70 ± 0.11 | 40.2 ± 2.0 | 816–1032 |
| alice|A_stock|M3_no_internal_validation | 5 | 9.15 ± 0.34 | 31.0 ± 3.3 | 636–879 |
| alice|B_md|M3_no_internal_validation | 5 | 9.30 ± 0.41 | 26.2 ± 4.3 | 490–872 |
| alice|C_md_agents|M3_no_internal_validation | 5 | 9.05 ± 0.11 | 31.1 ± 5.4 | 768–886 |
| alice|D_md_skills|M3_no_internal_validation | 5 | 9.15 ± 0.34 | 24.5 ± 3.6 | 522–824 |
| alice|E_full|M3_no_internal_validation | 5 | 9.00 ± 0.00 | 26.3 ± 2.1 | 629–884 |
| alice|G_alice_personal|M3_no_internal_validation | 5 | 9.10 ± 0.14 | 37.4 ± 3.3 | 642–883 |
| alice|A_stock|M4_run_tests | 5 | 10.00 ± 0.00 | 25.0 ± 2.5 | 470–589 |
| alice|B_md|M4_run_tests | 5 | 10.00 ± 0.00 | 24.3 ± 1.4 | 570–612 |
| alice|C_md_agents|M4_run_tests | 5 | 10.00 ± 0.00 | 23.3 ± 1.7 | 571–601 |
| alice|D_md_skills|M4_run_tests | 5 | 10.00 ± 0.00 | 25.9 ± 3.0 | 596–836 |
| alice|E_full|M4_run_tests | 5 | 10.00 ± 0.00 | 23.9 ± 0.8 | 572–604 |
| alice|G_alice_personal|M4_run_tests | 5 | 10.00 ± 0.00 | 30.4 ± 2.0 | 565–592 |
| alice|A_stock|M5_multiturn_memory | 5 | 10.00 ± 0.00 | 84.8 ± 13.2 | 3927–5981 |
| alice|B_md|M5_multiturn_memory | 5 | 10.00 ± 0.00 | 68.8 ± 4.9 | 3589–4467 |
| alice|C_md_agents|M5_multiturn_memory | 5 | 10.00 ± 0.00 | 73.3 ± 15.9 | 2758–5910 |
| alice|D_md_skills|M5_multiturn_memory | 5 | 10.00 ± 0.00 | 73.8 ± 15.3 | 2205–5238 |
| alice|E_full|M5_multiturn_memory | 5 | 10.00 ± 0.00 | 76.3 ± 20.0 | 2951–6035 |
| alice|G_alice_personal|M5_multiturn_memory | 5 | 10.00 ± 0.00 | 80.0 ± 15.9 | 2079–5190 |
| alice|A_stock|T1_bug | 5 | 9.80 ± 0.11 | 25.6 ± 2.6 | 647–865 |
| alice|B_md|T1_bug | 5 | 9.90 ± 0.14 | 27.5 ± 2.1 | 715–905 |
| alice|C_md_agents|T1_bug | 5 | 9.95 ± 0.11 | 28.3 ± 4.6 | 695–806 |
| alice|D_md_skills|T1_bug | 5 | 9.85 ± 0.14 | 29.5 ± 3.3 | 794–1343 |
| alice|E_full|T1_bug | 5 | 9.85 ± 0.14 | 29.4 ± 4.6 | 781–1095 |
| alice|G_alice_personal|T1_bug | 5 | 9.75 ± 0.00 | 37.6 ± 3.6 | 689–845 |
| alice|A_stock|T2_lru | 5 | 9.45 ± 0.11 | 53.4 ± 4.1 | 1293–1356 |
| alice|B_md|T2_lru | 5 | 9.45 ± 0.11 | 45.3 ± 7.9 | 1278–1458 |
| alice|C_md_agents|T2_lru | 5 | 9.55 ± 0.11 | 49.1 ± 7.1 | 1296–1633 |
| alice|D_md_skills|T2_lru | 5 | 9.40 ± 0.14 | 47.8 ± 4.6 | 1146–1474 |
| alice|E_full|T2_lru | 5 | 9.50 ± 0.00 | 48.9 ± 3.7 | 1260–1500 |
| alice|G_alice_personal|T2_lru | 5 | 9.45 ± 0.11 | 66.0 ± 6.7 | 1290–1526 |
| alice|A_stock|T3_refactor | 5 | 9.75 ± 0.00 | 33.4 ± 5.2 | 985–1057 |
| alice|B_md|T3_refactor | 5 | 9.75 ± 0.00 | 33.5 ± 2.1 | 1038–1238 |
| alice|C_md_agents|T3_refactor | 5 | 9.85 ± 0.14 | 35.6 ± 4.3 | 1145–1279 |
| alice|D_md_skills|T3_refactor | 5 | 9.75 ± 0.00 | 48.1 ± 12.2 | 1094–2491 |
| alice|E_full|T3_refactor | 5 | 9.75 ± 0.00 | 34.3 ± 2.9 | 1034–1290 |
| alice|G_alice_personal|T3_refactor | 5 | 9.80 ± 0.11 | 53.0 ± 9.6 | 1072–1663 |
| alice|A_stock|T4_crud | 5 | 8.75 ± 0.25 | 62.3 ± 7.0 | 1295–2150 |
| alice|B_md|T4_crud | 5 | 8.90 ± 0.14 | 65.1 ± 9.5 | 1448–1844 |

## Findings (auto-generated heuristics)

- **E_full vs A_stock**: time -2.9s, cache_creation +1161 tokens, quality +0.01.
