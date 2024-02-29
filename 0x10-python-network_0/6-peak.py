#!/usr/bin/python3
"""Finds the peak in an array"""


def find_peak(list_of_integers):
    """Finds the peak in an array"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    left_max = find_peak(list_of_integers[:mid])
    right_max = find_peak(list_of_integers[mid + 1:])
    peak = list_of_integers[mid]
    if peak > left_max and peak > right_max:
        return peak
    if left_max > peak and left_max > right_max:
        return left_max
    return right_max
