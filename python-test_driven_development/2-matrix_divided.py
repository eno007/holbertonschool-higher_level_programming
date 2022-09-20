#!/usr/bin/python3
"""Matrix_divided function"""


def matrix_divided(matrix, div):
    """Returns the sum of a + b"""

    if len({len(list) for list in matrix}) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    for list in matrix:
        for el in list:
            if type(el) is float:
                el = int(el)
            elif type(el) is not int:
                raise TypeError('matrix must be a matrix 
                        (list of lists) of integers/floats')
    if type(div) is float:
        div = int(div)
    if type(div) is not int:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[float("{:.2f}".format(el/div)) for el in list] for list in matrix]
