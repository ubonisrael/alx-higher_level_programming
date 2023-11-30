#!/usr/bin/python3
""" Contains the print square function. """


def print_square(size):
    """ Prints a square with the character #. """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if size == 0:
        return
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
