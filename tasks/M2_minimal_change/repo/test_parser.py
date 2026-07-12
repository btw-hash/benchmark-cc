from parser import compare_versions


def test_less():
    assert compare_versions("1.2.3", "1.2.4") == -1


def test_greater():
    assert compare_versions("2.0.0", "1.9.9") == 1


def test_equal():
    assert compare_versions("1.2.3", "1.2.3") == 0


def test_different_length():
    # This is the failing test: "1.2" vs "1.2.0" should be equal.
    assert compare_versions("1.2", "1.2.0") == 0
