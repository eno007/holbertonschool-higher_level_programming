#!/usr/bin/python3
"""Text_indentation function"""


def text_indentation(text):
    """Prints indentation text"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    string = ''
    for el in text:
        if el in '.?:':
            string += el
            print(string.strip(' '))
            print()
            string = ''
        else:
            string += el
    print(string.strip(' '), end='')
