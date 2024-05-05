import unittest
from main import prime_number

class TestPrimeNumber(unittest.TestCase):
    def test_prime_11(self):
        result = prime_number(11)
        self.assertEqual(result, "Prime", msg="Expected 'Prime' for input 11")

    def test_prime_13(self):
        result = prime_number(13)
        self.assertEqual(result, "Prime", msg="Expected 'Prime' for input 13")

    def test_prime_17(self):
        result = prime_number(17)
        self.assertEqual(result, "Prime", msg="Expected 'Prime' for input 17")

    def test_non_prime_20(self):
        result = prime_number(20)
        self.assertEqual(result, "Not Prime", msg="Expected 'Not Prime' for input 20")

    def test_non_prime_35(self):
        result = prime_number(35)
        self.assertEqual(result, "Not Prime", msg="Expected 'Not Prime' for input 35")
        
if __name__ == '__main__':
    unittest.main()