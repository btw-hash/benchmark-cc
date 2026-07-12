#!/usr/bin/env node
// runner.mjs — drives `claude -p` across setup × task matrix.
// Usage: node runner.mjs --runner alice [--setup A_stock] [--task T1_bug]
//        (omit --setup/--task to run the full matrix)
//
// Per run: copies tasks/<T>/repo → runs/<runner>/<setup>/<task>/repo,
// invokes claude -p there with CLAUDE_CONFIG_DIR=setups/<setup>/.claude,
// captures stream-json, computes diff, runs verify.ps1, appends jsonl row.

import { spawn } from "node:child_process";
import { mkdirSync, existsSync, readFileSync, writeFileSync, appendFileSync, cpSync, rmSync, readdirSync, statSync } from "node:fs";
import { join, resolve } from "node:path";
import { argv } from "node:process";
import os from "node:os";

const ROOT = resolve(import.meta.dirname);
const args = Object.fromEntries(
  argv.slice(2).reduce((acc, x, i, a) => {
    if (x.startsWith("--")) acc.push([x.slice(2), a[i + 1]?.startsWith("--") ? true : a[i + 1] ?? true]);
    return acc;
  }, [])
);
const RUNNER = args.runner ?? os.hostname();
const ONLY_SETUP = args.setup;
const ONLY_TASK = args.task;
const MODEL = args.model ?? "claude-opus-4-7";
const SAMPLES = parseInt(args.samples ?? "1", 10);

const setups = listDirs(join(ROOT, "setups")).filter((s) => !ONLY_SETUP || s === ONLY_SETUP);
const tasks = listDirs(join(ROOT, "tasks")).filter((t) => !ONLY_TASK || t === ONLY_TASK);

// Bootstrap auth: copy runner's live ~/.claude/.credentials.json into each setup
// so subscription auth carries over. This file is gitignored — each runner uses their own.
const liveCreds = join(os.homedir(), ".claude", ".credentials.json");
if (!existsSync(liveCreds)) {
  console.error("ERROR: ~/.claude/.credentials.json not found. Run `claude` once to log in.");
  process.exit(1);
}
for (const setup of setups) {
  const target = join(ROOT, "setups", setup, ".claude", ".credentials.json");
  cpSync(liveCreds, target);
}
console.log("auth: bootstrapped credentials into all setups");

console.log(`runner=${RUNNER} model=${MODEL}`);
console.log(`setups: ${setups.join(", ")}`);
console.log(`tasks:  ${tasks.join(", ")}`);
console.log(`total runs: ${setups.length * tasks.length}\n`);

const resultsFile = join(ROOT, "results", `runs_${RUNNER}.jsonl`);
mkdirSync(join(ROOT, "results"), { recursive: true });

// Build matrix: each task may have a .setups whitelist (one setup name per line).
// If absent: include all setups except F_full_plus_domain (domain-only) and
// G_*_personal that belong to OTHER runners (each personal slot is owned by one runner).
//
// G_<runner>_personal is auto-included for the current runner.
// G_<other>_personal is included if it exists in the repo (committed by the other runner).
const matrix = [];
for (const task of tasks) {
  const allowFile = join(ROOT, "tasks", task, ".setups");
  let allowed;
  if (existsSync(allowFile)) {
    allowed = readFileSync(allowFile, "utf8").split("\n").map((s) => s.trim()).filter(Boolean);
  } else {
    allowed = setups.filter((s) => {
      if (s === "F_full_plus_domain") return false;
      return true;
    });
  }
  for (const setup of setups) {
    if (allowed.includes(setup)) matrix.push({ setup, task });
  }
}
console.log(`matrix: ${matrix.length} (setup × task) pairs after per-task whitelist\n`);

console.log(`samples per cell: ${SAMPLES}\n`);

for (const { setup, task } of matrix) {
  for (let sample_idx = 1; sample_idx <= SAMPLES; sample_idx++) {
    const existing = existsSync(resultsFile)
      ? readFileSync(resultsFile, "utf8").split("\n").filter(Boolean).map((l) => JSON.parse(l))
      : [];
    if (existing.some((r) => r.setup === setup && r.task === task && (r.sample_idx ?? 1) === sample_idx)) {
      console.log(`SKIP ${setup} × ${task} #${sample_idx} (already done)`);
      continue;
    }
    await runOne(setup, task, sample_idx);
  }
}

console.log(`\nDone. Results → ${resultsFile}`);

// ─────────────────────────────────────────────────────────────────────────────

