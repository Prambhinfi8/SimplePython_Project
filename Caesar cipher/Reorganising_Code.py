print("Welcome to the Caesar Cipher of Part_1-Encryption Program..")

from art import logo
print(logo)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            end_text +=alphabet[new_position]
        else:
            end_text +=letter

    print(f"the {cipher_direction}d text is {end_text}")

should_continue=True
while should_continue:
    direction=input("Type 'encode' to Encrypt and type 'decode' to Decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the Shift Number:\n"))
    shift= shift%26 # same as shift
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    result=input("Type 'yes' if you want to go  again.Otherwise type 'no'.\n")
    if result=="no":
        should_continue=False
        print("GoodBye..")

