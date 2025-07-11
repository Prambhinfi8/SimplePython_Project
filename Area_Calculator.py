print("welcome to the Simple Area calculator Program.. ")
import math
def paint_cal(height,weight,coverage):
    print(f"the wall height is {height} and weight is {weight}")
    paint_cal=((height*weight)/coverage)
    total_cost =math.ceil(paint_cal)
    print(f"You'll need {total_cost} cans of paint")
    # total_cost=round(paint_cal)
    # print(f"your final cost is {total_cost}")

test_h=int(input("height of wall:"))
test_w=int(input("weight of wall:"))
cover=5
paint_cal(height=test_h,weight=test_w,coverage=cover)
