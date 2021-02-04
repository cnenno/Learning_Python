#!/usr/bin/env python3

print("gas mileage calc yo")

firstfill = int(input("odometer at fill up time 1: "))

secondfill = int(input("odometer at fill up time 2: "))

gallons = float(input("gallons filled: "))

milesdriven = secondfill - firstfill

mpg = milesdriven / gallons

print(mpg, "miles per gallons")

