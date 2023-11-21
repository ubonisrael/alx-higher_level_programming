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

    def my_print(self):
        """ Prints the square to stdout using the hash character. """
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print()

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
