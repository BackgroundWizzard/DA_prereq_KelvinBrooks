import random
user_choice = input("Please choose rock, paper, or scissors? ")
    if user_choice != ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
    random_number = random.randint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
if user_choice == "rock":
    if random_number ==  [0, 1, 2, 3]:
        computer_choice = "rock":
            print("Computer chose rock! It's a tie!")
    elif random_number == [4, 5, 6]:
        computer_choice = "paper":
            print("Computer chose paper! You lose!")\
    else random_number == [7, 8, 9]:
        computer_choice = "scissors":
            print("Computer chose scissors! You win!")
if user_choice == "paper":
    if random_number ==  [0, 1, 2, 3]:
        computer_choice = "rock":
            print("Computer chose rock! You win!")
    elif random_number == [4, 5, 6]:
        computer_choice = "paper":
            print("Computer chose paper! It's a tie!")
    else random_number == [7, 8, 9]:
        computer_choice = "scissors":
            print("Computer chose scissors! You lose!")
if user_choice == "scissors":
    if random_number ==  [0, 1, 2, 3]:
        computer_choice = "rock":
            print("Computer chose rock! You lose!")
    elif random_number == [4, 5, 6]:
        computer_choice = "paper":
            print("Computer chose paper! You win!")
    else random_number == [7, 8, 9]:
        computer_choice = "scissors":
            print("Computer chose scissors! It's a tie!")
    
    