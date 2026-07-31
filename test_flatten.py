from flatten import flatten_one_level


def test_flatten_basic():
    assert flatten_one_level([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_flatten_empty():
    assert flatten_one_level([]) == []


def test_flatten_with_empty_sublist():
    assert flatten_one_level([[1], [], [2, 3]]) == [1, 2, 3]
