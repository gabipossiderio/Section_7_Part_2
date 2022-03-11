import random

matrix_lines = 3
matrix_columns = 3
matrix = []

print('Enter 9 numbers to form a 3 x 3 matrix: \n')

for line in range(matrix_lines):
    child_list = []
    for column in range(matrix_columns):
        child_list.append(int(input(f'Number line {line + 1}/ column {column + 1}: ')))
    matrix.append(child_list)

print('\nThe matrix typed was:\n')

for i in matrix:
    print(i)

sum_list = [sum(idx) for idx in zip(*matrix)]

print(f'\nThe list with the sum of each column of the matrix typed is: {sum_list}')
