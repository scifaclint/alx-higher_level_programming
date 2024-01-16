#!/usr/bin/python3
"""Module for Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.width
                )

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
