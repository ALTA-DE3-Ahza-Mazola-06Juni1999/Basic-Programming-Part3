import unittest
from main import pangkat

class TestPangkat(unittest.TestCase):
    def test_pangkat_2_3(self):
        result = pangkat(2, 3)
        self.assertEqual(result, 8, msg="Expected 8 for 2^3")

    def test_pangkat_5_3(self):
        result = pangkat(5, 3)
        self.assertEqual(result, 125, msg="Expected 125 for 5^3")

    def test_pangkat_10_2(self):
        result = pangkat(10, 2)
        self.assertEqual(result, 100, msg="Expected 100 for 10^2")

    def test_pangkat_2_5(self):
        result = pangkat(2, 5)
        self.assertEqual(result, 32, msg="Expected 32 for 2^5")

    def test_pangkat_7_3(self):
        result = pangkat(7, 3)
        self.assertEqual(result, 343, msg="Expected 343 for 7^3")
        
if __name__ == '__main__':
    unittest.main()