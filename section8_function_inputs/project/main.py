alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shifting, alphabet_length = len(alphabet)):
    caesar_coding = ""
    # Looping every letter in text.
    for each_letter in range(len(message)): 
        encrypt_letter = message[each_letter]
        # If the letter is in alphabet list, encrypt program is going to encode each letter.
        if message[each_letter] in alphabet:
            message_index_num = alphabet.index(message[each_letter])
            # Using for loop to figure out the actual index number of encoded letter in list.
            for sequence in range(shifting):
                message_index_num+=1
                # If the index is greater than final index number on the right hand side then return message_index_num into 0.
                if message_index_num == alphabet_length:
                    message_index_num = 0
            encrypt_letter = alphabet[message_index_num]
        
        caesar_coding += encrypt_letter             #The summation of all letters that have been encoded    
    
    print(f"The encode text is {caesar_coding}")

def decrypt(message, shifting, alphabet_length = len(alphabet)):
    caesar_coding = ""
    # Looping every letter in text.
    for each_letter in range(len(message)):
        decrypt_letter = message[each_letter]
        # If the letter is in alphabet list, decrypt program is going to decode each letter.
        if message[each_letter] in alphabet:
            message_index_num = alphabet.index(message[each_letter])
            # Using for loop to figure out the actual index number of decoded letter in list.
            for sequence in range(shifting):
                message_index_num-=1
                # If the index is lower than final index on the left hand side then return message_index_num into the hightest index in list.
                if message_index_num == -alphabet_length-1:
                    message_index_num = alphabet_length - 1
        
            decrypt_letter = alphabet[message_index_num]
            
        caesar_coding+=decrypt_letter                  #The summation of all letters that have been decoded    
    
    print(f"The decode text is {caesar_coding}")

def caesar(message, shifting , direction_text):
    
    if direction == "encode":
        encrypt(message, shifting)
    elif direction == "decode":
        decrypt(message, shifting)
    else:
        print("Error!! It's seems you didn't type the correct order, Please try again!!!")


from art import logo

print(logo)
iscontinous = "yes"
while iscontinous == "yes":

    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, shifting=shift, direction_text=direction)
    iscontinous = input("Do you want to try again? If you want please type 'yes' otherwise please type 'no' : ")