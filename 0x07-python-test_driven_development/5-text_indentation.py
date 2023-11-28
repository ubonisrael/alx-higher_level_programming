#!/usr/bin/python3
""" Contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ prints a text with 2 new lines after
    each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    x = 0
    while x < len(text):
        print("{}".format(text[x]), end="")
        if text[x] == '.' or text[x] == '?' or text[x] == ':':
            print("\n")
            if text[x+1] == ' ':
                x += 1
        x += 1
