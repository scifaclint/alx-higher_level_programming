#!/usr/bin/python3


if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    def getargv(list):
        list.remove(list[0])
        getint = int(list[0])
        print(list)
        if len(list) == 0:
            print(len(list))
        else:
            a = 1
            while a < len(list):
                getint += int(list[a])
                a += 1
        print(getint)


getargv(sys.argv)
