#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 1, 2]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 5]), 5)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1000))), 999)

    # --- Edge cases supplémentaires ---
    def test_single_float(self):
        self.assertEqual(max_integer([3.14]), 3.14)

    def test_infinite_values(self):
        self.assertEqual(max_integer([1, 2, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, float('-inf')]), 2)

    def test_nan_value(self):
        import math
        # max_integer doit renvoyer le maximum parmi les autres nombres
        self.assertEqual(max_integer([1, 2, float('nan')]), 2)
        # si liste que NaN, il renvoie NaN
        self.assertTrue(math.isnan(max_integer([float('nan')])))

    def test_mix_extremes(self):
        self.assertEqual(max_integer([-1e10, 1e10, 0, 999]), 1e10)

    def test_large_and_small(self):
        self.assertEqual(max_integer([1e-10, 1e10, 5, -1e10]), 1e10)


if __name__ == '__main__':
    unittest.main()
