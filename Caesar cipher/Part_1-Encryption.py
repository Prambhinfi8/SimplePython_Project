print("Welcome to the Caesar Cipher of Part_1-Encryption Program..")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
direction=input("Type 'encode' to Encrypt and type 'decode' to Decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the Shift Number:\n"))


def encrypt(plain_text , shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        new_letter =alphabet[new_position]
        cipher_text +=new_letter
    print(f"the encoded message id :{cipher_text}")


encrypt(plain_text=text,shift_amount=shift)


