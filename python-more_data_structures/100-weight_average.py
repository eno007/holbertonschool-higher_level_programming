#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    avg = 0
    weight = 0
    for elem in my_list:
        avg += elem[0] * elem[1]
        weight += elem[1]
    return (avg / weight)
