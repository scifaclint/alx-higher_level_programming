#!/usr/bin/python3
"""
    This writes and returns a json
"""
import json


def to_json_string(my_obj):
    """
    This returns a json representation.

    Args:
        my_obj (_type_): _description_.
    Returns:
        Str: Json representation of object.
    """
    return json.dumps(my_obj)
