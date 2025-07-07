# ============================ Tip Calculator=========================
# # print("hello Welcome to tip calculator")
# # bill=float(input("enter your bill amount: "))
# # tip=float(input("enter your tip percent: 10 ,12,15 ::"))
# # person=int(input("enter how many people split the bill: "))
# #
# # tip_as_percent=tip/100
# # total_bill=bill*tip_as_percent
# # people_split=total_bill/person
# # print(f"your total amount to pay is: {total_bill}Rs. ")
# #
#============Birth Calculator======
# print("hello")
# birth_year=int(input("enter your birth year: "))
# current_year=int(input("enter your current year: "))
# age=current_year - birth_year
# total_days=age*365
# total_months=age*12
# total_week=age*52
# print(age)
# print(f"your total_days: {total_days}, total_months: {total_months}, total_week: {total_week}")

# ==================IF Else ===========
# print("welcome to the rollercoaster!!")
# height=int(input("enter your height:"))
# if height>=120:
#     print("you are able to ride roller-coster")
# else:
#     print("you are not able to ride roller-coster")

# ===================check odd-even number ==========================
# number=int(input("enter Any Type of Number:"))
# if number%2 ==0:
#     print("Number is Even")
# else :
#     print("Number is Odd")
#

print("welcome to the Roller_Coster!!")
height=int(input("enter your Height!!"))

if height < 120:
    print("you are eligible for the ride!!")
    age=int(input("enter your age!!"))
    if age >18:
         print("you should pay 500Rs.")
    else :
         print("you should pay 20Rs.")

else :
     print("you  are not eligible for this ride!!!")