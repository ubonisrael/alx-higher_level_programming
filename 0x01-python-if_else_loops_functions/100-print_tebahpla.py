#!/usr/bin/python3
number = 122
while number > 96:
    print("{:c}".format(number if number % 2 == 0 else number - 32), end='')
    number -= 1
