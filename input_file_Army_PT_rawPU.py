#!/usr/bin/env python3


#file = open("Army_PT_Test2file.txt", "r")

with open("Army_PT_Test2file.txt", "r") as file:
    data = file.readlines()

    for line in data:
        words = line.split()


    rawpushup = words[6]
    rawpushup = int(rawpushup)
print(rawpushup)
print(type(rawpushup))


#file.close
