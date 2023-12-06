#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    oal = 0
    for num in my_list:
        if num not in new_list:
            oal += num
            new_list.append(num)
    return oal
