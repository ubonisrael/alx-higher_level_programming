#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end='')
if number > 0:
    d = number % 10
else:
    d = (number * -1) % 10
if d > 5:
    print("{} and is greater than 5".format(d if number > 0 else -d))
elif d < 6 and d > 0:
    print("{} and is less than 6 and not 0".format(d if number > 0 else -d))
else:
    print(f"{last_digit} and is 0")
