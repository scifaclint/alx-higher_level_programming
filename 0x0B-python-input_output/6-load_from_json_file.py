#!/usr/bin/python3
"""
    This loads json file and places its 
    as a python dictionary
"""


def load_from_json_file(filename):
    """
    Creates python dictionary from a 
    json file.

    Args:
        filename (any): should be a json file.
    Return:
        The object representation of data
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
