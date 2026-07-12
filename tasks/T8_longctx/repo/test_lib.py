from lib import percentile


def test_p50_ten_values():
    # Nearest-rank: idx = ceil(p/100 * N) - 1 = ceil(5) - 1 = 4 → s[4] = 5
    assert percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50) == 5


def test_p10_ten_values():
    # ceil(1) - 1 = 0 → s[0] = 1
    assert percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 1


def test_p100():
    assert percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100) == 10


def test_p0():
    # ceil(0) - 1 = -1, clamp to 0 → s[0]
    assert percentile([1, 2, 3, 4, 5], 0) == 1


def test_unsorted_input():
    assert percentile([5, 1, 3, 4, 2], 50) == 3


def test_p25():
    # ceil(2.5) - 1 = 2 → s[2] = 3
    assert percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25) == 3


def test_empty():
    assert percentile([], 50) == 0.0


def test_invalid_p():
    import pytest
    with pytest.raises(ValueError):
        percentile([1, 2, 3], -1)
    with pytest.raises(ValueError):
        percentile([1, 2, 3], 101)
