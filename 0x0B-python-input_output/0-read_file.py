#!/usr/bin/python3
def read_file(filename=""):
    """funtion to read to output

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(f"{filename}", "r") as file:
        print(file.read())
