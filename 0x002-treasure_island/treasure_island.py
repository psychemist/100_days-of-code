#!/usr/bin/env python3
'''Treasure Island game'''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Left or Right? ")
if choice1.lower() == "left":
    print("You turn left and keep walking till you reach a river full of whirpools.")
    choice2 = input("Swim or Wait? ")
    if choice2.lower() == "wait":
        print("You wait for 20 minutes before a demigod appears. Choose wisely.")
        print("You must choose between three doors to advance: Blue, Red, or Yellow.")
        choice3 = input("Which door? ")
        if choice3.lower() == "yellow":
            print("You found the Lost Treasure of Killimooin! Great job.")
            print("You win! :)")
        elif choice3.lower == "blue":
            print("There is a great fire behind this door. You are burned alive in one second.")
            print("Game over :(")
        elif choice3.lower == "red":
            print("You find the Curse of Zikavushi. It tears you apart limb by limb.")
            print("Game over :(")
        else:
            print("There are countless horrors behind this door. It was nice knowing you.")
            print("Game over :(")
    else:
        print("You wade into the waters and swim. You are shark food within 3 minutes.")
        print("Game over :(")
else:
    print("You walk 50 paces and fall into a gorge. Skill issue.")
    print("Game over :(")
