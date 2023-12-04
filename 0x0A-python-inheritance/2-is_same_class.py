#!/usr/bin/python3
""" Contains the is_same_class function. """


def is_same_class(obj, a_class):
    """ Returns if 'obj' is an exactly instance of 'a_class'"""
    return type(obj) == a_class
