# Create a program that takes the length of the password
# and generates a random password of the same length.
#
# by JemboDev @ 06.02.21

import string
import random

# Default character pool for pass contains digits
char_pool = []
char_pool.append(string.digits)

length = int(input("Enter password length: "))
while length < 8:
    length = int(input("Must be at least 8!\nEnter password length: "))

letters = input("Want to use letters? y/n\n")
letters = letters.casefold() == "y"
punctuation = input("Want to use special characters? (!@#$%^&*...) y/n\n")
punctuation = punctuation.casefold() == "y"

# Add other characters to the pool if user wants
if letters:
    char_pool.append(string.ascii_letters)
if punctuation:
    char_pool.append(string.punctuation)

password = list()

# Make sure password has all of the selected types of chars
while len(password) < length:
    for category in char_pool:
        password.append(random.choice(category))

random.shuffle(password)
password = "".join(password)

print(f"Here's your new password: {password}")
