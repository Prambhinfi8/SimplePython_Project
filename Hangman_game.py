print("Welcome to Hangman Program !!")

import random

word_list=["bhumil", "jay","jaydip"]
chosen_word=random.choice(word_list)
print(f"your guesse word is {chosen_word}")

display=[]
for letter in chosen_word:
    display +="_"
print(display)

guess=input("Guess a letter:").lower()

for letter in chosen_word:
    if letter==guess:
    else:
        print("wrong")
