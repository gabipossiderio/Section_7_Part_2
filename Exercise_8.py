import random

matrix = []
sum_numbers = 0

for line in range(3):
    child_list = []
    for column in range(3):
        child_list.append(random.randint(10, 30))
        if line < column:
            sum_numbers += child_list[column]
    matrix.append(child_list)

print('The generated matrix is:\n')

for i in matrix:
    print(i)

print(f'\nThe sum of the numbers above the main diagonal is {sum_numbers}.')
