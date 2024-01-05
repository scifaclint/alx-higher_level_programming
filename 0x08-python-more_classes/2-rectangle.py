#!/usr/bin/python3
"""Defines a Rectangle class here """


class Rectangle:
    """A Rectangle class with width and height and more """

    def __init__(self, width=0, height=0):
        """Initialize  Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle here"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Returns the area of rectangle"""
        if self.height or self.width == 0 :
            return 0
        else:
            return self.height * self.width
    
    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width or self.height == 0 :
            return 0
        else:
            return((2 * self.height) + (2 * self.width))