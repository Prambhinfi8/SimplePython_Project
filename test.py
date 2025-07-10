import random

word_list=["Bhumil", "jay", "jaydip"]

chosen_word=random.choice(word_list)
print(f"your chosen word is : {chosen_word}")
display=[]
for _ in range(len(chosen_word)):
    display +="_"
print(display)
guess=input("guess the letter:").lower()

for letter in chosen_word:
    if letter ==guess:
        print("right")
    else :
        print("wrong")