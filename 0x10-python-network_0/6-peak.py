#!/usr/bin/python3
"""Finds the peak in an array"""


def find_peak(list_of_integers):
    """Finds the peak in an array"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    
    if list_of_integers[size - 1] > list_of_integers[size - 2]:
        return list_of_integers[size - 1]

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    if list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid + 1:])