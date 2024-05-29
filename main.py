import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

lifes = 6
num_of_letters = 0

display = []
for _ in chosen_word:
    display.append("_")
    
for postion in range(len(chosen_word)):
    letter = chosen_word[postion]
    if letter == guess:
        display[postion] = letter
    else:
        print("Wrong")

if num_of_letters == 0:
    lifes -= 1
    print(f"You have {lifes} lifes left")

print(f"You have {lifes} lifes left")
