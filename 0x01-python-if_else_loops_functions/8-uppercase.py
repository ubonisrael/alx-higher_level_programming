#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = ord(i)
        if x >= 'a' and x <= 'z':
            x = chr(ord(x) - ord(" "))
        print("{}".format(x), end="")
    print("")
