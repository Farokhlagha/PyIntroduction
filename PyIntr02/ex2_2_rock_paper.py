# Rock Paper Scissors Game

import random

cumpoter_score = 0
user_score = 0

while cumpoter_score < 4 and user_score < 4:

    x = random.randint(1, 3)

    if x == 1:
        cumpoter_choice = "rock"
    elif x == 2:
        cumpoter_choice = "paper"
    elif x == 3:
        cumpoter_choice = "scissors"

    user_choise = input("enter your choice (rock, paper, scissors): ")

    if user_choise == cumpoter_choice:
        print("Your choice is like choosing computer!")

    elif (user_choise == "rock" and cumpoter_choice == "paper") or \
        (user_choise == "paper" and cumpoter_choice == "scissors") or\
        (user_choise == "scissors" and cumpoter_choice == "rock"):
        cumpoter_score += 1
        print("💻: " , cumpoter_choice)
        print("👤: " , user_choise)
        print("🧨")

    elif (cumpoter_choice == "rock" and user_choise == "paper") or \
        (cumpoter_choice == "paper" and user_choise == "scissors") or\
        (cumpoter_choice == "scissors" and user_choise == "rock"):
        user_score += 1
        print("💻: " , cumpoter_choice)
        print("👤: " , user_choise)
        print("✨")

    else:
        print("⚠ enter true choice")

if user_score == 4:
    print("you win")
else:
    print("cumpoter win")