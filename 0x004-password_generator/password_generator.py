#!/usr/bin/python3
'''Password Generator'''

import random
import string

alphabets = list(string.ascii_letters)
digits = list(string.digits)
syms = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '?']

try:
    print("Welcome to the PyPassword Generator!\n")
    letters = int(input("How many letters would you like in your password?: "))
    numbers = int(input("How many numbers would you like in your password?: "))
    symbols = int(input("How many symbols would you like in your password?: "))
except Exception:
    print("Input must be a valid integer")
    exit(1)

password = []

for letter in range(letters):
    password += random.choice(alphabets)

for number in range(numbers):
    password += random.choice(digits)

for symbol in range(symbols):
    password += random.choice(syms)

random.shuffle(password)
print(f"Here is your password: {''.join(password)}")
