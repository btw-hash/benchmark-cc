from search import find_pairs


def test_basic():
    result = find_pairs([1, 2, 3, 4, 5], 5)
    assert sorted(result) == sorted([(1, 4), (2, 3)])


def test_no_pairs():
    assert find_pairs([1, 2, 3], 100) == []


def test_empty():
    assert find_pairs([], 5) == []


def test_duplicates_handled():
    # Each pair returned at most once; order within pair: smaller first
    result = find_pairs([1, 1, 4, 4], 5)
    assert (1, 4) in result
    assert len(result) >= 1


def test_negative_numbers():
    assert sorted(find_pairs([-2, -1, 0, 1, 2, 3], 1)) == sorted([(-2, 3), (-1, 2), (0, 1)])
