#!/usr/bin/python3
import sys


def getargv(list):
    list.remove(list[0])
    if len(list) == 0:
        print("{} arguments.".format(len(list)))
    else:
        if len(list) == 1:
            print("{} argument:".format(len(list)))
            print("1: {}".format(list[0]))
        if len(list) > 1:
            print("{} arguments:".format(len(list)))
            a = 0
            b = 1
            while a < len(list):
                print("{}: {}".format(b, list[a]))
                b += 1
                a += 1


getargv(sys.argv)
