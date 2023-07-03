class EncodeAndDecodeMachine():
    def __init__(self):
        pass
    
    def encoding(self, characters, alphabet_list, shifting):
        encoded_password = ""

        for al in characters:
            if al in alphabet_list:
                encoded_password += alphabet_list[(alphabet_list.index(al) + shifting) % len(alphabet_list)]
            else:
                encoded_password += al
            
            if len(encoded_password) == 1:
                encoded_password = encoded_password.upper()

        return encoded_password
        
    def decoding(self, characters, alphabet_list, shifting):
        decoded_password = ''
        for al in characters:
            if al in alphabet_list:
                decoded_password += alphabet_list[(alphabet_list.index(al) - shifting) % len(alphabet_list)]
                
            else:
                decoded_password += al
            
            if len(decoded_password) == 1:
                decoded_password = decoded_password.upper()
       
        return decoded_password

    def print_the_result(self, user):
        if user.purpose == 'e':
            print(f"{user.name}: your password is {user.encoded_password}")
        elif user.purpose == 'd':
            print(f"{user.name}: your password is {user.decoded_password}")



