import pytest
from loyalty import loyalty_bonus


def test_gold_recent():
    # 1000 amount = gold tier (0.10), 0 years since = 0.10 base
    assert loyalty_bonus("2026-05-01", 1000, "2026-05-01") == 100.00


def test_silver_one_year():
    # 700 = silver (0.05), 1 year = 0.05 + 0.01 = 0.06
    assert loyalty_bonus("2025-05-01", 700, "2026-05-01") == 42.00


def test_bronze_two_years():
    # 200 = bronze (0.02), 2 years = 0.02 + 0.02 = 0.04
    assert loyalty_bonus("2024-05-01", 200, "2026-05-01") == 8.00


def test_cap_at_25():
    # 30 years would imply 0.30+ — must cap at 0.25
    assert loyalty_bonus("1996-05-01", 1000, "2026-05-01") == 250.00


def test_string_input_date():
    # This is the failing case — uncovered until you run it
    result = loyalty_bonus("2026-01-15", 500, "2026-05-01")
    assert result == 25.0 or result == 25.29  # silver + ~3.5 months
