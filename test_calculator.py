import unittest
from calculator import sum_even_numbers

class TestCalculator(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(sum_even_numbers(5), 6)

    def test_zero(self):
        self.assertEqual(sum_even_numbers(0), 0)

    def test_no_even(self):
        self.assertEqual(sum_even_numbers(1), 0)

if __name__ == "__main__":
    unittest.main()