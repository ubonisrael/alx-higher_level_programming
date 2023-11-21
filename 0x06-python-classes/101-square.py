#!/usr/bin/python3
""" This module creates a class that defines a square """


class Square:
    """ An class that defines a square object."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the square object to a size of 'size'
         or 0 if size is not given

        """
        self.size = size
        self.position = position

    def area(self):
        """ Computes the area of the square and returns the result. """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square to stdout with the hash character. """
        tracker = 0
        if self.__size == 0:
            print()
        else:
            for new_line in range(self.__position[1]):
                print()
            for x in range(0, self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for y in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """ Retrieves the size of the square. """
        return self.__size

    @property
    def position(self):
        """ Retrieves the position of the square. """
        return self.__position

    @size.setter
    def size(self, value):
        """ Sets the size of the square to a new one. """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        """ Sets the position of the square to a new one. """
        if isinstance(value, tuple) and len(value) == 2 and \
           isinstance(value[0], int) and isinstance(value[1], int)\
           and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def __str__(self):
        """ Used to make the Square class when printed
        call the my_print function.
        """
        self.my_print()
        return ""
