#!/usr/bin/python3
""" class to define a rectangle class """


class Rectangle():
    """ instances and rest defined here """

    def __init__(self, height=0, width=0):
        """create private instances """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ retrieve width value """
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
