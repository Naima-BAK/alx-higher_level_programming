#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
lastDigit = abs(num) % 10
if num > 5:
    print(f'Last digit of {num} is {lastDigit} and is greater than 5')
elif num == 0:
    print(f'Last digit of {num} is {lastDigit} and is 0')
else:
    print(f'Last digit of {num} is -{lastDigit} and is less than 6 and not 0')
