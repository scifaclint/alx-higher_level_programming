#!/usr/bin/python3
"""Module for Base class."""
import json
import os
import csv
import turtle
import random


class Base:
    """Base class.

    Attributes:
        id (int): The identifier of the instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int, optional): The identifier of the instance.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', encoding="utf-8", newline='') as csvfile:
            if list_objs is not None:
                writer = csv.writer(csvfile)
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow(
                                [obj.id, obj.width, obj.height, obj.x, obj.y]
                                )
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".csv"
        list_objs = []
        if os.path.isfile(filename):
            with open(filename, 'r', encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                                "id": int(row[0]), "width": int(row[1]),
                                "height": int(row[2]), "x": int(row[3]),
                                "y": int(row[4])
                                }
                    elif cls.__name__ == "Square":
                        dictionary = {
                                "id": int(row[0]), "size": int(row[1]),
                                "x": int(row[2]), "y": int(row[3])
                                }
                    list_objs.append(cls.create(**dictionary))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares."""
        window = turtle.Screen()
        window.bgcolor("white")
        draw_turtle = turtle.Turtle()

        for rect in list_rectangles:
            draw_turtle.penup()
            draw_turtle.goto(rect.x, rect.y)
            draw_turtle.pendown()
            draw_turtle.color("black", "red")
            draw_turtle.begin_fill()
            for _ in range(2):
                draw_turtle.forward(rect.width)
                draw_turtle.right(90)
                draw_turtle.forward(rect.height)
                draw_turtle.right(90)
            draw_turtle.end_fill()

        for square in list_squares:
            draw_turtle.penup()
            draw_turtle.goto(square.x, square.y)
            draw_turtle.pendown()
            draw_turtle.color("black", "blue")
            draw_turtle.begin_fill()
            for _ in range(4):
                draw_turtle.forward(square.size)
                draw_turtle.right(90)
            draw_turtle.end_fill()

        window.exitonclick()
