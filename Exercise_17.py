import random

matrix_lines = 10
matrix_columns = 3
matrix = []
worst_grades_exam_1 = 0
worst_grades_exam_2 = 0
worst_grades_exam_3 = 0

for line in range(matrix_lines):
    child_list = []
    for column in range(matrix_columns):
        child_list.append(random.randrange(1, 10))
    matrix.append(child_list)
    if child_list.index(min(child_list)) == 0:
        worst_grades_exam_1 += 1
    elif child_list.index(min(child_list)) == 1:
        worst_grades_exam_2 += 1
    else:
        worst_grades_exam_3 += 1

print("STUDENTS' RESULTS\n")

for index, value in enumerate(matrix):
    print(f'Student {index + 1}: {value}')

print(f'\n{worst_grades_exam_1} students had the worst grade on test 1.')
print(f'{worst_grades_exam_2} students had the worst grade on test 2.')
print(f'{worst_grades_exam_3} students had the worst grade on test 3.')
