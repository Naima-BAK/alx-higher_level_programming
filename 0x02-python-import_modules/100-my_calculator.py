#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    arg1 = int(sys.argv[1])
    operator = sys.argv[2]
    arg2 = int(sys.argv[3])

    if operator == '+':
        print("{} {} {} = {}".format(arg1, operator,arg2, add(arg1,arg2)))
    elif operator == '-':
        print("{} {} {} = {}".format(arg1, operator,arg2, sub(arg1,arg2)))
    elif operator == '*':
        print("{} {} {} = {}".format(arg1, operator,arg2, mul(arg1,arg2)))
    elif operator == '/':
        print("{} {} {} = {}".format(arg1, operator,arg2, div(arg1,arg2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
