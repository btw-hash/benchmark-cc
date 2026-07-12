#!/usr/bin/env node
// judge.mjs — for each run row, ask Opus 4.7 to score quality 1-10 across:
//   correctness, completeness, scope_discipline, code_quality.
// Reads results/runs_*.jsonl, augments each row with `quality` object,
// writes results/judged_<runner>.jsonl.
//
// Uses `claude -p` headless with a temp config dir (no hooks/agents/skills)
// so judging is deterministic and identical across both runners.

import { spawn } from "node:child_process";
import { readFileSync, writeFileSync, existsSync, readdirSync, mkdirSync, cpSync } from "node:fs";
import { join, resolve } from "node:path";
import os from "node:os";

const ROOT = resolve(import.meta.dirname);
const JUDGE_CONFIG = join(ROOT, ".judge-config", ".claude");
mkdirSync(JUDGE_CONFIG, { recursive: true });
writeFileSync(join(JUDGE_CONFIG, "settings.json"), JSON.stringify({ model: "claude-opus-4-7" }));
const liveCreds = join(os.homedir(), ".claude", ".credentials.json");
if (existsSync(liveCreds)) cpSync(liveCreds, join(JUDGE_CONFIG, ".credentials.json"));

const RUBRIC = `You are evaluating the output of a coding agent on a fixed task.

You'll receive:
1. The task prompt
2. The agent's final message to the user
3. The diff of files it changed
4. Whether automated verify passed

IMPORTANT: For M1-M4 tasks, the verify checks adherence to a *specific stylistic rule* (e.g. "no comments", "minimal change"), NOT whether the code is intrinsically good. You should score code_quality INDEPENDENTLY of whether verify passed — sometimes the verify-failing variant is actually the better solution and your code_quality score should reflect that. The benchmark needs to surface cases where the rule is wrong.

Score on a 1-10 scale across four axes. Be strict — reserve 9-10 for genuinely excellent work.

- correctness (1-10): did it actually solve the user's underlying task (not just the rule)? Check soundness, edge cases.
- completeness (1-10): did it finish, or leave TODO/half-done parts?
- scope_discipline (1-10): did it touch only what was needed? Lower for unrequested refactors, unrelated changes.
- code_quality (1-10): readability, idiomatic style, no anti-patterns. **For M-tasks: judge the code on its own merit, regardless of rule adherence.**

If this is an M1-M4 task, also include "rule_call": one of "rule_correct" (the stylistic rule produced better code), "rule_wrong" (the rule produced worse code than ignoring it would), or "neutral" (no meaningful difference).

Respond with ONLY a JSON object, no prose, no markdown fences:

{"correctness": N, "completeness": N, "scope_discipline": N, "code_quality": N, "rule_call": "rule_correct" | "rule_wrong" | "neutral" | null, "rationale": "1-2 sentences"}`;

const runnerFiles = readdirSync(join(ROOT, "results")).filter((f) => /^runs_.*\.jsonl$/.test(f));
if (runnerFiles.length === 0) {
  console.error("No results/runs_*.jsonl found. Run runner.mjs first.");
  process.exit(1);
}

for (const file of runnerFiles) {
  const rows = readFileSync(join(ROOT, "results", file), "utf8").split("\n").filter(Boolean).map(JSON.parse);
  const judgedPath = join(ROOT, "results", file.replace(/^runs_/, "judged_"));
  const existing = existsSync(judgedPath)
    ? readFileSync(judgedPath, "utf8").split("\n").filter(Boolean).map(JSON.parse)
    : [];
  console.log(`\n=== ${file} (${rows.length} rows) ===`);

  for (const row of rows) {
    if (existing.some((e) => e.setup === row.setup && e.task === row.task && (e.sample_idx ?? 1) === (row.sample_idx ?? 1))) {
      console.log(`SKIP ${row.setup} × ${row.task} #${row.sample_idx ?? 1} (already judged)`);
      continue;
    }
    // M5_multiturn_memory is a recall test, not a code-quality test.
    // Skip LLM-judging entirely; the verify_details (recall_score=N/6) IS the quality signal.
    if (row.task.startsWith("M5_")) {
      const score = parseRecallScore(row.verify_details);
      const augmented = {
        ...row,
        quality: {
          correctness: score,
          completeness: score,
          scope_discipline: 10,  // recall task doesn't have scope to violate
          code_quality: 10,      // not measured for recall task
          rule_call: null,
          rationale: `Recall test — score from verify (${score}/10, scaled from N/6).`,
        },
      };
      writeFileSync(judgedPath, [...existing, augmented].map((r) => JSON.stringify(r)).join("\n") + "\n");
      existing.push(augmented);
      console.log(`  ${row.setup} × ${row.task} #${row.sample_idx ?? 1} ... recall_score=${score}/10 (no LLM judge)`);
      continue;
    }
    const promptPath = join(ROOT, "tasks", row.task, "prompt.md");
    const diffPath = join(ROOT, row.diff_path);
    const taskPrompt = existsSync(promptPath) ? readFileSync(promptPath, "utf8") : "(missing)";
    const diff = existsSync(diffPath) ? readFileSync(diffPath, "utf8") : "(missing)";
    const judgeInput = `${RUBRIC}

==== TASK PROMPT ====
${taskPrompt}

==== AGENT'S FINAL MESSAGE ====
${row.final_text ?? "(empty)"}

==== DIFF ====
${diff.slice(0, 50000)}

==== AUTOMATED VERIFY ====
passed: ${row.passed}
`;

    process.stdout.write(`  ${row.setup} × ${row.task} ... `);
    const quality = await invokeJudge(judgeInput);
    console.log(
      quality
        ? `corr=${quality.correctness} comp=${quality.completeness} scope=${quality.scope_discipline} qual=${quality.code_quality}`
        : "FAILED"
    );
    const augmented = { ...row, quality };
    writeFileSync(judgedPath, [...existing, augmented].map((r) => JSON.stringify(r)).join("\n") + "\n");
    existing.push(augmented);
  }
}
console.log("\nDone.");

function parseRecallScore(details) {
  if (!details) return 0;
  const m = details.match(/recall_score=(\d+)\/(\d+)/);
  if (!m) return 0;
  const got = parseInt(m[1], 10);
  const total = parseInt(m[2], 10);
  return Math.round((got / total) * 10);
}

function invokeJudge(input) {
  return new Promise((res) => {
    const child = spawn(
      "claude",
      ["-p", "--output-format", "stream-json", "--verbose", "--model", "claude-opus-4-7", "--permission-mode", "bypassPermissions"],
      {
        env: { ...process.env, CLAUDE_CONFIG_DIR: JUDGE_CONFIG },
        stdio: ["pipe", "pipe", "pipe"],
        shell: true,
      }
    );
    child.stdin.write(input);
    child.stdin.end();
    let buf = "";
    let result = null;
    child.stdout.on("data", (d) => {
      buf += d.toString();
      const lines = buf.split("\n");
      buf = lines.pop();
      for (const line of lines) {
        if (!line.trim()) continue;
        try {
          const ev = JSON.parse(line);
          if (ev.type === "result" && ev.result) {
            const m = ev.result.match(/\{[\s\S]*\}/);
            if (m) {
              try { result = JSON.parse(m[0]); } catch {}
            }
          }
        } catch {}
      }
    });
    child.stderr.on("data", () => {});
    child.on("close", () => res(result));
  });
}
