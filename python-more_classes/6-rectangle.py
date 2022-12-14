#!/usr/bin/python3
"""Function that will print a rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    """Counts number of instances"""

    def __init__(self, width=0, height=0):
        """Initialize data"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width property"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width property setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Height property"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height property setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area public instance method"""
        return (self.height * self.width)

    def perimeter(self):
        """Perimeter public instance method"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.height + self.width) * 2)

    def __str__(self):
        """Return str with character '#'"""
        string = ''
        if self.width > 0 and self.height > 0:
            for height in range(self.__height):
                for width in range(self.__width):
                    string += '#'
                string += '\n'
        return (string[: -1])

    def __repr__(self):
        """Return string representation of rectangle to recreate new one"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints 'Bye rectangle...' when instance of Rectangle is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
