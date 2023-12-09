#!/usr/bin/python3
"""
    This script returns type of data type and more
"""
import json


def from_json_string(my_str):
    """
    This function returns the type of data type and more

    Args:
        my_str (_type_): _description_ takes the data.
    Returns:
        dict: python object 
    """
    return json.load(my_str)
