from title_case import title_case


def test_title_case_basic():
    assert title_case("the quick brown fox") == "The Quick Brown Fox"


def test_title_case_single_word():
    assert title_case("hello") == "Hello"
