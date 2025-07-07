import random
random_number=random.randint(0,1) #for integer and range is [0,1]
# random_number =random.random(0,1)  ------for float and range is [0,1)
if random_number==0:
    print("Head")
else:
    print("Tail")