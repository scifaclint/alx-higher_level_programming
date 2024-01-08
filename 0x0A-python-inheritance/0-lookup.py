#!/usr/bin/python3

# function to return object

def lookup(obj):
    """looks up for an object

    Args:
        obj (any): returns available atrributes
    """
    return (dir(obj))
