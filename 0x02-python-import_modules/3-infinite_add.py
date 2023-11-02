#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add_up = 0
    for i in range(1, len(argv)):
        add_up += int(argv[i])
    print("{}".format(add_up))
