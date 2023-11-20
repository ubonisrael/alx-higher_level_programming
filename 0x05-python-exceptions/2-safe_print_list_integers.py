#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    tracker = 0
    while counter < x:
        try:
            print("{:d}".format(my_list[counter]), end="")
            tracker += 1
        except (ValueError, TypeError):
            counter += 1
            continue
        counter += 1
    print()
    return tracker
