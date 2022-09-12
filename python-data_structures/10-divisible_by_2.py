#!/usr/bin/python3
def divisible_by_2(my_list={}):
    divisible = []
    for el in my_list:
        if el % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)
    return divisible
