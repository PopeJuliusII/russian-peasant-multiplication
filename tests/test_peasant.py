"""
Unittesting, because it has actually kind of grown on me!
"""

import unittest
from app import peasant


class TestMultiplication(unittest.TestCase):
    """
    Tests for the multiplication of positive integers
    with the peasant function from app.
    """

    def test_positive(self):
        """
        Testing for regular positive integers.
        Tests include the edge case of zero,
        and with the larger number passed as
        both the first and second position.
        """
        self.assertEqual(peasant(0, 0), 0)
        self.assertEqual(peasant(1, 0), 0)
        self.assertEqual(peasant(1, 1), 1)
        self.assertEqual(peasant(5, 3), 15)
        self.assertEqual(peasant(6, 8), 48)

    def test_very_positive(self):
        """
        Testing for large positive integers.
        Note: Testing with this c value may take up to 10 seconds.
        """
        large_a = 10 ** 100
        large_b = 9000 ** 9000
        large_c = 987654321 ** 9876

        self.assertEqual(peasant(large_a, large_a), large_a ** 2)
        self.assertEqual(peasant(large_a, large_b), large_a * large_b)
        self.assertEqual(peasant(large_c, large_c), large_c ** 2)


if __name__ == "__main__":
    unittest.main()
