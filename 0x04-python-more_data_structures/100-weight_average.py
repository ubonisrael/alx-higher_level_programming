#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    summation = 0
    for x in list(map(lambda x: x[0] * x[1], my_list)):
        summation += x
    total = 0
    for y in list(map(lambda x: x[1], my_list)):
        total += y
    return summation / total
