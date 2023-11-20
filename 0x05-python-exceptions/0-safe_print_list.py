#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for a in my_list:
        try:
            if counter == x:
                break
            print("{}".format(a), end="")
            counter += 1
        except IndexError:
            print("Index not found")
    print()
    return counter
