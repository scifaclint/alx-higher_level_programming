#!/usr/bin/python3
"""
This module contains a class BaseGeometry with public instance
methods area and integer_validator.
"""


class BaseGeometry:
    """
    A class BaseGeometry with public instance methods area and
    integer_validator.
    """

    def area(self):
        """
        Public instance method that raises an Exception with
        the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value.

        Args:
            name (str): The name.
            value (int): The value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))
        if value is None:
            raise TypeError("{} must be an integer".format(name))
        if type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
