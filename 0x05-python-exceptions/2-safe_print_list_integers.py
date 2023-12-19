#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    fet = 0
    for f in range(0, x):
        try:
            print("{:d}".format(my_list[f]), end="")
            fet += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (fet)
