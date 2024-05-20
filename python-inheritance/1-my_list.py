#!/usr/bin/python3
"""
class mylist inherits from list
"""
class MyList(list):
    """
    type class MyList
    """
    def print_sorted(self):
        """
        prints in ascending order
        """
        print (sorted(self))