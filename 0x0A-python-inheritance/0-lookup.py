#!/usr/bin/python3
"""
This module contains and does 
whole lot on the object here
"""


def lookup(obj):
    """looks up for an object and list of 
       Attributes associated with an object

    Args:
        obj: Any object
    Returns:
        List of attributes
    """
    return (dir(obj))
