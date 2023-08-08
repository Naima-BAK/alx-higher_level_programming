#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    lastd = (num * -1) % 10
    lastd *= -1
else:
    lastd = num % 10
if lastd > 5:
    result = f"and is greater than 5"
elif lastd == 0:
    result = f"and is 0"
else:
    result = f"and is less than 6 and not 0"

print(f"Last digit of {num:d} is {lastd:d} {result}")
