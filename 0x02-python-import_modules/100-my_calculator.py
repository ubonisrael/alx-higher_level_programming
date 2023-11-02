#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    length = len(sys.argv)
    args = sys.argv
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[1])
    b = int(args[3])
    if args[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif args[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif args[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif args[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
