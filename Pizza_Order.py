print("Welcome To the Pizza_Order Program...")
size=input("what size do you want pizza? S , M ,L")
add_pepperoni=input("add pepperoni? Y or N :")
extra_cheese=input("do you want extra  to cheess? Y or N :")
bill=0

if size=="S":
    bill +=15
elif size=="M":
    bill +=20
elif size=="L":
    bill +=30
else:
    print("please enter a valid size")
if add_pepperoni=="Y":
    if size=="S":
        bill +=2
    if size=="M":
        bill +=3
if extra_cheese=="Y":
    bill +=1
print(f"Your final bill is {bill}")

