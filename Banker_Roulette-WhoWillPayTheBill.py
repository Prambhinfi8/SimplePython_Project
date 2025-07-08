# str_op="Hello, from, AskPython"
# op=str_op.split(", ")
# print(op)
import random
print("Welcome to the Banker Roulette!!")
name_string=input("Give me your friend's circle name,seperated by the comma:")
name=name_string.split(", ")
print(f"{name[random.randint(0,len(name)-1)]} is going to buy meal")

# logic is
#     print(name[random.randint(0,len(name)-1])