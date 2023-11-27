#!/usr/bin/python3
""" Contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ Divides all the elements of 'matrix' by 'div' and
    returns a new matrix containing the results.
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if len(matrix) == 0:
        raise TypeError\
            ('matrix must be a matrix (list of lists) of integers/floats')
    row_size = None
    new_matrix = []
    for x in matrix:
        if not isinstance(x, list) or len(x) == 0:
            raise TypeError\
                ('matrix must be a matrix (list of lists) of integers/floats')
        count = 0
        mat = []
        for y in x:
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError\
                    ('matrix must be a matrix (list of lists) of integers/floats')
            mat.append(round(y/div, 2))
            count += 1
        if row_size is None:
            row_size = count
        if row_size != count:
            raise TypeError('Each row of the matrix must have the same size')
        new_matrix.append(mat)

    return new_matrix
