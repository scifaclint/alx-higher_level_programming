#!/usr/bin/python3
"""
    This scripts writes an object
    to a file in a json form
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function saves an object to a json file

    Args:
        my_obj (object ): _description_ an object data.
        filename (any): _description_ any.
    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
