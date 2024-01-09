#!/usr/bin/python3
"""Function to write to a file"""


def write_file(filename="", text=""):
    """
    This function writes a text to a file

    Args:
        filename (str, optional): File name to write str to "".
        text (str, optional): text or string to write to file "".
    Return:
        Number of characters written to file.
    """
    with open(filename, "w", encoding="UTF8") as filed:
        return filed.write(text)
