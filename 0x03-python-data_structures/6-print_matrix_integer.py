#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row_matrix in matrix:
        for row_element in row_matrix:
            print("{:d}".format(row_element),
                  end="" if row_matrix[len(row_matrix)-1] == row_element else " ")
        print("".format())
