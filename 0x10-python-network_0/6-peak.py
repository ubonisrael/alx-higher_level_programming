#!/usr/bin/python3
# Finds the peak in an array

def find_peak(list_of_integers):
    """Finds the peak in an array"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    return (max(list_of_integers))
