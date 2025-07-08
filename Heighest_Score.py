print("welcome to the Heighest score Program..")
# student_score=input("enter student score:").split()
# for n in range(0, len(student_score)):
#     student_score[n]=int(student_score[n])
# print(f"Maximum student score is {max(student_score)}")
student_score=[0,100,45,78,54,78,42]
high_score=0
lower_score=0
for score in student_score:
    if score>high_score:
        high_score=score
    if score < lower_score:
        lower_score=score
print(f"student high score is {high_score}")
print(f"student low score is {lower_score}")