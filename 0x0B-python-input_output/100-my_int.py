#!/usr/bin/python3
"""
Module with a class Myint
"""


class MyInt(int):
    """
    A class MyInt that inherits from int and has == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Overrides the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.
        """
        return super().__eq__(other)
