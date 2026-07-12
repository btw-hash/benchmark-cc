#!/usr/bin/env node
// merge.mjs — produces report.md from results/judged_*.jsonl.

import { readFileSync, writeFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { join, resolve } from "node:path";

const ROOT = resolve(import.meta.dirname);
const files = readdirSync(join(ROOT, "results")).filter((f) => /^judged_.*\.jsonl$/.test(f));
if (files.length === 0) {
  console.error("No results/judged_*.jsonl found. Run judge.mjs first.");
  process.exit(1);
}

const rows = files.flatMap((f) =>
  readFileSync(join(ROOT, "results", f), "utf8").split("\n").filter(Boolean).map(JSON.parse)
);
const runners = [...new Set(rows.map((r) => r.runner))].sort();
const setups = [...new Set(rows.map((r) => r.setup))].sort();
const tasks = [...new Set(rows.map((r) => r.task))].sort();

const fmt = (n, d = 0) => (n == null ? "?" : n.toFixed(d));
const sum = (xs, k) => xs.reduce((a, r) => a + (r[k] ?? 0), 0);
const avg = (xs, k) => (xs.length ? sum(xs, k) / xs.length : 0);
const qSum = (r) =>
  r.quality
    ? (r.quality.correctness + r.quality.completeness + r.quality.scope_discipline + r.quality.code_quality) / 4
    : null;

let out = "# benchmark-cc — report\n\n";
out += `Runners: ${runners.join(", ")} | Setups: ${setups.length} | Tasks: ${tasks.length} | Total runs: ${rows.length}\n\n`;

// ─── Setup compositions (what's actually in each config layer)
const SETUP_SOURCES = {
  A_stock: "empty baseline",
  B_md: "generic 30-line CLAUDE.md (original)",
  C_md_agents: "agents from github.com/affaan-m/everything-claude-code (MIT)",
  D_md_skills: "skills from github.com/obra/superpowers (MIT)",
  E_full: "B + C + D + secrets-scan hook",
  F_full_plus_domain: "E + 4 domain experts (prisma/telegram/supabase/chrome-ext)",
};
out += "## Setup compositions\n\n";
out += "What is actually inside each setup — to interpret quality/cost deltas in context.\n\n";
out += "| Setup | CLAUDE.md (lines) | Agents (count) | Skills (count) | Hooks | Total size (KB) | Source |\n";
out += "|---|---|---|---|---|---|---|\n";
for (const s of setups) {
  const dir = join(ROOT, "setups", s, ".claude");
  if (!existsSync(dir)) { out += `| ${s} | ? | ? | ? | ? | ? | ? |\n`; continue; }
  const mdPath = join(dir, "CLAUDE.md");
  const mdLines = existsSync(mdPath) ? readFileSync(mdPath, "utf8").split("\n").length : 0;
  const agentsDir = join(dir, "agents");
  const skillsDir = join(dir, "skills");
  const hooksDir = join(dir, "hooks");
  const agents = existsSync(agentsDir) ? readdirSync(agentsDir).filter((f) => f.endsWith(".md")) : [];
  const skills = existsSync(skillsDir) ? readdirSync(skillsDir).filter((f) => statSync(join(skillsDir, f)).isDirectory()) : [];
  const hooks = existsSync(hooksDir) ? readdirSync(hooksDir).filter((f) => statSync(join(hooksDir, f)).isFile()) : [];
  const sizeKB = Math.round(dirSize(dir) / 1024);
  const src = SETUP_SOURCES[s] ?? (s.startsWith("G_") ? "personal config (runner-owned, gitignored)" : "?");
  out += `| ${s} | ${mdLines || "—"} | ${agents.length} | ${skills.length} | ${hooks.length} | ${sizeKB} | ${src} |\n`;
}
out += "\n";
out += "### Agent / skill rosters\n\n";
for (const s of setups) {
  const dir = join(ROOT, "setups", s, ".claude");
  const agentsDir = join(dir, "agents");
  const skillsDir = join(dir, "skills");
  const agents = existsSync(agentsDir) ? readdirSync(agentsDir).filter((f) => f.endsWith(".md")).map((f) => f.replace(/\.md$/, "")) : [];
  const skills = existsSync(skillsDir) ? readdirSync(skillsDir).filter((f) => statSync(join(skillsDir, f)).isDirectory()) : [];
  if (agents.length === 0 && skills.length === 0) continue;
  out += `**${s}**\n`;
  if (agents.length > 0) out += `- agents (${agents.length}): ${agents.join(", ")}\n`;
  if (skills.length > 0) out += `- skills (${skills.length}): ${skills.join(", ")}\n`;
  out += "\n";
}


// ─── Leaderboard by setup (averaged across all runners + tasks)
out += "## Leaderboard (by setup)\n\n";
out += "| Setup | Avg quality (/10) | Pass rate | Avg time (s) | Avg input | Avg output | Avg cache_r | Avg cache_w | Avg cost ($) | Avg turns |\n";
out += "|---|---|---|---|---|---|---|---|---|---|\n";
for (const s of setups) {
  const rs = rows.filter((r) => r.setup === s);
  const qs = rs.map(qSum).filter((q) => q != null);
  const pass = rs.filter((r) => r.passed === true).length;
  const passable = rs.filter((r) => r.passed != null).length;
  out += `| ${s} | ${fmt(qs.length ? qs.reduce((a, b) => a + b) / qs.length : null, 2)} | ${pass}/${passable} | ${fmt(avg(rs, "wall_ms") / 1000, 1)} | ${fmt(avg(rs, "input_tokens"))} | ${fmt(avg(rs, "output_tokens"))} | ${fmt(avg(rs, "cache_read"))} | ${fmt(avg(rs, "cache_creation"))} | ${fmt(avg(rs, "total_cost_usd"), 2)} | ${fmt(avg(rs, "num_turns"), 1)} |\n`;
}
out += "\n";

// ─── Per-task breakdown
out += "## Per-task results\n\n";
for (const t of tasks) {
  out += `### ${t}\n\n`;
  out += "| Runner | Setup | Pass | Quality | Time (s) | Tokens (in/out) | Cache (r/w) | Cost | Turns | Tools |\n";
  out += "|---|---|---|---|---|---|---|---|---|---|\n";
  for (const r of rows.filter((x) => x.task === t).sort((a, b) => (a.runner + a.setup).localeCompare(b.runner + b.setup))) {
    const tools = Object.entries(r.tool_calls ?? {}).map(([k, v]) => `${k[0]}${v}`).join("");
    out += `| ${r.runner} | ${r.setup} | ${r.passed === true ? "✓" : r.passed === false ? "✗" : "?"} | ${fmt(qSum(r), 1)} | ${fmt(r.wall_ms / 1000, 1)} | ${r.input_tokens}/${r.output_tokens} | ${r.cache_read}/${r.cache_creation} | $${fmt(r.total_cost_usd, 2)} | ${r.num_turns} | ${tools} |\n`;
  }
  out += "\n";
}

// ─── Noise floor (same setup × task across runners)
if (runners.length > 1) {
  out += "## Noise floor (variance between runners on identical setup × task)\n\n";
  out += "| Setup | Task | Quality range | Time range (s) | Token range (out) |\n";
  out += "|---|---|---|---|---|\n";
  for (const s of setups) {
    for (const t of tasks) {
      const rs = rows.filter((r) => r.setup === s && r.task === t);
      if (rs.length < 2) continue;
      const qs = rs.map(qSum).filter((q) => q != null);
      const tms = rs.map((r) => r.wall_ms / 1000);
      const outs = rs.map((r) => r.output_tokens);
      const range = (xs) => (xs.length ? `${Math.min(...xs).toFixed(1)}–${Math.max(...xs).toFixed(1)}` : "?");
      out += `| ${s} | ${t} | ${range(qs)} | ${range(tms)} | ${Math.min(...outs)}–${Math.max(...outs)} |\n`;
    }
  }
  out += "\n";
}

// ─── M-test rule-bias check
const mRows = rows.filter((r) => r.task.startsWith("M") && r.quality?.rule_call);
if (mRows.length > 0) {
  out += "## M-test rule bias check\n\n";
  out += "Surfacing cases where the verify rule may have penalized actually-good code (`rule_wrong`) or where high `code_quality` coexists with `passed=false` (a sign the rule is too strict).\n\n";
  out += "| Setup | Task | Sample | Passed | Code quality | Judge rule_call |\n|---|---|---|---|---|---|\n";
  for (const r of mRows.sort((a, b) => a.task.localeCompare(b.task))) {
    out += `| ${r.setup} | ${r.task} | ${r.sample_idx ?? 1} | ${r.passed ? "✓" : "✗"} | ${r.quality.code_quality} | ${r.quality.rule_call} |\n`;
  }
  out += "\n";
  const wrongCalls = mRows.filter((r) => r.quality.rule_call === "rule_wrong").length;
  out += `**Summary:** ${wrongCalls}/${mRows.length} M-runs flagged as \`rule_wrong\` by judge. ${wrongCalls > mRows.length * 0.3 ? "⚠️ High rate suggests M-rules need revision." : ""}\n\n`;
}

// ─── Sample variance (per-cell stdev when n>=2)
const cells = {};
for (const r of rows) {
  const k = `${r.runner}|${r.setup}|${r.task}`;
  (cells[k] = cells[k] ?? []).push(r);
}
const multiSampleCells = Object.entries(cells).filter(([, xs]) => xs.length >= 2);
if (multiSampleCells.length > 0) {
  out += "## Within-cell variance (across samples, same runner+setup+task)\n\n";
  out += "Estimates how much one setup × task varies on repeat runs. Effect sizes smaller than this aren't reliable.\n\n";
  out += "| Cell | n | Quality mean ± stdev | Time mean ± stdev (s) | Tokens out range |\n|---|---|---|---|---|\n";
  for (const [k, xs] of multiSampleCells.slice(0, 50)) {
    const qs = xs.map(qSum).filter((q) => q != null);
    const tms = xs.map((r) => r.wall_ms / 1000);
    const outs = xs.map((r) => r.output_tokens);
    const meanQ = qs.length ? qs.reduce((a, b) => a + b) / qs.length : null;
    const stdQ = meanQ != null && qs.length > 1
      ? Math.sqrt(qs.reduce((a, b) => a + (b - meanQ) ** 2, 0) / (qs.length - 1))
      : null;
    const meanT = tms.reduce((a, b) => a + b) / tms.length;
    const stdT = tms.length > 1
      ? Math.sqrt(tms.reduce((a, b) => a + (b - meanT) ** 2, 0) / (tms.length - 1))
      : 0;
    out += `| ${k} | ${xs.length} | ${meanQ?.toFixed(2) ?? "?"} ± ${stdQ?.toFixed(2) ?? "?"} | ${meanT.toFixed(1)} ± ${stdT.toFixed(1)} | ${Math.min(...outs)}–${Math.max(...outs)} |\n`;
  }
  out += "\n";
}

// ─── Findings (heuristic)
out += "## Findings (auto-generated heuristics)\n\n";
const A = rows.filter((r) => r.setup.startsWith("A"));
const fullSetups = setups.filter((s) => s.endsWith("_full"));
for (const fs of fullSetups) {
  const f = rows.filter((r) => r.setup === fs);
  if (A.length === 0 || f.length === 0) continue;
  const tDelta = (avg(f, "wall_ms") - avg(A, "wall_ms")) / 1000;
  const cwDelta = avg(f, "cache_creation") - avg(A, "cache_creation");
  const qA = A.map(qSum).filter(Boolean);
  const qF = f.map(qSum).filter(Boolean);
  const qDelta = qF.length && qA.length
    ? qF.reduce((a, b) => a + b) / qF.length - qA.reduce((a, b) => a + b) / qA.length
    : 0;
  out += `- **${fs} vs A_stock**: time ${tDelta >= 0 ? "+" : ""}${tDelta.toFixed(1)}s, cache_creation ${cwDelta >= 0 ? "+" : ""}${Math.round(cwDelta)} tokens, quality ${qDelta >= 0 ? "+" : ""}${qDelta.toFixed(2)}.\n`;
}

writeFileSync(join(ROOT, "report.md"), out);
console.log(`Wrote ${join(ROOT, "report.md")}`);

function dirSize(p) {
  if (!existsSync(p)) return 0;
  let total = 0;
  for (const e of readdirSync(p)) {
    const full = join(p, e);
    const st = statSync(full);
    if (st.isDirectory()) total += dirSize(full);
    else total += st.size;
  }
  return total;
}
