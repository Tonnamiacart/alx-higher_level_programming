#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[0:2]
    b = tuple_b[0:2]

    a += (0,) * (2 - len(a))
    b += (0,) * (2 - len(b))

    solution = (a[0] + b[0], a[1] + b[1]
    return solution
