"""
This is a guessing game
the computer will ask you if you want to play, until you have played 5 rounds
the computer will pick a random number
if you guess the number right, you get a point
at then end of the 5 rounds, print how many points you have
"""
# pseudocode
""" in this guessing game the computer will be able choose a number with the use of a ran
    and the user will have to guess the number with 5 chances at their disposal, using a 
    the user will be asked for their guess with use of an input statement and
    with the use of print statements, the user will be told they got the answers wrong
    and when they guess the number right they have a point and the point is counted"""


import random
welcome_question = input(
    f"Do you want to play this guessing game (yes/no)").lower()


def guessing_game():
    game_rounds = 0
    user_score = 0
    computer_score = 0
    computer_round = 0
    user_round = 0
    if welcome_question == "yes":
        print(f"Welcome to the guessing game you have five rounds, you are playing against the computer")
        while game_rounds < 5:
            computer_num = random.randint(1, 10)
            user_num = int(input("Guess a number between 1 and 10 here: "))
            if computer_num > user_num:
                computer_score += 1
                computer_round += 1
                print(f"Computer won")
            elif user_num > computer_num:
                user_score += 1
                user_round += 1
                print(f"User won")
            else:
                print(f"It's a tie!!")
            game_rounds += 1
            print(f"\nThis is your attempt {game_rounds} number")
            # printing results
            print(f"Printing game results...:")
            print(f"Your score is {user_score}, You won {user_round} rounds")
            print(f"Computer score is {computer_score}, Computer won {
                  computer_round} rounds")
    else:
        print(f"Adios")


guessing_game()
