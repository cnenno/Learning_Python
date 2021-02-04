

#!/usr/bin/env python3




class Hero(object):
    def __init__(self, name="Hero", position="00",
        health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.max_health = health #trust me, you want to have this as well
        self.health = health 
        self.damage = damage
        self.experience = experience

def starting_mark(height):
    return round(9.45 + (10.67 - 9.45) / (1.83 - 1.52) * (height - 1.52), 2)



substract days and compare to prove period 
def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length

import datetime
def period_is_late(last,today,c):
    d = (today - last).days
    return d > c 
   
