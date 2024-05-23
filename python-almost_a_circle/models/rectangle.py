#!/usr/bin/python3
"""
Class rectangle that inherits from Base
"""

from base import Base

class Rectangle(Base):
    """
    Rectangle Class inheriting from Base
    """
    def __init__ (self, width, height, x=0, y=0, id=None):
        """
        Init class with seom attr
        """
        super().__init__(id)
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y



if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)