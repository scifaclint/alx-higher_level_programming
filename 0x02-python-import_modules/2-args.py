#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    args_num = len(sys.argv) - 1
    arg = "argument"
    if args_num > 0:
        if args_num == 1:
            print("{} {}".format(args_num, arg + ":"))
        else:
            print("{} {}".format(args_num, arg + "s:"))
        for i in range(1, args_num + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print("{} {}".format(args_num, arg + "s."))
