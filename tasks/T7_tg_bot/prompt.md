In `bot.ts`, implement a small Telegram bot using the grammY framework. It should:

1. Handle `/start` — reply with a welcome message and an inline keyboard with two buttons ("Help" and "About").
2. Handle `/help` — reply with usage instructions.
3. Handle errors gracefully via `bot.catch`.

Use idiomatic grammY patterns. Do not start the bot (no `bot.start()` call) — the test imports the module.

Run `npm install` then `npm test` to verify.
