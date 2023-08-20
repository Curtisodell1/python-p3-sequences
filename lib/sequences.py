#!/usr/bin/env python3

def print_fibonacci(length):
    list = []
    if length > 0 :
        list.append(0)
        if length > 1:
            list.append(1)
            if length > 2:
                i = 2
                while i < length:
                    list.append(
                        list[-1] + list[-2])
                    i += 1
    print(list)

    pass