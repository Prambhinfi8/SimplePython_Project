import random
print("Welcome to The Password Generator Program..")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

bn_letter=int(input("How many letters would you like in your password?\n "))
bn_number=int(input("How many number would you like in your password?\n "))
bn_symbols=int(input("How many symbols would you like in your password?\n "))

password_list=[]
for char in range(1,bn_letter+1):
    password_list +=random.choice(letters)
for char in range(1,bn_number+1):
    password_list +=random.choice(numbers)
for char in range(1,bn_symbols+1):
    password_list +=random.choice(symbols)
print(password_list)

password=""
for char in password_list:
    password +=char
print(password)