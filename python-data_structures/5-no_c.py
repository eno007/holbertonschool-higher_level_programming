#!/usr/bin/python3
def no_c(my_string):
    our_string = ""
    for el in my_string:
        if (el != "c" and el != "C"):
            our_string += el
    return our_string
