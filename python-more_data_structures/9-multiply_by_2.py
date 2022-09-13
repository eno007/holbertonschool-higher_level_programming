#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied = {}
    for key in a_dictionary:
        multiplied[key] = (a_dictionary[key] * 2)
    return (multiplied)
