#!/usr/bin/python3
"""Module for Rectangle class tests."""

from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def setUp(self):
        """Set up for the tests."""
        Rectangle._Base__nb_objects = 0

    def test_id(self):
        """Test for id."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 15)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 16)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_attributes(self):
        """Test for attributes."""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_attributes_edge_cases(self):
        """Test for attributes edge cases."""
        # Test with negative width
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)

        # Test with zero height
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0)

        # Test with negative x
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -3, 4)

        # Test with negative y
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -4)

    # Test Area Function
    def test_area(self):
        """Test for area."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

        r = Rectangle(8, 7)
        self.assertEqual(r.area(), 56)

    # Test Display Function
    def test_display(self):
        """Test for display."""
        r = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

        r = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    # Test __str__ Function
    def test_str(self):
        """Test for __str__."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (17) 1/0 - 5/5")

    # Test update Function
    def test_update(self):
        """Test for update."""
        r = Rectangle(10, 10, 10, 10)

        r.update(89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(89, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(89, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 10)

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        r.update(id=90)
        self.assertEqual(r.id, 90)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        r.update(width=3, x=2)
        self.assertEqual(r.id, 90)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 5)

        r.update(y=1, width=2, x=3, id=91)
        self.assertEqual(r.id, 91)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.id, 91)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {
            'x': 1, 'y': 9, 'id': 18,
            'height': 2, 'width': 10
            })
        self.assertTrue(type(r1_dictionary) is dict)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)


if __name__ == "__main__":
    unittest.main()
