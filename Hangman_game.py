print("welcome to the Hangman Program..")

import random

# Word list to choose from
word_list = ["bhumil", "jay", "jaydip"]
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

# Hangman ASCII stages
stages = [
    """
       _______
      |       |
      |       O
      |      /|\\
      |      / \\
      |
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      /|\\
      |      / 
      |
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      /|\\
      |      
      |
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      /|
      |      
      |
    __|__
    """,
    """
       _______
      |       |
      |       O
      |       |
      |      
      |
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      
      |      
      |
    __|__
    """,
    """
       _______
      |       |
      |       
      |      
      |      
      |
    __|__
    """
]

# Display setup
display = ["_" for _ in chosen_word]
guessed_letters = []

# Game starts
print("Welcome to Hangman!")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue
    else:
        guessed_letters.append(guess)

    # Update display if guess is correct
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong guess! You lost a life. Lives left: {lives}")
        print(stages[6 - lives])  # Show the appropriate hangman stage

    # Show current state of word
    print("Word: " + " ".join(display))

    # Check for win
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You won the game..")

    # Check for loss
    if lives == 0:
        end_of_game = True
        print("You lost! The word was:", chosen_word)
        print(stages[0])  # Final hangman

