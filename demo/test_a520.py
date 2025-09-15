import unittest
from a520 import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("world"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

if __name__ == "__main__":
    unittest.main()
