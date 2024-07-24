import unittest
from main.palindrome_checker import is_palindrome

class TestPlaindromeChecker(unittest.TestCase):
    def test_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("OpenAI"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))
    
    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))
    
    def test_numbers(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1a2b2a1"))
        self.assertFalse(is_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()