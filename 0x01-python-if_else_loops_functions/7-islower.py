#!/usr/bin/python3
def islower(c):
    """checks for a lowercase character"""
    char = ord(c)
    if char >= 97 and char <= 122:
        return True
    return False
