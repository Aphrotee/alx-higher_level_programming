#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("$")
        return
    for i in matrix:
        a = len(matrix)
        for j in range(a):
            if j != a - 1:
                print("{:d} ".format(i[j]), end="")
            else:
                print("{:d}".format(i[j]))
