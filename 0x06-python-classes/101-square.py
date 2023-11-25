#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A square with a size, a position, a method to calculate its area,
        and a method to print it.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a size and a position.
        Args:
            size (int): The size of the new square.
            position (tuple): a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) for n in value) or \
           not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Return a string representation of the square.
        """
        if self.__size == 0:
            return ""
        else:
            return ("\n" * self.__position[1] +
                    "\n".join([" " * self.__position[0] + "#" * self.__size
                               for i in range(self.__size)]))
