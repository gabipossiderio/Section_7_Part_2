import random

matrix_size = 5
matrix = []

for line in range(matrix_size):
    child_list = []
    for column in range(matrix_size):
        child_list.append(*random.sample(range(0, 99), 1))
    matrix.append(child_list)

print('*' * 10)
print('BINGO CARD')
print('*' * 10, '\n')

for i in matrix:
    print(i)
