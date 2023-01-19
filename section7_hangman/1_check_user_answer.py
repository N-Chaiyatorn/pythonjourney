#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = word_list[random.randint(0, 2)]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please type your first letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

correct = 0
amount_of_letters = len(chosen_word)

for letter in range(amount_of_letters):
    if guess == chosen_word[letter]:
        correct+=1

iscorrect = bool(correct)
if iscorrect:
    print(f"You answer is {guess} are correct and {guess} are {correct} in this problem.")
else:
    print("You answer is incorrect! you are going to lose one life.")
