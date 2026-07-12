from stats import compute_mean


def test_basic():
    assert compute_mean([1, 2, 3, 4, 5]) == 3.0


def test_single():
    assert compute_mean([42]) == 42.0


def test_floats():
    assert abs(compute_mean([1.5, 2.5]) - 2.0) < 1e-9
