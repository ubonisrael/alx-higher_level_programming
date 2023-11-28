#!/usr/bin/python3
""" Contains a funcction that multiplies
2 matrices.
"""


def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    row_size_a = None
    row_size_b = None

    for m in m_a:
        if not isinstance(m, list):
            raise TypeError('m_a must be a list of lists')
        if len(m) == 0:
            raise ValueError("m_a can't be empty")

        count = 0
        for n in m:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError("m_a should contain only integers or floats")
            count += 1
        if row_size_a is None:
            row_size_a = count
        if row_size_a != count:
            raise TypeError("each row of m_a must be of the same size")
    len_a = len(m_a)
    if len_a == 0:
        raise ValueError("m_a can't be empty")

    for m in m_b:
        if not isinstance(m, list):
            raise TypeError('m_b must be a list of lists')
        if len(m) == 0:
            raise ValueError("m_b can't be empty")

        count = 0
        for n in m:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError("m_b should contain only integers or floats")
            count += 1
        if row_size_b is None:
            row_size_b = count
        if row_size_b != count:
            raise TypeError("each row of m_b must be of the same size")
    len_b = len(m_b)
    if len_b == 0:
        raise TypeError("m_b can't be empty")

    if row_size_a != len_b:
        raise ValueError("m_a and m_b can't be multiplied")

    res_matrix = []
    for x in m_a:
        mat = []
        i = 0
        while i < len_b:
            sum = 0
            for y, m in enumerate(m_b):
                sum += x[0+y] * m[i]
            mat.append(sum)
            i += 1
        res_matrix.append(mat)

    return res_matrix
