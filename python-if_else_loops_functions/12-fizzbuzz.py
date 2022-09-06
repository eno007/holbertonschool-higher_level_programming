#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 15 == 0):
            print("FizzBuzz", end="")
        elif (x % 3 == 0):
            print("Fizz".format(x), end="")
        elif (x % 5 == 0):
            print("Buzz".format(x), end="")
        else:
            print(x, end="")
        print(" ", end="")
