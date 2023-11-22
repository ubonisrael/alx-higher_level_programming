#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    x = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return result
    length = len(roman_string)
    cpy = roman_string
    while x < length:
        if cpy[x] == 'M':
            result += 1000
        elif cpy[x] == 'D':
            result += 500
        elif cpy[x] == 'C' and x + 1 < length and cpy[x + 1] == 'M':
            result += 900
            x += 1
        elif cpy[x] == 'C' and x + 1 < length and cpy[x + 1] == 'D':
            result += 400
            x += 1
        elif cpy[x] == 'C':
            result += 100
        elif cpy[x] == 'L':
            result += 50
        elif cpy[x] == 'X' and x + 1 < length and cpy[x + 1] == 'C':
            result += 90
            x += 1
        elif cpy[x] == 'X' and x + 1 < length and cpy[x + 1] == 'L':
            result += 40
            x += 1
        elif cpy[x] == 'X':
            result += 10
        elif cpy[x] == 'V':
            result += 5
        elif cpy[x] == 'I' and x + 1 < length and cpy[x + 1] == 'X':
            result += 9
            x += 1
        elif cpy[x] == 'I' and x + 1 < length and cpy[x + 1] == 'V':
            result += 4
            x += 1
        elif cpy[x] == 'I':
            result += 1

        x += 1

    return result
