#!/usr/bin/python3
"""Task 5"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """Public instance method"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Public instance method that checks value"""
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
