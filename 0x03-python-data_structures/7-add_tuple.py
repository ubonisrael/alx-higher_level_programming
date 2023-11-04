#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = [(tuple_a[i] if i < len(tuple_a) else 0) +
           (tuple_b[i] if i < len(tuple_b) else 0)
           for i in range(0, 2)]
    return tuple(res)
