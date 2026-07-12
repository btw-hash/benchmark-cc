A user reports the following error from the loyalty bonus script:

```
Traceback (most recent call last):
  File "main.py", line 8, in <module>
    bonus = loyalty_bonus("2026-01-15", "500", "2026-05-01")
  File "loyalty.py", line 11, in loyalty_bonus
    base = {"gold": 0.10, "silver": 0.05, "bronze": 0.02}[tier(amount)]
  File "discount.py", line 14, in tier
    if amount >= 1000:
TypeError: '>=' not supported between instances of 'str' and 'int'
```

Investigate the root cause and fix it. The fix must:
- Handle the case where `amount` is passed as a string (a common upstream issue from CSV parsing).
- Not break any existing tests in `test_loyalty.py`.
- Be applied in the most appropriate file — think about where the responsibility should live.

Run `python -m pytest test_loyalty.py -v` to verify. Done when all tests pass.
