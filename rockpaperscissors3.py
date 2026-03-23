import random

user_choice = input("Please choose rock, paper, or scissors? ")

if user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice! Please choose rock, paper, or scissors.")

random_number = random.randint(0, 9)

if user_choice == "rock":
    if random_number in [0, 1, 2, 3]:
        computer_choice = "rock"
        print("Computer chose rock! It's a tie!")
    elif random_number in [4, 5, 6]:
        computer_choice = "paper"
        print("Computer chose paper! You lose!")
    elif random_number in [7, 8, 9]:
        computer_choice = "scissors"
        print("Computer chose scissors! You win!")

if user_choice == "paper":
    if random_number in [0, 1, 2, 3]:
        computer_choice = "rock"
        print("Computer chose rock! You win!")
    elif random_number in [4, 5, 6]:
        computer_choice = "paper"
        print("Computer chose paper! It's a tie!")
    elif random_number in [7, 8, 9]:
        computer_choice = "scissors"
        print("Computer chose scissors! You lose!")

if user_choice == "scissors":
    if random_number in [0, 1, 2, 3]:
        computer_choice = "rock"
        print("Computer chose rock! You lose!")
    elif random_number in [4, 5, 6]:
        computer_choice = "paper"
        print("Computer chose paper! You win!")
    elif random_number in [7, 8, 9]:
        computer_choice = "scissors"
        print("Computer chose scissors! It's a tie!")