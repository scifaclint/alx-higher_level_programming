#!/usr/bin/python3
"""Replicates the behavior described in the given bytecode"""

import math


class MagicClass:
    """Defines a class MagicClass
    """

    def __init__(self, radius=0):
        """Initializes MagicClass with a radius
        Args:
            radius (float): Radius of Circle
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """Get/set the Circle radius
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """Calculates the area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle
        """
        return 2 * math.pi * self.__radius
