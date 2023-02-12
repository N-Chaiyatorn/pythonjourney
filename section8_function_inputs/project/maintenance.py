alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shifting, alphabet_length = len(alphabet)):
    encoded_message = ""
    # Looping every letter in text.
    for input_letter in message:                             #Maintenance code
        
        # If the letter is in alphabet list, encrypt program is going to encode each letter.
        if input_letter in alphabet:
            input_letter_index = alphabet.index(input_letter)
            lowest_shifting_amount = shifting % alphabet_length
            encode_index = lowest_shifting_amount + input_letter_index
            if encode_index <= 25:
                encoded_message += alphabet[encode_index]
            elif encode_index > 25:
                encode_index = lowest_shifting_amount - (25 - input_letter_index + 1) 
                encoded_message += alphabet[encode_index]
        else:
            encoded_message += input_letter
        
        print(f"The encode text is {encoded_message}")


