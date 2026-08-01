from is_palindrome import is_palindrome

def test_is_palindrome_simple():
    assert is_palindrome("racecar") == True

def test_is_palindrome_case_insensitive():
    assert is_palindrome("RaceCar") == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Hello, world!") == False

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True
