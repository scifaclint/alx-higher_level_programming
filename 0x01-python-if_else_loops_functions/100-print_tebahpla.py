#!/usr/bin/python3


current_char = 'z'

for i in range(122, 64, -1):

    print(f"{current_char}", end="")

    current_char = current_char.swapcase()

print("Y", end="")
