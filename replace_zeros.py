
#You are given a decimal number n as a string. Transform it into an array of numbers (given as strings again), such that each number has only one nonzero digit and their sum equals n.

#Each number in the output array should be written without any leading and trailing zeros.
#Input/Output
#    [input] string n
#    A non-negative number.
#    1 ≤ n.length ≤ 30.
#    [output] a string array
#    Elements in the array should be sorted in descending order.

#Example
#For n = "7970521.5544" the output should be:
# ["7000000", 
# "900000", 
# "70000", 
# "500", 
# "20", 
# "1", 
# ".5",
# ".05",
# ".004",
# ".0004"]


#!/usr/bin/env python3
#solutions
def split_exp(n):
    dot = n.find('.')
    if dot == -1: dot = len(n)
    return [d+"0"*(dot-i-1) if i<dot else ".{}{}".format("0"*(i-dot-1), d)
            for i,d in enumerate(n) if i != dot and d != '0']


def split_exp(n):
  try:
      dot = n.index('.')
  except:
      dot = len(n)
  return [n[i]+'0'*(dot-1-i) for i in range(dot) if n[i] != '0'] +\
          ['.' + '0'*(i-dot-1) + n[i] for i in range(dot+1,len(n)) if n[i] != '0']



