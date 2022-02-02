import random

matrix_lines = 3
matrix_columns = 10
matrix = []
answer_key = []
results = []
approved_students = 0
approved_percentage = 0

for line in range(matrix_lines):
    child_list = []
    for column in range(matrix_columns):
        child_list.append(chr(random.randrange(ord('A'), ord('F'))))
    matrix.append(child_list)

for i in range(10):
    answer_key.append(chr(random.randrange(ord('A'), ord('F'))))

print('\nANSWER KEY\n')

print(answer_key)

for line in range(matrix_lines):
    hits = 0
    for column in range(matrix_columns):
        if matrix[line][column] == answer_key[column]:
            hits += 1
    if hits > 6:
        approved_students += 1
    results.append(hits)

if approved_students > 0:
    approved_percentage = (approved_students / matrix_lines) * 100

print('\nREPORT CARD\n')

for index, value in enumerate(results):
    print(f'STUDENT {index + 1} - ANSWERS: {matrix[index]} - GRADE: {float(value)}')

print(f'\nPERCENTAGE OF APPROVED STUDENTS: {approved_percentage}%')

