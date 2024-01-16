#!/usr/bin/python3
"""Module for Square class tests."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class."""

    def setUp(self):
        """Set up for the tests."""
        Square._Rectangle__nb_objects = 0

    def test_id(self):
        """Test for id."""
        s1 = Square(5)
        self.assertEqual(s1.id, 21)

        s2 = Square(2, 2)
        self.assertEqual(s2.id, 22)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.id, 23)

    def test_str(self):
        """Test for __str__."""
        s = Square(5, 1, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 1/1 - 5")

    def test_update(self):
        """Test for update."""
        s = Square(5, 5, 5, 5)

        s.update(89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

        s.update(89, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

        s.update(y=1, size=2, x=3, id=90)
        self.assertEqual(s.id, 90)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 1)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 24, 'x': 2, 'size': 10, 'y': 1})
        self.assertTrue(type(s1_dictionary) is dict)

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertFalse(s1 == s2)


if __name__ == "__main__":
    unittest.main()
