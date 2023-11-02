#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("{} Arguments.".format(len(argv)-1))
    elif len(argv) == 2:
        print("{}: Argument:".format(len(argv)-1))
        print("{}: {}".format(len(argv)-1, argv[1]))
    else:
        print("{} Arguments:".format(len(argv)))
        for i, j in enumerate(argv):
            print("{}:{}".format(i+1, j))
