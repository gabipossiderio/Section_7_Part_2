matrix_lines = 5
matrix_columns = 3
matrix = []
students_grade_dict = {}

print('\nPlease enter your details correctly.\n'
      '\nNumber 1 (Registration number - use an integer -);'
      '\nNumber 2 (Average of the tests);'
      '\nNumber 3 (Average of works);\n')

for line in range(matrix_lines):
    students_info_list = []
    for column in range(matrix_columns):
        students_info_list.append(int(input(f'Number {column + 1} of Student {line + 1}: ')))
    grade_sum = students_info_list[1] + students_info_list[2]
    students_grade_dict[students_info_list[0]] = grade_sum
    students_info_list.append(grade_sum)
    matrix.append(students_info_list)
    print('\nCongratulations! You have inputted your details correctly.\n'
          f'\nSTUDENT {line + 2}\n')

print('\nThe data inputted were:\n')

for i in matrix:
    print(i)

student_highest_grade = max(students_grade_dict, key=students_grade_dict.get)

print(f'\nThe student with the highest final grade has the registration number {student_highest_grade}.'
      f'\nThe arithmetic mean of the final grades is {(sum(students_grade_dict.values())) / 5}.')
