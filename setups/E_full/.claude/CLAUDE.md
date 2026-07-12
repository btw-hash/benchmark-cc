# Engineering practices

## Think before you code

State your understanding of the problem in one sentence before touching files. If unsure, ask — guessing wastes more time than asking.

## Simplicity wins

Smallest change that solves the actual problem. No speculative abstractions, no defensive code for inputs that can't occur, no "while we're here" cleanup. Three similar lines beat a premature abstraction.

## Surgical edits

Touch what was asked. Don't rename neighbors, reformat unrelated code, or refactor inside a bug-fix task. If you spot something else worth fixing, mention it, don't do it.

## Explicit success criteria

Before claiming done: state what you tested, what passed, what you did not verify. "Tests pass + exercised the golden path" beats "should work".

## Code defaults

- No comments unless the WHY is non-obvious (hidden constraint, subtle invariant, workaround for a specific bug). Naming explains WHAT.
- Validate at system boundaries only (user input, external APIs). Trust internal code.
- No backwards-compat shims unless explicitly required.

## Verification

After code changes: run the test suite. Report pass/fail explicitly. Never claim done without evidence.
