import random

matrix_lines = 5
matrix_columns = 10
matrix = []
answer_key = []
results = []

for line in range(matrix_lines):
    child_list = []
    for column in range(matrix_columns):
        child_list.append(chr(random.randrange(ord('A'), ord('E'))))
    matrix.append(child_list)

for i in range(10):
    answer_key.append(chr(random.randrange(ord('A'), ord('E'))))

print('\nANSWER CARD\n')

for index, value in enumerate(matrix):
    print(f'STUDENT {index + 1} {value}')

print('\nANSWER KEY\n')

print(answer_key)

for line in range(matrix_lines):
    hits = 0
    for column in range(matrix_columns):
        if matrix[line][column] == answer_key[column]:
            hits += 1
    results.append(hits)

print('\nREPORT CARD\n')

for index, value in enumerate(results):
    print(f'STUDENT {index + 1}: {value} HITS')
