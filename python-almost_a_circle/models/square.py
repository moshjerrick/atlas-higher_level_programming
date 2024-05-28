#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""

from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor
        """
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """
        STR time
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

