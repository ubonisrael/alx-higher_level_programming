#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        a = []
        for y in x:
            a.append(y**2)
        new_matrix.append(a)
    return new_matrix
