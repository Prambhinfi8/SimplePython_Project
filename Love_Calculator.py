print("welcome to the Love_Calculator program.!!!")
name_1=input("enter your name :\n")
name_2=input("enter your their name :\n")
combined_str = name_1+name_2
lower_case_string=combined_str.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true=t+r+u+e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love=l+o+v+e
love_score=int(str(true)+str(love))
print(love_score)
if love_score<=10 or love_score>=90:
    print(f"your love_scoer is {love_score} ,you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"your love_score is {love_score}, you are all right together.")
else:
    print(f"your love_score is {love_score}")



