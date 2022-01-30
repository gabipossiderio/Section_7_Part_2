matrix = []

for i in range(4):
    child_list = []
    for g in range(4):
        if g == i:
            child_list.append(1)
        else:
            child_list.append(0)
    matrix.append(child_list)

print(f"The generated matrix is:")

for i in matrix:
    print(i)
