#!/usr/bin/python3
"""
Module for the Square class, which inherits from the Rectangle class.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    Represents a square with a size, x and y positions, and an optional id.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int, optional): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the string representation of the Square instance.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """
        Updating Square with attributes
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                    self.width = arg
                    self.height = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                else:
                    break
        elif kwargs:
            for j, value in kwargs.items():
                if j == "id":
                    self.id = value
                elif j == "size":
                    self.size = value
                    self.width = value
                    self.height = value
                elif j == "x":
                    self.x = value
                elif j == "y":
                    self.y = value
                else:
                    break
