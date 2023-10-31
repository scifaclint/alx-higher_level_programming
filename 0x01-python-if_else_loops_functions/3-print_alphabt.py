#!/usr/bin/python3
for char in range(ord("a"), ord("z")+1):
    if chr(char) == "e":
        pass
    elif chr(char) == "q":
        pass
    else:
        print("{}".format(chr(char)), end="")
