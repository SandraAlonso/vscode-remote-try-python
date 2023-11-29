#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# # write 'hello world' to the console
# print("hello world")

# Create a function to perform rock papers scissor game to play against the computer
def game():
    comp_win = 0
    user_win = 0
    import random
    while True:
        print("Enter your choice: \n Rock \n Paper \n Scissors \n Exit Game")
        choice = input("User turn: ").lower()
        while choice not in ['rock', 'paper', 'scissors', 'exit game']:
            choice = input("enter valid input: ").lower()
        if choice == 'exit game':
            break
        print("user choice is: " + choice)
        print("\nNow its computer turn.......")

        # Computer chooses randomly any number among 'rock' , 'paper' and 'scissors'. Using randint method of random module
        comp_choice = random.choice(['rock', 'paper', 'scissors'])

        # looping until comp_choice value is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.choice(['rock', 'paper', 'scissors'])

        print("Computer choice is: " + comp_choice)

        print(choice + " V/s " + comp_choice)

        # condition for winning
        if ((choice == "rock" and comp_choice == "scissors") or (choice == "paper" and comp_choice == "rock") or (
                choice == "scissors" and comp_choice == "paper")):
            print("User wins!!")
            user_win += 1
        else:
            print("Computer wins!!")
            comp_win += 1

    print("User score: " + str(user_win))
    print("Computer score: " + str(comp_win))
    print("")
       
game()