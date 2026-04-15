import unittest
from calculator import sum_even_numbers

class TestCalculator(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(sum_even_numbers(5), 6)

if __name__ == "__main__":
    unittest.main()