#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines a class to test the function max_integer"""

    def test_max_integer(self):
        """Tests normal inputs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, -3, -4]), 2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([]), None)

    def test_max_integer_exceptions(self):
        """Tests exceptions"""
        self.assertRaises(TypeError, max_integer, [1, 2, "3", 4])
        self.assertRaises(TypeError, max_integer, None)

    def test_max_integer_edge_cases(self):
        """Tests edge cases"""
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, -1, -2]), 0)
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
