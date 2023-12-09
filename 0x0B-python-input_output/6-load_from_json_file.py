#!/usr/bin/python3
"""
    This loads json file and places its 
    as a python dictionary
"""


def load_from_json_file(filename):
    """
    Function to create an Object from a “JSON file”.

    Args:
        filename (str): should be a json file.
    Return:
        The object representation of 'filename'.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
