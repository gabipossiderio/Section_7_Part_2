import random

matrix = []
largest_number = 0
largest_number_line = 0
largest_number_column = 0

for line in range(1, 5):
    child_list = []
    for column in range(1, 5):
        generated_number = (random.randrange(100, 1000))
        child_list.append(generated_number)
        if generated_number > largest_number:
            largest_number = generated_number
            largest_number_column = column
            largest_number_line = line
    matrix.append(child_list)

print(f"The generated matrix is:\n")

for i in matrix:
    print(i)

print(f'\nThe largest number in this matrix is {largest_number}. This number is in row number '
      f'{largest_number_line} of column number {largest_number_column}.')
