#!/usr/bin/python3
"""This module contains and does 
   a whole lot on the object here
"""

def lookup(obj):
    """looks up for an object

    Args:
        obj (any): returns available atrributes
    Returns:
        List of attributes
    """
    return (dir(obj))
