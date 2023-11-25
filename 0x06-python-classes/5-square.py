#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A square with a size, a method to calculate its area,
        and a method to print it.
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

    def my_print(self):
        """Print the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
