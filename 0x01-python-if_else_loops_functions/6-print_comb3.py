#!/usr/bin/python3
a = 1
for x in range(0,9):
    y = a
    while y < 10:
        if x < 8 or y < 9:
            print(f"{x}{y}, ", end='')
        else:
            print(f"{x}{y}")
        y += 1
    a += 1
