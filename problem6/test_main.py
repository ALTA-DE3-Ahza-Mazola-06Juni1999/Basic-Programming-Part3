import unittest
from main import full_prima

class TestFullPrima(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEqual(full_prima(2), True, "Expected True for prime number (2)")
        self.assertEqual(full_prima(3), True, "Expected True for prime number (3)")
        self.assertEqual(full_prima(23), True, "Expected True for prime number (23)")
        self.assertEqual(full_prima(37), True, "Expected True for prime number (37)")
        self.assertEqual(full_prima(53), True, "Expected True for prime number (53)")
    def test_non_prime_numbers(self):
        self.assertEqual(full_prima(11), False, "Expected False for non-prime number (11)")
        self.assertEqual(full_prima(13), False, "Expected False for non-prime number (13)")
        self.assertEqual(full_prima(29), False, "Expected False for non-prime number (29)")
        self.assertEqual(full_prima(41), False, "Expected False for non-prime number (41)")
        self.assertEqual(full_prima(43), False, "Expected False for non-prime number (43)")
    def test_negative_numbers(self):
        self.assertEqual(full_prima(-2), False, "Expected False for negative number (-2)")
        self.assertEqual(full_prima(-3), False, "Expected False for negative number (-3)")
    def test_zero(self):
        self.assertEqual(full_prima(0), False, "Expected False for zero (0)")
    def test_one(self):
        self.assertEqual(full_prima(1), False, "Expected False for one (1)")
        
if __name__ == '__main__':
    unittest.main()