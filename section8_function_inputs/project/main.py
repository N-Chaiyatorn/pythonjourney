alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shifting, alphabet_length = len(alphabet)):
    encoded_message = ""
    # Looping every letter in text.
    for input_letter in message:                             
        
        # If the letter is in alphabet list, encrypt program is going to encode each letter.
        if input_letter in alphabet:
            input_letter_index = alphabet.index(input_letter)
            lowest_shifting_amount = shifting % alphabet_length
            encoded_index = lowest_shifting_amount + input_letter_index
            if encoded_index <= 25:
                encoded_message += alphabet[encoded_index]
            elif encoded_index > 25:
                encoded_index = encoded_index - 26
                encoded_message += alphabet[encoded_index]
        else:
            encoded_message += input_letter
        
    print(f"The encode text is {encoded_message}")

def decrypt(message, shifting, alphabet_length = len(alphabet)):
    
    decoded_message = ""
    for input_letter in message:
        
        if input_letter in alphabet:
            input_letter_index = alphabet.index(input_letter)
            decoded_index = input_letter_index - (shifting % alphabet_length)
            decoded_message += alphabet[decoded_index]
        else:
            decoded_message += input_letter
            
    print(f"The decode text is {decoded_message}")

def caesar(message, shifting , direction_text):
    
    if direction == "encode":
        encrypt(message, shifting)
    elif direction == "decode":
        decrypt(message, shifting)
    else:
        print("Error!! It's seems you didn't type the correct direction, Please try again!!!")


from art import logo

print(logo)
iscontinous = "yes"
while iscontinous == "yes":

    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, shifting=shift, direction_text=direction)
    iscontinous = input("Do you want to try again? If you want please type 'yes' otherwise please type 'no' : ")