#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end='')
    print()
