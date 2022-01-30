matrix = []

for i in range(1, 5):
    child_list = []
    for g in range(1, 5):
        child_list.append(i * g)
    matrix.append(child_list)

print(f"The generated matrix is:")

for i in matrix:
    print(i)
