#!/usr/bin/env python3

a = [4, 5, 6]
b = [1, 2, 3]
x = [1, 2, 3]
y = [4, 5, 6]


def array_madness(a,b):
#    return sum(x ** 2 for x in a) > sum(x **3 for x in b)
    print(sum(x ** 2 for x in a) > sum(x ** 3 for x in b))

array_madness(a,b)
array_madness(x,y)
