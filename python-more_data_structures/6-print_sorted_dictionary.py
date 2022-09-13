#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for elem in sorted(a_dictionary.keys):
        print("{} : {}", elem, a_dictionary[elem])
