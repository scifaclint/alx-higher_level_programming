#!/usr/bin/python3
"""Function to read file output"""


def read_file(filename=""):
    """
    This reads file and print to stdout

    Args:
        filename (str, optional): name of the file .
    Return:
        None
    """
    with open(filename, "r", encoding="UTF8") as filed:
        output = filed.read()
        print(output,end="")
