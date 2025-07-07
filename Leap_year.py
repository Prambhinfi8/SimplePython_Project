print("Welcome to the Leap_year Counter Program..")
year=int(input("please enter year to know ,year is leap year or not:"))
if year%4==0:
  if year%100==0:
      if year%400==0:
          print("your give year is Leap Year")
      else:
          print("your give year is not leap year")
  else:
    print("your given year is not leap year")
else:
 print("plese enter a valid year!!Please try agian,Because your given year is not leap year😊😊")