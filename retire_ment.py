#!/usr/bin/env python3

def calculate_retirement(yearly_deposit, min_target_balance):
    mydict = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0
    }
    balance = 0
    print(balance)
    for i in range(1,7):
        balance = 0
        while balance < min_target_balance:
            balance += yearly_deposit
            balance += balance*(i / 100)
            mydict[i] += 1
            print(balance)
    return mydict
