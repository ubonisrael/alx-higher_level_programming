#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for i in str:
        x = ord(i)
        if x >= 97 and x <= 122:
            x -= 32
        print("{:c}".format(x), end='')
    print("{:c}".format(10), end='')
