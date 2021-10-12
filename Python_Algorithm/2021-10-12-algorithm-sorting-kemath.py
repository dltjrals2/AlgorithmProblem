student_number = int(input())
student_list = []

for _ in range(student_number):
    input_data = input().split()
    student_list.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

student_list = sorted(student_list, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for student in student_list:
    print(student[0])
