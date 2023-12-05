#!/usr/bin/python3
"""Contains the pascal_triangle function and its helper functions. """


def fac(n=0):
    """ Finds and returns the factorial of a number. """
    if n < 0:
        return None
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * fac(n-1)


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle
    of n.
    """
    t_list = []
    if n <= 0:
        return t_list
    i = 0
    while i < n:
        inner_list = []
        for x in range(0, i+1):
            inner_list.append(fac(i)//(fac(x) * fac(i-x)))
        t_list.append(inner_list)
        i += 1
    return t_list
