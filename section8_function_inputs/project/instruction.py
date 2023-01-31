""" part 1 encryption """
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


""" part 2 decryption """
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
    #Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.


""" part 3 Refactor/Reorganized the code """
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


""" part 4 Improvement / Bonus """
#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet? implement the code to handle it
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 

#TODO-3: What happens if the user enters a number/symbol/space? implement the code to handle it
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "@ 3"
    #end_text = "@ 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program? implement the code to handle it
    #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 