# T1 Oracle (do NOT show to runner)

Bug: off-by-one in the loop range.

`range(len(values) - window)` produces `0..N-W-1`, missing the last valid window starting at index `N-W`.

Fix: `range(len(values) - window + 1)`.

Failing tests on the buggy version:
- `test_basic` — expected `[2.0, 3.0, 4.0]`, got `[2.0, 3.0]`
- `test_window_equals_length` — expected `[20.0]`, got `[]`
- `test_floats` — expected `[1.5, 2.5, 3.5]`, got `[1.5, 2.5]`

Expected difficulty: trivial. Any decent model fixes in 1-2 turns.

Why it's good for the benchmark: signal for setup overhead. If Setup E takes 4× tokens of Setup A for this, you're paying for agents/skills that don't activate on a 3-line fix.
