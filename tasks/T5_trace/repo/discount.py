from datetime import date


def parse_date(s):
    """Parse 'YYYY-MM-DD' into a date object."""
    parts = s.split("-")
    return date(int(parts[0]), int(parts[1]), int(parts[2]))


def days_since(d, ref):
    """How many days from `d` until `ref` (ref >= d)."""
    return (ref - d).days


def tier(amount):
    if amount >= 1000:
        return "gold"
    elif amount >= 500:
        return "silver"
    else:
        return "bronze"
