#!/usr/bin/python3
"""Text_indentation function"""


def text_indentation(text):
    """Prints indentation text"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    symbols = [".", "?", ":"]
        new_str = ""
        for i in range(len(text)):
            if text[i] == " " and flag == 1:
                continue
            flag = 0
            new_str += text[i]
            if text[i] in symbols:
                new_str += "\n" + "\n"
                flag = 1
        print(new_str, end="")
