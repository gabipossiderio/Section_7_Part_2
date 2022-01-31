import random

matrix = []
sum_numbers = 0

for line in range(3):
    child_list = []
    for column in range(3):
        child_list.append(random.randint(10, 30))
    matrix.append(child_list)

for i in range(len(matrix)):
    sum_numbers += matrix[i][(len(matrix) - 1) - i]

print('The generated matrix is:\n')

for i in matrix:
    print(i)

print(f'\nThe sum of the numbers that are on the secondary diagonal is {sum_numbers}.')
