#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) < 1:
        print("{} Arguments.".format(0))
    elif len(argv) == 1:
        print("{}: Argument:".format(len(argv)))
        print("{}: {}".format(len(argv), argv[0]))
    else:
        print("{} Arguments:".format(len(argv)))
        for i, j in enumerate(argv):
            print("{}:{}".format(i+1, j))
