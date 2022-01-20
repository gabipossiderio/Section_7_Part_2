import random

matrix = []
count = 0

for i in range(4):
    child_list = []
    for g in range(4):
        generated_number = (random.randrange(0, 20))
        child_list.append(generated_number)
        if generated_number > 10:
            count += 1
    matrix.append(child_list)

print(f'Here is the 4x4 matrix with 16 numbers: {matrix}. \nThis matrix has {count} numbers greater than 10.')
