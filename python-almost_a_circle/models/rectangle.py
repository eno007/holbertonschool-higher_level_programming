#!/usr/bin/python3
"""This module creates class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Initializes Rectangle width"""
        return(self.__width)

    @property
    def height(self):
        """Initializes Rectangle height"""
        return(self.__height)

    @property
    def x(self):
         """Initializes Rectangle x"""
         return(self.__x)

    @property
    def y(self):
         """Initializes Rectangle y"""
         return(self.__y)
