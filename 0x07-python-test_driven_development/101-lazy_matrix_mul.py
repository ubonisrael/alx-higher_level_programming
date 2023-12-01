#!/usr/bin/python3
""" Contains a funcction that multiplies
2 matrices.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices using numpy and returns the result. """

    return np.matmul(m_a, m_b)
