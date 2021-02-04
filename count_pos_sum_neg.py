#!/usr/bin/env python3

#my solution
import math
def count_positives_sum_negatives(arr):
    pos = []
    negs = []
    if not arr:
        return arr
    for x in arr:
        if x > 0:
            pos.append(x)
    for y in arr:
        if y < 0:
            negs.append(y)
    return [len(pos), math.fsum(negs)]

#alternate list comprehension solution
def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
