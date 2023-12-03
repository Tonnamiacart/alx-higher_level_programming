#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    replit = my_list.copy()
    if idx <= -1:
        return replit
    if idx >= length:
        return length
    replit[idx] = element
    return replit
