#!/usr/bin/env python3


#my solution
def getCount(inputStr):
    num_vowels = 0
    vowels = "aeiou"
    for x in list(inputStr):
        if x in vowels:
            num_vowels += 1
    return num_vowels

#function
def getCount(s):
    return sum(c in 'aeiou' for c in s)

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

