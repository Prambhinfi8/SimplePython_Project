import random

word_list=["bhumil", "jay", "jaydip"]
random_word=random.choice(word_list)

guess=input("Guess a letter:").lower()

for letter in random_word:
    if letter ==guess:
        print("right")
    else:
        print("Wrong")