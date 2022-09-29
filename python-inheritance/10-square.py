#!/usr/bin/python3
"""Module for Rectangle class"""


Rectangle = __import__('9-rectange').Rectangle


class Square(Rectangle):
    """Class Square that inherits from 'Rectangle'"""
    def __init__(self, size):
        """Instantiation with private attributes"""
        self.intiger_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Function to return area of square"""
        return (self.__size ** 2)
