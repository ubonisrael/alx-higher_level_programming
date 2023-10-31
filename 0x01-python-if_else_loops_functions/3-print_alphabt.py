#!/usr/bin/python3
number = 97
while number < 123:
    print(f"{number:c}", end='')
    number += 1
    if number == 101 or number == 113:
        number += 1
