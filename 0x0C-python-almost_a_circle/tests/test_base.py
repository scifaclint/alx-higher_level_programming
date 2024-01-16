#!/usr/bin/python3
"""Module for Base class tests."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class."""

    def setUp(self):
        """Set up for the tests."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test for id."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_id_edge_cases(self):
        """Test for id edge cases."""
        # Test with negative id
        b6 = Base(-1)
        self.assertEqual(b6.id, -1)

        # Test with zero id
        b7 = Base(0)
        self.assertEqual(b7.id, 0)

        # Test with large id
        b8 = Base(1000000)
        self.assertEqual(b8.id, 1000000)

        # Test with string id
        b9 = Base("100")
        self.assertEqual(b9.id, "100")

        # Test with None id after setting id
        b10 = Base()
        self.assertEqual(b10.id, 1)

    def test_save_to_file(self):
        """Test the save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(
                content,
                '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},'
                ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
                )

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_from_json_string(self):
        """Test the from_json_string method."""
        json_str = (
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},'
                ' {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
                )
        json_list = Base.from_json_string(json_str)
        self.assertEqual(
                json_list,
                [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                    {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]
                )

        json_str_empty = '[]'
        json_list_empty = Base.from_json_string(json_str_empty)
        self.assertEqual(json_list_empty, [])

        json_str_none = None
        json_list_none = Base.from_json_string(json_str_none)
        self.assertEqual(json_list_none, [])

    def test_create(self):
        """Test the create method."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

        s1 = Square(3, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        """Test the load_from_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual([r.to_dictionary() for r in list_rectangles_input],
                         [r.to_dictionary() for r in list_rectangles_output])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual([s.to_dictionary() for s in list_squares_input],
                         [s.to_dictionary() for s in list_squares_output])

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_load_from_file_csv(self):
        """Test the save_to_file_csv and load_from_file_csv methods."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual([r.to_dictionary() for r in list_rectangles_input],
                         [r.to_dictionary() for r in list_rectangles_output])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual([s.to_dictionary() for s in list_squares_input],
                         [s.to_dictionary() for s in list_squares_output])

        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")


if __name__ == "__main__":
    unittest.main()
