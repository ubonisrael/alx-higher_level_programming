#!/usr/bin/python3
""" This module creates a class that defines a square """


class Square:
    """ An class that defines a square object."""
    def __init__(self, size=0):
        """ Initializes the square object to a size of 'size'
         or 0 if size is not given

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
