# dice : ただのダイスロール

import random

def diceRoll(num, max):  # ex.1d6(num=1,max=6) 
    # ダイスは100個までしか振らない
    if num > 100:
        raise Exception('Dice num input Error')

    # 0面以下のダイスは振らない
    if max <= 0:
        raise Exception('Dice side input Error')
    
    sum_nummber = 0
    for i in range(num):
        sum_nummber += random.randint(1, max)
        
    return sum_nummber
    