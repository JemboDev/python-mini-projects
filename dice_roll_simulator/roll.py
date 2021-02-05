# The goal is to create a program that will simulate the roll of dice.
# by JemboDev @ 05.02.21

from random import randint

num_of_dice = int(input("How many dice you want to roll: "))

for die in range(1, num_of_dice + 1):
    print(f"Die {die} rolled {randint(1, 6)}")
