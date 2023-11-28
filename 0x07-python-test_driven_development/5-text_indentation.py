#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after
    each of these characters: ., ? and :

    Parameters:
    text (str): The text to be printed.

    Raises:
    TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")), end="")
