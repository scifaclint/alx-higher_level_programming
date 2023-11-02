#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}{}".format(chr(i), chr(i - 32) if i >= ord('a') else ''), end='')
