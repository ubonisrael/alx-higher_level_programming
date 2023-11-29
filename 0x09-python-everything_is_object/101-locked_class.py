#!/usr/bin/python3
""" Contain the LockedClass class. """


class LockedClass:
    """ A class that prevents the user from dynamically creating nre instances
    except 'first_name'.
    """

    __slots__ = ['first_name']
