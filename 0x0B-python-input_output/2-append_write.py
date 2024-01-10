#!/usr/bin/python3
"""Funtion to append text to an existing file"""


def append_write(filename="", text=""):
    """
    This function appends the given text to the end of a specified file.

    Args:
        filename (str, optional): name of file to append text to.  "".
        text (str, optional): text or string to append to the file. "".
    Return:
        Returns number of characters added 
    """
    with open(filename, "a", encoding="UTF8") as filed:
        return filed.write(text)
