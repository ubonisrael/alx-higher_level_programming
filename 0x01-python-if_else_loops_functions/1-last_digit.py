#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end='')
if number > 0:
    d = number % 10
else:
    d = (number * -1) % 10

if d == 0:
    print("{} and is 0".format(d))
elif d > 5 and number > 0:
    print("{} and is greater than 5".format(d))
else:
    print("{} and is less than 6 and not 0".format(d if number > 0 else -d))
