# The Goal is to create a command-line game where a user is given a chance
# to choose between rock, paper, and scissors and if the user wins the score is added,
# and at the end when the user finishes the game the score is shown to the user.
#
# by JemboDev @ 05.02.21

import random

user_score = 0
robot_score = 0
num_of_games = 0

while True:
    weapon_dict = {"rock": 1, "paper": 2, "scissors": 3}

    user_choise = input("Select your weapon: ").casefold()
    while user_choise not in weapon_dict:
        print("Choose between rock, paper or scissors")
        user_choise = input("Select your weapon: ").casefold()

    robot_choise = random.choice(list(weapon_dict))

    print(f"\nYour weapon of choise is {user_choise}")
    print(f"Robot's weapon of choise is {robot_choise}\n")

    result = (weapon_dict[user_choise] - weapon_dict[robot_choise]) % len(weapon_dict)

    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("Player wins! +1 point!")
        user_score += 1
    else:
        print("Robot wins!")
        robot_score += 1

    num_of_games += 1

    play_again = input("\nPlay again? Y/N: ").casefold()
    print()

    if play_again == "n":
        print(f"Your score: {user_score}! Win rate is about {(user_score / num_of_games):.2%}")
        print(f"Robot's score: {robot_score}")
        break
