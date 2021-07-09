
# importing required libraries(random)
import random

# Giving user options and taking input 
user_choice = input("Enter a choice (rock, paper, scissors): ")

# storing all possible choices in a list
all_choices = ["rock", "paper", "scissors"]

# using random function to choose a random
# choice from all three for computer 
computer_choice = random.choice(all_choices)

# printing user and computer's choice
print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
 
# using simple if-else statement to compare 
# and generate who is winner
if user_choice == computer_choice:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")