#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = a + b
            break
    return result


dis.dis(magic_calculation)
