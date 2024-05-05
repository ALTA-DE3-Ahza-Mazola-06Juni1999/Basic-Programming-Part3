import unittest
from main import palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_civic(self):
        result = palindrome("civic")
        self.assertEqual(result, True, msg="'civic' is a palindrome, so it should return True")

    def test_palindrome_katak(self):
        result = palindrome("katak")
        self.assertEqual(result, True, msg="'katak' is a palindrome, so it should return True")

    def test_palindrome_kasur_rusak(self):
        result = palindrome("kasur rusak")
        self.assertEqual(result, True, msg="'kasur rusak' is a palindrome, so it should return True")

    def test_palindrome_kupu_kupu(self):
        result = palindrome("kupu-kupu")
        self.assertEqual(result, False, msg="'kupu-kupu' is not a palindrome, so it should return False")

    def test_palindrome_lion(self):
        result = palindrome("lion")
        self.assertEqual(result, False, msg="'lion' is not a palindrome, so it should return False")
        
if __name__ == '__main__':
    unittest.main()