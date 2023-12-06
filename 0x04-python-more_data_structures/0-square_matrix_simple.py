#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    empty = []
    for row in matrix:
        squared_row = [num ** 2 for num in row]
        empty.append(squared_row)
    return empty
