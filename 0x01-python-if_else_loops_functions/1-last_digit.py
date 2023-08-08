#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
lastDigit = (num * -1) % 10
if num == 0:
 print(f'lastDigit digit of {num} is {lastDigit} and is 0')
   
elif num > 5:
    print(f'lastDigit digit of {num} is {lastDigit} and is greater than 5')
else:
    print(f'lastDigit digit of {num} is -{lastDigit} and is less than 6 and not 0')
