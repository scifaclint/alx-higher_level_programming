#!/usr/bin/python3
"""
This scripts writes 
       to a file .
"""


def write_file(filename="", text=""):
    """
    this function is to write a text

    Args:
        filename (str, optional): _description_. Defaults to "".
    Returns:
        None
    """
    with open(f"{filename}", "w", encoding="utf-8") as file:
        return file.write(text)
