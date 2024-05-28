#!/usr/bin/python3
"""
Class rectangle that inherits from Base
"""


from .base import Base


class Rectangle(Base):

    """
    Rectangle Class inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance with given attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int, optional): The identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Print the rectangle using the `#` character.
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: New attribute values in the order id, width, height, x, y.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the rectangle's dict
        """
        rec_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                  'height': self.__height, 'width': self.__width}
        return rec_dict