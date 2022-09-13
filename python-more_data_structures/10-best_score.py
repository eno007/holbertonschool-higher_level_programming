#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    max_key = ""
    if a_dictionary:
        for keys in a_dictionary.keys():
            if max_score < a_dictionary[keys]:
                max_score = a_dictionary[keys]
                max_key = keys
        return (max_key)
    return None
