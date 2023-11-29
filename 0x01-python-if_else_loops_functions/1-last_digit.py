#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnum = abs(number) % 10
# YOUR CODE HERE
if number < 0:
    strnum = -strnum
print(f"Last digit of {number:d} is {strnum:d} and is ", end="")
if strnum > 5:
    print("greater than 5")
elif strnum == 0:
    print("0")
else:
    print("less than 6 and not 0")
