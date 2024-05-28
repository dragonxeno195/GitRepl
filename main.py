import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
lifes = 6
num_of_letters = 0

for letter in chosen_word:
    if letter == guess:
        print(f"The letter {guess} is in the word")
        num_of_letters += 1
    else:
        print("Wrong")

if num_of_letters == 0:
    lifes -= 1
    print(f"You have {lifes} lifes left")

print(f"You have {lifes} lifes left")
