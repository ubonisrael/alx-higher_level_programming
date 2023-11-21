#!/usr/bin/python3
""" This module creates a class that defines a square """


class Square:
    """ An class that defines a square object."""
    def __init__(self, size=0):
        """ Initializes the square object to a size of 'size'
         or 0 if size is not given

        """
        self.size = size

    def area(self):
        """ Computes the area of the square and returns the result. """
        return self.__size * self.__size

    @property
    def size(self):
        """ Retrieves the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the square to a new one. """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, other):
        """ Checks whether this instance is equal with another. """
        return self.__size == other.size
    def __le__(self, other):
        """ Checks whether this instance is less than or equal with another. """
        return self.__size <= other.size
    def __lt__(self, other):
        """ Checks whether this instance is less than with another. """
        return self.__size < other.size
    def __ne__(self, other):
        """ Checks whether this instance is not equal with another. """
        return self.__size != other.size
    def __gt__(self, other):
        """ Checks whether this instance is greater than another. """
        return self.__size > other.size
    def __ge__(self, other):
        """ Checks whether this instance is greater than
        or equal with another.
        """
        return self.__size >= other.size
