#!/usr/bin/python3
number = 97
while number < 123:
    print("{:c}".format(number), end='')
    number += 1
    if number == 101 or number == 113:
        number += 1
