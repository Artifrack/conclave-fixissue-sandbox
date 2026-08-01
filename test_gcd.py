from gcd import gcd


def test_gcd_basic_case():
    assert gcd(48, 18) == 6


def test_gcd_swapped_inputs():
    assert gcd(18, 48) == 6


def test_gcd_coprime_numbers():
    assert gcd(17, 22) == 1


def test_gcd_one_divides_other():
    assert gcd(10, 5) == 5
    assert gcd(5, 10) == 5


def test_gcd_edge_cases():
    assert gcd(1, 1) == 1
    assert gcd(7, 7) == 7
