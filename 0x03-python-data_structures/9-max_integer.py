#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    ola = my_list[0]
    for num in my_list:
        if num > ola:
            ola = num
    return ola
