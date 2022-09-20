#!/usr/bin/python3
"""Say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Returns name and surname"""
    if type(first_name) is not str:
        if not first_name:
            raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        if not last_name:
            raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
