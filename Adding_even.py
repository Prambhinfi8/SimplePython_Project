print("Welcome to the  Adiding Even number Program..")
total=0
for number in range(0,101,2):
        total +=number
print(f"total sum of even number (using step in range(0,101,2 )is:{total}")

for number in range(0,101):
    if number%2==0:
        total+=number
print("total sum of even number(using %) is :" +str(total))