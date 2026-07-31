from reverse_words import reverse_words


def test_reverse_words_basic():
    assert reverse_words("the quick brown fox") == ["fox", "brown", "quick", "the"]
