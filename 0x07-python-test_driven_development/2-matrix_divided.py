#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a number.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The number to divide by.

    Returns:
    list of lists of int/float: The divided matrix.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats,
               if each row of the matrix does not have the same size,
               or if div is not a number.
    ZeroDivisionError: If div is 0.
    """

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
