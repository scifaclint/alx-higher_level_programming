#!/usr/bin/python3

# function to return object

def lookup(obj):
    """looks up for an object

    Args:
        obj (any): returns available atrributes
    Returns:
        List of attributes
    """
    return (dir(obj))
