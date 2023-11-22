#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
