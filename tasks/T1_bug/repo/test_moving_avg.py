import pytest
from moving_avg import moving_average


def test_basic():
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]


def test_window_equals_length():
    assert moving_average([10, 20, 30], 3) == [20.0]


def test_window_too_large():
    assert moving_average([1, 2], 5) == []


def test_window_invalid():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)


def test_floats():
    result = moving_average([1.0, 2.0, 3.0, 4.0], 2)
    assert result == [1.5, 2.5, 3.5]
