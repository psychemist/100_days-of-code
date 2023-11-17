#!/usr/bin/env python3
'''Rock x Paper x Scissors Game'''

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

try:
    print('What do you choose?')
    p1 = int(input('Type 0 for Rock, 1 for Paper, or 2 for Scissors: '))
    p2 = random.randrange(0, 3, 1)
except Exception as e:
    print('Choice must be a valid number')
    exit(1)

if (p1 < 0 or p1 > 2):
    print('Choice must be either 0, 1 or 2!')
    exit(1)

hand = {0: rock, 1: paper, 2: scissors}
results = ['Draw', 'You win! :)', 'Computer wins! :(']

print(f'\nYou chose:\n{hand[p1]}')
print(f'\nComputer chose:\n{hand[p2]}')

print(f'\nResult: {results[p1 - p2]}')
