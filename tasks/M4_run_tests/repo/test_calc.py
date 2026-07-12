from calc import add, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(10, -4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(7, 0) == 0
