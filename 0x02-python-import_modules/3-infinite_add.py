#!/usr/bin/python3


if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    arguments = sys.argv
    arguments.remove(arguments[0])
    total = 0
    for a in range(len(arguments)):
        total += int(arguments[a])
    print("{}".format(total))