async function runOne(setup, task, sample_idx = 1) {
  console.log(`\n=== ${setup} × ${task} #${sample_idx} ===`);
  const workdir = join(ROOT, "runs", RUNNER, setup, task, `s${sample_idx}`);
  if (existsSync(workdir)) rmSync(workdir, { recursive: true, force: true });
  mkdirSync(workdir, { recursive: true });
  cpSync(join(ROOT, "tasks", task, "repo"), join(workdir, "repo"), { recursive: true });

  const prompt = readFileSync(join(ROOT, "tasks", task, "prompt.md"), "utf8");
  const prompt2Path = join(ROOT, "tasks", task, "prompt2.md");
  const hasMultiTurn = existsSync(prompt2Path);
  const configDir = join(ROOT, "setups", setup, ".claude");
  const streamPath = join(workdir, "stream.jsonl");

  const t0 = Date.now();
  let stream;
  if (hasMultiTurn) {
    const prompt2 = readFileSync(prompt2Path, "utf8");
    stream = await invokeClaudeMultiTurn(prompt, prompt2, join(workdir, "repo"), configDir, streamPath);
  } else {
    stream = await invokeClaude(prompt, join(workdir, "repo"), configDir, streamPath);
  }
  const wall_ms = Date.now() - t0;

  // Verify
  const verifyScript = join(ROOT, "tasks", task, "verify.ps1");
  let passed = null;
  let verifyOut = "";
  if (existsSync(verifyScript)) {
    const v = await runPS(verifyScript, join(workdir, "repo"));
    passed = v.code === 0;
    verifyOut = v.stdout;
  }

  // Diff (filter test cache artifacts)
  const rawDiff = await captureDiff(join(workdir, "repo"), join(ROOT, "tasks", task, "repo"));
  const diff = filterDiff(rawDiff);
  writeFileSync(join(workdir, "diff.patch"), diff);

  // Final summary
  const row = {
    runner: RUNNER,
    setup,
    task,
    sample_idx,
    timestamp: new Date().toISOString(),
    wall_ms,
    model: MODEL,
    multi_turn: hasMultiTurn,
    duration_api_ms: stream.duration_api_ms,
    num_turns: stream.num_turns,
    input_tokens: stream.input_tokens,
    output_tokens: stream.output_tokens,
    cache_read: stream.cache_read,
    cache_creation: stream.cache_creation,
    total_cost_usd: stream.total_cost_usd,
    tool_calls: stream.tool_calls,
    passed,
    verify_details: verifyOut,
    files_touched: countFilesInDiff(diff),
    diff_path: `runs/${RUNNER}/${setup}/${task}/s${sample_idx}/diff.patch`,
    stream_path: `runs/${RUNNER}/${setup}/${task}/s${sample_idx}/stream.jsonl`,
    final_text: stream.final_text,
  };
  appendFileSync(resultsFile, JSON.stringify(row) + "\n");
  console.log(
    `  ${passed === null ? "?" : passed ? "PASS" : "FAIL"} ` +
      `${(wall_ms / 1000).toFixed(1)}s | in=${stream.input_tokens} out=${stream.output_tokens} ` +
      `cache_r=${stream.cache_read} cache_w=${stream.cache_creation} ` +
      `turns=${stream.num_turns} cost=$${stream.total_cost_usd?.toFixed(3) ?? "?"}`
  );
}

async function invokeClaudeMultiTurn(prompt1, prompt2, cwd, configDir, streamPath) {
  // Turn 1
  const t1Path = streamPath + ".turn1";
  const turn1 = await invokeClaude(prompt1, cwd, configDir, t1Path);
  // Parse session_id from turn1 stream
  const turn1Lines = readFileSync(t1Path, "utf8").split("\n").filter(Boolean);
  let sessionId = null;
  for (const line of turn1Lines) {
    try {
      const ev = JSON.parse(line);
      if (ev.session_id) sessionId = ev.session_id;
    } catch {}
  }
  if (!sessionId) {
    console.warn("  (no session_id captured in turn1; turn2 will start fresh)");
  }
  // Turn 2 with --resume
  const t2Path = streamPath + ".turn2";
  const turn2 = await invokeClaude(prompt2, cwd, configDir, t2Path, sessionId);
  // Merge: turn2 tokens/cost stand on top of turn1; concatenate streams
  const merged = readFileSync(t1Path, "utf8") + "\n" + readFileSync(t2Path, "utf8");
  writeFileSync(streamPath, merged);
  return {
    input_tokens: (turn1.input_tokens || 0) + (turn2.input_tokens || 0),
    output_tokens: (turn1.output_tokens || 0) + (turn2.output_tokens || 0),
    cache_read: (turn1.cache_read || 0) + (turn2.cache_read || 0),
    cache_creation: (turn1.cache_creation || 0) + (turn2.cache_creation || 0),
    total_cost_usd: (turn1.total_cost_usd || 0) + (turn2.total_cost_usd || 0),
    num_turns: (turn1.num_turns || 0) + (turn2.num_turns || 0),
    duration_api_ms: (turn1.duration_api_ms || 0) + (turn2.duration_api_ms || 0),
    tool_calls: mergeToolCalls(turn1.tool_calls, turn2.tool_calls),
    final_text: turn2.final_text,
  };
}

