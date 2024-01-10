#!/usr/bin/python3
"""
This module contains a function that returns an object
(Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Function to return an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to an object.

    Returns:
        The object represented by `my_str`.
    """
    return json.loads(my_str)
