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
        None
    """
    with open(filename, "r") as file:
        data = json.load(file)