function mergeToolCalls(a, b) {
  const out = { ...(a ?? {}) };
  for (const [k, v] of Object.entries(b ?? {})) out[k] = (out[k] ?? 0) + v;
  return out;
}

function invokeClaude(prompt, cwd, configDir, streamPath, resumeSessionId = null) {
  return new Promise((res, rej) => {
    const claudeArgs = [
      "-p",
      "--output-format", "stream-json",
      "--verbose",
      "--model", MODEL,
      "--permission-mode", "bypassPermissions",
    ];
    if (resumeSessionId) {
      claudeArgs.push("--resume", resumeSessionId);
    }
    const child = spawn(
      "claude",
      claudeArgs,
      {
        cwd,
        env: { ...process.env, CLAUDE_CONFIG_DIR: configDir },
        stdio: ["pipe", "pipe", "pipe"],
        shell: true,
      }
    );
    child.stdin.write(prompt);
    child.stdin.end();
    let buf = "";
    const stream = {
      input_tokens: 0, output_tokens: 0, cache_read: 0, cache_creation: 0,
      total_cost_usd: 0, num_turns: 0, duration_api_ms: 0,
      tool_calls: {}, final_text: "",
    };
    const out = [];
    child.stdout.on("data", (d) => {
      buf += d.toString();
      const lines = buf.split("\n");
      buf = lines.pop();
      for (const line of lines) {
        if (!line.trim()) continue;
        out.push(line);
        try {
          const ev = JSON.parse(line);
          if (ev.type === "assistant" && ev.message?.content) {
            for (const block of ev.message.content) {
              if (block.type === "tool_use") {
                stream.tool_calls[block.name] = (stream.tool_calls[block.name] ?? 0) + 1;
              }
            }
          }
          if (ev.type === "result") {
            stream.input_tokens = ev.usage?.input_tokens ?? 0;
            stream.output_tokens = ev.usage?.output_tokens ?? 0;
            stream.cache_read = ev.usage?.cache_read_input_tokens ?? 0;
            stream.cache_creation = ev.usage?.cache_creation_input_tokens ?? 0;
            stream.total_cost_usd = ev.total_cost_usd ?? 0;
            stream.num_turns = ev.num_turns ?? 0;
            stream.duration_api_ms = ev.duration_api_ms ?? 0;
            stream.final_text = ev.result ?? "";
          }
        } catch {}
      }
    });
    child.stderr.on("data", (d) => process.stderr.write(d));
    child.on("close", (code) => {
      writeFileSync(streamPath, out.join("\n") + "\n");
      if (code !== 0 && code !== null) console.warn(`  (claude exit ${code})`);
      res(stream);
    });
    child.on("error", rej);
  });
}

function runPS(script, cwd) {
  return new Promise((res) => {
    const child = spawn("pwsh", ["-NoProfile", "-File", script], { cwd, shell: true });
    let stdout = "", stderr = "";
    child.stdout.on("data", (d) => (stdout += d.toString()));
    child.stderr.on("data", (d) => (stderr += d.toString()));
    child.on("close", (code) => res({ code, stdout, stderr }));
  });
}

async function captureDiff(workRepo, originalRepo) {
  // Quick file-by-file diff. Avoids requiring git init in worktree.
  const { execSync } = await import("node:child_process");
  try {
    return execSync(`git diff --no-index --no-color "${originalRepo}" "${workRepo}"`, {
      encoding: "utf8", maxBuffer: 50 * 1024 * 1024,
    });
  } catch (e) {
    // git diff --no-index exits 1 when there are differences
    return e.stdout?.toString() ?? "";
  }
}

function countFilesInDiff(diff) {
  return (diff.match(/^diff /gm) || []).length;
}

function filterDiff(diff) {
  // Drop sections for test-artifact dirs.
  const skipRe = /(__pycache__|\.pytest_cache|node_modules|\.next|dist|build)\//;
  const blocks = diff.split(/(?=^diff )/m);
  return blocks.filter((b) => !skipRe.test(b.split("\n")[0] ?? "")).join("");
}

function listDirs(p) {
  if (!existsSync(p)) return [];
  return readdirSync(p).filter((f) => statSync(join(p, f)).isDirectory());
}
