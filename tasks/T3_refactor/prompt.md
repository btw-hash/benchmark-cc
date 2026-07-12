The function `process` in `orders.py` works but is hard to read — deeply nested if/else, no helpers, no early returns.

Refactor it for readability without changing behavior. The full test suite in `test_orders.py` must continue to pass — do not modify the tests, do not change the public signature `process(orders, region, currency, vip_users, banned_users, today)`.

Run `python -m pytest test_orders.py -v` to verify. When tests pass, you are done.
