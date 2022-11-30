#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# YOUR CODE HERE
getstra = str(number)
number_positive = None
numbernegative = None
if number > 0:
    number_positive = int(getstra[-1])
    if number_positive > 5:
        print("Last digit of", number, "is",
             number_positive, 
            "and is greater than 5"
        )
    if number_positive == 0:
        print("Last digit of", number, "is", number_positive, "and is 0")
    if number_positive < 6 and number_positive != 0:
        print(
            "Last digit of",
            number,
            "is",
            number_positive,
            "and is less than 6 and not 0",
        )
else:
    numbernegative = -int(getstra[-1])
    print(numbernegative)
    if numbernegative > 5:
        print("Last digit of", number, "is", numbernegative, 
            "and is less than 5"
        )
    if numbernegative == 0:
        print("Last digit of", number, "is",
            numbernegative, "and is 0"
        )
    if numbernegative < 6 and numbernegative != 0:
        print(
            "Last digit of",
            number,
            "is",
            numbernegative,
            "and is less than 6 and not 0"
        )
