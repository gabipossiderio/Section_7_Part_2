matrix = []

for i in range(10):
    matrix_line = []

    for j in range(10):
        if i < j:
            matrix_line.append(2 * i + 7 * j - 2)
        elif i == j:
            matrix_line.append(3 * i * i - 1)
        else:
            matrix_line.append(4 * i * i * i - 5 * j * j - 1)

    matrix.append(matrix_line)

print('The generated matrix is:\n')
for line in matrix:
    print(line)
