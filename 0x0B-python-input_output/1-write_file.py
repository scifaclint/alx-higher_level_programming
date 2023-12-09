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
        text (str): The text to write to the file. Defaults to "".
    Returns:
        int:number of characters
    """
    with open(f"{filename}", "w", encoding="utf-8") as file:
        return file.write(text)
