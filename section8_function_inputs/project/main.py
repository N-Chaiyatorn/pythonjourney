alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shifting):
    encrypt_code = ""
    for each_letter in range(len(message)):
        message_index_num = alphabet.index(text[each_letter])
        alphabet_length = len(alphabet)
        
        for sequence in range(shifting):
            message_index_num+=1
            if message_index_num == alphabet_length:
                message_index_num = 0
        
        encrypt_letter = alphabet[message_index_num]
        encrypt_code += encrypt_letter
    
    print(f"The encode text is {encrypt_code}")

def decrypt(message, shifting):
    decrypt_code = ""
    for each_letter in range(len(message)):
        message_index_num = alphabet.index(text[each_letter])
        alphabet_length = len(alphabet)

        for sequence in range(shifting):
            message_index_num-=1
            if message_index_num == -alphabet_length-1:
                message_index_num = alphabet_length - 1
        
        decrypt_letter = alphabet[message_index_num]
        decrypt_code+=decrypt_letter
    
    print(f"The decode text is {decrypt_code}")

def caesar(message, shifting , direction_text):
    crypt_code = ""
    
    if direction == "encode":
        for each_letter in range(len(message)): 
            encrypt_letter = text[each_letter]
            if text[each_letter] in alphabet:
                message_index_num = alphabet.index(text[each_letter])
                alphabet_length = len(alphabet)
                for sequence in range(shifting):
                    message_index_num+=1
                    if message_index_num == alphabet_length:
                        message_index_num = 0
        
                encrypt_letter = alphabet[message_index_num]
            crypt_code += encrypt_letter
    
        print(f"The encode text is {crypt_code}")
        
    elif direction == "decode":

        for each_letter in range(len(message)):
            decrypt_letter = text[each_letter]
            if text[each_letter] in alphabet:
                message_index_num = alphabet.index(text[each_letter])
                alphabet_length = len(alphabet)
                
                for sequence in range(shifting):
                    message_index_num-=1
                    if message_index_num == -alphabet_length-1:
                        message_index_num = alphabet_length - 1
        
                decrypt_letter = alphabet[message_index_num]
            
            crypt_code+=decrypt_letter
        print(f"The decode text is {crypt_code}")
    
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