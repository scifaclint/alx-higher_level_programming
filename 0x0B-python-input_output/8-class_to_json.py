#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Function to return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj: The object to convert to a dictionary.

    Returns:
        dict: The dictionary representation of `obj`.
    """
    return obj.__dict__
