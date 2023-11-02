#!/usr/bin/python3
for i in range(26):

    print(chr(122 - i).swapcase() if i % 2 == 0 else chr(122 - i), end="")
