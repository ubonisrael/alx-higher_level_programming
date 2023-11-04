#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        a = 0
        for y in x:
            print("{:d}".format(y), end=' ' if a < len(x) - 1 else '')
            a += 1
        print()
