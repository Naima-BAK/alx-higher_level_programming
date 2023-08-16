#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixB = []
    for row in matrix:
        matrixRow = []
        for index in row:
            matrixRow.append(index ** 2)
        matrixB.append(matrixRow)
    return matrixB
