from orders import process


def _orders():
    return [
        {"id": 1, "user_id": "u1", "region": "EU", "currency": "EUR", "status": "paid", "date": "2026-01-01", "amount": 1500},
        {"id": 2, "user_id": "u2", "region": "EU", "currency": "EUR", "status": "paid", "date": "2026-01-02", "amount": 750},
        {"id": 3, "user_id": "u3", "region": "EU", "currency": "EUR", "status": "paid", "date": "2026-01-03", "amount": 300},
        {"id": 4, "user_id": "u4", "region": "US", "currency": "EUR", "status": "paid", "date": "2026-01-04", "amount": 999},
        {"id": 5, "user_id": "u5", "region": "EU", "currency": "USD", "status": "paid", "date": "2026-01-05", "amount": 999},
        {"id": 6, "user_id": "u6", "region": "EU", "currency": "EUR", "status": "pending", "date": "2026-01-06", "amount": 999},
        {"id": 7, "user_id": "u7", "region": "EU", "currency": "EUR", "status": "paid", "date": "2026-99-99", "amount": 999},
        {"id": 8, "user_id": "u8", "region": "EU", "currency": "EUR", "status": "paid", "date": "2026-01-08", "amount": 1200},
    ]


def test_vip_discount():
    r = process(_orders(), "EU", "EUR", vip_users={"u1"}, banned_users=set(), today="2026-12-31")
    o1 = next(x for x in r["orders"] if x["id"] == 1)
    assert o1["discount"] == 0.20
    assert o1["final"] == 1500 * 0.80


def test_high_amount_discount():
    r = process(_orders(), "EU", "EUR", vip_users=set(), banned_users=set(), today="2026-12-31")
    o8 = next(x for x in r["orders"] if x["id"] == 8)
    assert o8["discount"] == 0.10


def test_mid_amount_discount():
    r = process(_orders(), "EU", "EUR", vip_users=set(), banned_users=set(), today="2026-12-31")
    o2 = next(x for x in r["orders"] if x["id"] == 2)
    assert o2["discount"] == 0.05


def test_low_amount_no_discount():
    r = process(_orders(), "EU", "EUR", vip_users=set(), banned_users=set(), today="2026-12-31")
    o3 = next(x for x in r["orders"] if x["id"] == 3)
    assert o3["discount"] == 0.0


def test_filters_region_currency_status_date_banned():
    r = process(_orders(), "EU", "EUR", vip_users=set(), banned_users={"u1"}, today="2026-12-31")
    ids = {x["id"] for x in r["orders"]}
    assert ids == {2, 3, 8}  # u1 banned, u4 wrong region, u5 wrong currency, u6 not paid, u7 future


def test_total():
    r = process(_orders(), "EU", "EUR", vip_users=set(), banned_users=set(), today="2026-12-31")
    expected = 1500 * 0.90 + 750 * 0.95 + 300 * 1.0 + 1200 * 0.90
    assert abs(r["total"] - expected) < 1e-6


def test_empty():
    r = process([], "EU", "EUR", vip_users=set(), banned_users=set(), today="2026-12-31")
    assert r == {"orders": [], "total": 0}
