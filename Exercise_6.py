import random

matrix1 = []
matrix2 = []
matrix3 = []

for line in range(1, 5):
    child_list = []
    child_list2 = []
    for column in range(1, 5):
        child_list.append(random.randrange(100, 1000))
        child_list2.append(random.randrange(100, 1000))
    matrix1.append(child_list)
    matrix2.append(child_list2)

print('The first generated matrix is:\n')

for i in matrix1:
    print(i)

print('\nThe second generated matrix is:\n')

for i in matrix2:
    print(i)

for line in range(4):
    child_list3 = []
    for column in range(4):
        if matrix1[line][column] > matrix2[line][column]:
            child_list3.append(matrix1[line][column])
        else:
            child_list3.append(matrix2[line][column])
    matrix3.append(child_list3)

print('\nThe third generated matrix with only the highest numbers of each position of the previous matrices is:\n')

for i in matrix3:
    print(i)
