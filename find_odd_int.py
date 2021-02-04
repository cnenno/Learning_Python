#!/usr/bin/env python3


#my solution
def find_it(seq):
    for elem in set(seq):
        if seq.count(elem) % 2 == 1:
            return elem


#similar 0 solution
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

#func
import operator
import functools
def find_it(xs):
    return functools.reduce(operator.xor, xs)
    
#def find_it(xs):
#    return functools.reduce(lambda x,y: x ^ y, xs)
