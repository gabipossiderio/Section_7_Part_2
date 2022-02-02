import random

matrix_size = 3
matrix = []

for line in range(matrix_size):
    child_list = []
    for column in range(matrix_size):
        child_list.append(random.randint(1, 20))
    matrix.append(child_list)

print('The generated matrix is:\n')

for i in matrix:
    print(i)

for line in range(len(matrix)):
    for column in range(len(matrix)):
        if line < column:
            matrix[line][column] = 0

print('\nHere is the previous matrix transformed into a lower triangular matrix:\n')

for i in matrix:
    print(i)
