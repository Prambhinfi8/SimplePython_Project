print("Welcome to the Caesar Cipher of Part_1-Encryption Program..")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
direction=input("Type 'encode' to Encrypt and type 'decode' to Decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the Shift Number:\n"))

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        end_text +=alphabet[new_position]
    print(f"the {cipher_direction}d text is {end_text}")

caesar(start_text=text,shift_amount=shift,cipher_direction=direction)



