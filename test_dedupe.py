from dedupe import dedupe_preserve_order


def test_dedupe_removes_duplicates_preserving_order():
    assert dedupe_preserve_order([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]


def test_dedupe_empty_list():
    assert dedupe_preserve_order([]) == []


def test_dedupe_no_duplicates():
    assert dedupe_preserve_order([1, 2, 3]) == [1, 2, 3]


def test_dedupe_strings():
    assert dedupe_preserve_order(["a", "b", "a", "c"]) == ["a", "b", "c"]
