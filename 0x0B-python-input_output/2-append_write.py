#!/usr/bin/python3
"""
    This writes and appends to existing file
"""


def append_write(filename="", text=""):
    """
        This function appends and writes to an existing file

        Args:
            filename (str, optional): _description_. Defaults to "".
            text (str, optional): _description_. Defaults to "".
        Returns:
            int: number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
