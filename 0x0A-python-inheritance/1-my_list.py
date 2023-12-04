#!/usr/bin/python3
""" COntains a class that inherits from list. """


class MyList(list):
    """ Inherits from list and prints a sorted list. """

    def print_sorted(self):
        """ Prints a sorted list. """
        print(sorted(self))
