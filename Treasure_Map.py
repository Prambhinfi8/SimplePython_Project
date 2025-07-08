print("Welcome to the Treasure Map Program..")

row1=["❤️","❤️","❤️"]
row2=["❤️","❤️","❤️"]
row3=["❤️","❤️","❤️"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("where do you want to put the treasure: ")
# position="23"
horizonal=int(position[0]) # "2"
vertical=int(position[1])  # "3"

selected_row=map[horizonal -1]
selected_row[vertical - 1]="😍"

print(f"{row1}\n{row2}\n{row3}\n")
