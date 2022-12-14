#!/usr/bin/python3
"""This module creates class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @width.setter
    def width(self, width):
        """setter for width"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @height.setter
    def height(self, height):
        """setter for height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        """setter for x"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        """setter for y"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Calculate area value"""
        return(self.__width * self.__height)

    def display(self):
        """Displays in STDOUT rectangle with charachter '#'"""
        for y in range(self.__y):
            print('')
        for row in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for col in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Method that overrides __str__ method"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for idx in range(len(args)):
                setattr(self, attributes[idx], args[idx])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if hasattr(self, key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
