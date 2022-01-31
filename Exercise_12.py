import random

matrix = []

for line in range(3):
    child_list = []
    for column in range(3):
        child_list.append(random.randint(10, 30))
    matrix.append(child_list)

print('The generated matrix is:\n')

for i in matrix:
    print(i)

transposed_matrix = list(map(list, zip(*matrix)))

print('\nThe transposed version of the previous matrix is:\n')

for i in transposed_matrix:
    print(i)
