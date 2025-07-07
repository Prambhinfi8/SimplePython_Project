height=float(input("enter your height in cm: "))
weight=float(input("enter yuor weight in kg: "))
bmi=round(weight/height**2)
if bmi<18.5:
    print(f"your are underweight and your weight is {bmi}")
elif bmi>18.5 and bmi<25:
    print(f"your are normal and your weight is {bmi}")
elif bmi>25 and bmi<30:
    print(f"your are overweight and your weight is {bmi}")
elif bmi>30 and bmi<35:
    print(f"your are obse and your weight is {bmi}")
elif bmi>35 :
    print(f"you are clincally obse and your weight is {bmi}")
else:
    print("please enter a valid entry.!!")