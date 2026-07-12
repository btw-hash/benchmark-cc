from discount import parse_date, days_since, tier


def loyalty_bonus(purchase_date_str, amount, today_str):
    """Compute a loyalty bonus: tier-based percentage of amount,
    plus 1% per full year since the purchase, capped at 25%.
    """
    purchase_date = parse_date(purchase_date_str)
    today = parse_date(today_str)
    days = days_since(purchase_date, today)
    years = days / 365
    base = {"gold": 0.10, "silver": 0.05, "bronze": 0.02}[tier(amount)]
    pct = base + years * 0.01
    if pct > 0.25:
        pct = 0.25
    return round(amount * pct, 2)
