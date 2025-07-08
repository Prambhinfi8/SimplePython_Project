print("Welcome to the Average_Height Program!!!")
student_height=input("input list of student height:").split()
total_height=0
for height in student_height:
    total_height += int(height)
print(f"total_height is {total_height}")

number_of_student=0
for student in student_height:
    number_of_student +=1
print(f"number of student is {number_of_student}")
average=total_height/len(student_height)
print(f"average is {average}")

# print("welcome with other methos")
#
# student_height=input("enter you student height:").split()
# for n in range(0, len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)
# print(sum(student_height))
# print(len(student_height))