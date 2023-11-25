#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A square with a size and a method to calculate its area.
    """
    def __init__(self, size=0):
        """Initialize a new Square with a size.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area.
        """
        return self.__size * self.__size

    def __lt__(self, other):
        """Compare if the area of self is less than the area of other.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of self is less than or
        equal to the area of other.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Compare if the area of self is equal to the area of other.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if the area of self is not equal to the area of other.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if the area of self is greater than the area of other.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of self is greater than or
        equal to the area of other.
        """
        return self.area() >= other.area()
