import { describe, it, expect } from 'vitest';
import { readFileSync } from 'node:fs';

const src = readFileSync('./bot.ts', 'utf8');

describe('bot.ts structure', () => {
  it('imports Bot from grammy', () => {
    expect(src).toMatch(/import\s+\{[^}]*\bBot\b[^}]*\}\s+from\s+["']grammy["']/);
  });

  it('registers a /start command handler', () => {
    // Either bot.command("start", ...) or bot.command(/^start/, ...)
    expect(src).toMatch(/\.command\s*\(\s*["']start["']\s*,/);
  });

  it('registers a /help command handler', () => {
    expect(src).toMatch(/\.command\s*\(\s*["']help["']\s*,/);
  });

  it('uses ctx.reply for responses', () => {
    expect(src).toMatch(/ctx\.reply\s*\(/);
  });

  it('includes inline keyboard or reply_markup for /start', () => {
    // Either InlineKeyboard imported, or reply_markup in start handler
    expect(
      src.match(/InlineKeyboard/) || src.match(/reply_markup/) || src.match(/Keyboard/)
    ).toBeTruthy();
  });

  it('handles errors with bot.catch', () => {
    expect(src).toMatch(/bot\.catch\s*\(/);
  });
});
