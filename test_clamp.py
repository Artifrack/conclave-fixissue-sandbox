import pytest
from clamp import clamp


def test_clamp_below_range():
    assert clamp(-5, 0, 10) == 0


def test_clamp_within_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_above_range():
    assert clamp(15, 0, 10) == 10


def test_clamp_invalid_range():
    with pytest.raises(ValueError, match="low must be <= high"):
        clamp(5, 10, 0)
