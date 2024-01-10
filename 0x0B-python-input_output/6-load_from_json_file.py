#!/usr/bin/python3
"""
This module contains a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Function to create an Object from a “JSON file”.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        The object represented by the JSON string in `filename`.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
