#!/usr/bin/env python3

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people should split the bill? "))

total_bill = (bill + (tip / 100 * bill)) / people

print(f"Each person should pay: ${round(total_bill, 2)}")
