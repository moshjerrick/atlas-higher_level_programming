#!/usr/bin/python3
"""
Module for the Square class, which inherits from the Rectangle class.
"""

from model.rectangle import Rectangle

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

    def __str__(self):
        """
        Return the string representation of the Square instance.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
