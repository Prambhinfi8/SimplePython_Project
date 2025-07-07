print("Welcome to Treasure Island........")
choice=input("your mission to find the treasure in island ,so you wannt to choose a choice,left or right::").lower()
if choice=="left":
    choice_2=input("you want to swim or wait for the next step in entire game environment").lower()
    if choice_2=="wait":
        choice_3=input("which color door you want to choose?yellow ,red ,blue: ").lower()
        if choice_3=="yellow":
            print("you Won the game..")
        elif choice_3=="red":
            print("you lose game..")
        elif choice_3=="blue":
            print("you lose the game..")
        else:
            print("choose  a valid color to further move in the game")
    else :
        print("Game is Over")
else:
    print("Game is Over")