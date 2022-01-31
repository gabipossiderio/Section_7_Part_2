import random
matrix = []
informed_number_line = 0
informed_number_column = 0
count = 0

for line in range(1, 5):
    child_list = []
    for column in range(1, 5):
        generated_number = (random.randrange(0, 50))
        child_list.append(generated_number)

    matrix.append(child_list)

print(f"The generated matrix is:\n")

for i in matrix:
    print(i)

informed_number = int(input('\nPlease enter a number from 0 to 50. We will check if it is in the matrix: '))

for line in range(1, 5):
    for column in range(1, 5):
        if informed_number == matrix[line - 1][column - 1]:
            informed_number_line = line
            informed_number_column = column
            count = 1

if count > 0:
    print(f'\nYou entered the number {informed_number}.\nThis number is in row number '
          f'{informed_number_line} of column number {informed_number_column}.')

else:
    print('\nThe number entered does not appear in the matrix.')
