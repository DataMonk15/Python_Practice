import random

# Program for rock paper scissors game

games = ["Rock","Scissors","Paper"]

user_choice = int(input("provide your input 0 for Rock 1 for Scissor 2 for paper\n"))

computer_choice = random.randint(0,2)

if(user_choice < 3):
    print(f"you Choose " + games[user_choice])
    print(f"Computer Choose "+games[computer_choice])

if(user_choice == 2 and computer_choice == 0):
    print("You Win!")
elif(user_choice < computer_choice):
    print("You Win!")
elif(user_choice == computer_choice):
    print("It's a Draw!")
elif(user_choice > 2):
    print("please provide valid input between 0,1,2")
else:
    print("You lose!")




