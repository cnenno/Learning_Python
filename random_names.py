#!/usr/bin/env python3
import random


class whatever:

    def __init__(self):
        self.namelist = []
        self.adjective = []

        while True:
            a = input("enter a name or q to quit: ")
            if (a == "q") or (a == "Q"):
                break
            else:
                self.namelist.append(a)

        while True:
            b = input("enter an adjective or q to quit: ")
            if (b == "q") or (b == "Q"):
                break
            else:
                self.adjective.append(b)


    def choicename(self):
        return random.choice(self.namelist)

    def choiceadj(self):
        return random.choice(self.adjective)

    def __repr__(self):
        return "{} is {}".format(self.choicename(),self.choiceadj())

x = whatever()

while True:
    print(x)
    if input("Continue?").lower() == "no":
        break

