#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
            x = chr(ord(x) - 32)
        print("{:s}".format(x), end="")
    print("")
