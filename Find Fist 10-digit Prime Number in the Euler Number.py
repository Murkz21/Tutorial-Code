import math as mt
from decimal import Decimal as dec
from collections import deque as dq

eulerNumber = mt.e
# print('%1.60f'%e)                                   # Only 52 digits can be show in math.
eulerDigit = dec(eulerNumber * 10**51)                # Translate the Euler number string into an integer number.
eulerString = str(eulerDigit)

def tenEulerNum(DigitString):
    tenString = DigitString[0:10]
    tenDigitNum = int(tenString)
    return tenDigitNum

def checkIsPrime(num):                                # Intuitive one, not the one with the best performance..
    if num > 1:
        for i in range(2, num//2 + 1):
            if 0 == (num % i):
                break                                 # This is not a prime number.
        else:
            print('Bingo!\nThe number is: {}'.format(num))
            return True
    else:
        raise ValueError('Need a valid input.')

def main(string):
    for i in range(0, 51):
        if checkIsPrime(tenEulerNum(string)) == True:
            break
        stringDQ = dq(string)
        stringDQ.rotate(-1)                          # roate the string to the left by 1 step.
        string = ''.join(stringDQ)
    else:
        print('Not found!')

findTenEulerDigit_PrimeNum = main(eulerString)

# BTW, the number shoud be 5762718281, and it took my PC ~13 mins to figue out...
