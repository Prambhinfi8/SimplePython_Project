print("Welcome to The Roller_Coster Program...")
height=float(input("enter your heightin meter:"))
bill=0
if height>=200:
    print("you can ride in to the Roller_Coster.")
    age=int(input("enter your age:"))
    if age<=12:
        bill +=5
        print("you should pay 5Rs.")
    elif age>=12 and age<=18:
        bill=7
        print("you should pay 7Rs.")
    elif age>=45 and age<=55:
        print("free for your age person!!!❤️❤️❤️")
    else :
        bill=12
        print("you should pay 12Rs.")
    want_photo=input("you want to take photo in the Roller_Coster? Y or N :")
    if want_photo=="Y" and want_photo=="yes":
        bill=bill+3
        print(f"Your final bill is {bill}")

else:
    print("Sorry,You can't Ride in The Roller_Coster.😒😒")
