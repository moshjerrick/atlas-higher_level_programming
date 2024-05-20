#!/usr/bin/python3
"""
class mylist inherits from list
"""
class MyList(list):

    """Class that extends `list`"""
    def print_sorted(self):
        """
        prints in ascending order
        """
        print (sorted(self))