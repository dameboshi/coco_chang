# dice : ただのダイスロール

import random

def diceRoll(num, max):  # ex.1d6(num=1,max=6) 
    sum_nummber = 0
    for i in range(num):
        sum_nummber += random.randint(1, max)
        
    return sum_nummber
    