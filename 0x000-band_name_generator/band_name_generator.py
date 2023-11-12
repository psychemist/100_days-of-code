#!/usr/bin/env python3

# Create greeting
print("Welcome to the Band Name Generator!")
# Ask user for city they grew up in
city = input("What city did you grow up in?\n")
# Ask user for name of a pet
pet = input("What was the name of your first pet?\n")
# Combine name of city and pet and show band name
band_name = f"{city} {pet} Band"
# Ensure input cursor shows on new line
print(f"Your band name could be {band_name}")
