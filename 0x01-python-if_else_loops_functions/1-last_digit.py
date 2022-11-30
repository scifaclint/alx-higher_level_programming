#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# YOUR CODE HERE
getstra = str(number)
conumber = int(getstra[-1])
if conumber > 5:
    print("Last digit of", number, "is", conumber, "and is greater than 5")
if conumber == 0:
    print("Last digit of", number, "is", conumber, "and is 0")
if conumber < 6 and conumber != 0:
    print(
        "Last digit of",
        number,
        "is",
        conumber,
        "and is less than 6 and not 0"
    )
