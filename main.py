# Password Generator Project
import random

# Define the possible characters for the password
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

# Welcome message
print("Welcome to the PyPassword Generator!")

# Get the number of each type of character from the user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create a list to store the password components
password_list = []

# Add random letters to the password list
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Easy Level - Order not randomized
easy_password = ''.join(password_list)
print(f"Easy level password: {easy_password}")

# Hard Level - Order of characters randomized
random.shuffle(password_list)
hard_password = ''.join(password_list)
print(f"Hard level password: {hard_password}")
