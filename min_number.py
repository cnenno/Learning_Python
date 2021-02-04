#!/usr/bin/env python3

a = input("enter several number: ")
b = a.split(" ")

numbers = []

for mynumber in b:
    numbers.append(int(mynumber))

print(numbers)

def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers

remove_smallest(numbers)

print(numbers)
