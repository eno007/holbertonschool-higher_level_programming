#!/usr/bin/python3
"""Matrix_divided function"""


def matrix_divided(matrix, div):
    """Returns result of division of matrix by div"""
    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) ' +
                    'of integers/floats')

        if type(i) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) ' +
                'of integers/floats')
        if len(i) is not len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        if type(div) is not int and type(div) is not float:
            raise TypeError('div must be a number')

        if div is 0:
            raise ZeroDivisionError('division by zero')

        matrix_div = []

    for i in matrix:
        row = []
        for j in i:
            row.append(round(j / div, 2))
        matrix_div.append(row)
    return (matrix_div)
