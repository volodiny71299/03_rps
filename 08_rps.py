# Yara Volodin
# Rock paper scissors
from random import randint


# defines int_check so that it only allows whole numbers
def int_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response
            else:
                print("You did not enter a number between {} and {}".format(low, high))
        except ValueError:
            print("Invalid input")


def string_checker(question, to_check):
    valid = False
    while not valid:
        response = input(question).capitalize()
        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        print("Error! Please enter: r, p, s (rock, paper, scissors) ")


def rps_outcome(user, comp):
    if user == comp:
        result = "It's a draw"
    elif user == "paper" and comp == "rock":
        result = "User wins"
    elif user == "scissors" and comp == "paper":
        result = "User wins"
    elif user == "rock" and comp == "scissors":
        result = "User wins"
    else:
        result = "User Loses"

    return result

# **** Main Routine ****

comp_choice1 = "Rock"
comp_choice2 = "Paper"
comp_choice3 = "Scissors"

user_list = ["Rock", "Paper", "Scissors"]

# create a list of play options
# t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = user_list[randint(0, 2)]

# set player to False
player = False

# Start of infinite loop that allows you to keep going or stop after the end of the match
keep_going = ""
while keep_going == "":

    # First to reach a certain amount of wins
    first_to_win = int_check("First to reach 1 - 10 wins: ", 1, 10)

    # sets win counters to 0
    player_win_counter = 0
    bot_win_counter = 0

    # Start of loop that keeps going while (player or computer) wins are less than the goal
    while first_to_win > player_win_counter and first_to_win > bot_win_counter:

        # Start of the game
        while player is False:
            # Tie between user and Computer

            player = string_checker("\nRock, Paper, Scissors? ", user_list)
            print("\nComputer:", computer)

            # if player == computer:
            #     print("It's a tie, no one wins this round\n")

            # Player plays ROCK
            if player == "Rock" or "R":
                if computer == "Paper":
                    bot_win_counter += 1
                    print("Computer won")

                elif computer == "Scissors":
                    player_win_counter += 1
                    print("You won")

                else:
                    print("It's a tie")

            # Player plays PAPER
            elif player == "Paper" or "P":
                if computer == "Scissors":
                    bot_win_counter += 1
                    print("Computer won")

                elif computer == "Rock":
                    player_win_counter += 1
                    print("You won")

                else:
                    print("It's a tie")

            # Player plays SCISSORS
            elif player == "Scissors" or "S":
                if computer == "Rock":
                    bot_win_counter += 1
                    print("Computer won")

                elif computer == "Paper":
                    player_win_counter += 1
                    print("You won")

                else:
                    print("It's a tie")

            # States winner of game
            if bot_win_counter == first_to_win:
                if bot_win_counter == 1:
                    print("Computer won by one point, you lose")
                else:
                    print("Computer won by {} points, you lost".format(bot_win_counter - player_win_counter))
            elif player_win_counter == first_to_win:
                if player_win_counter - bot_win_counter == 1:
                    print("You won by one point")
                else:
                    print("You won by {} points, computer you lost".format(player_win_counter - bot_win_counter))

        # Keeps the loop going until someone reaches the goal
        player = False
        computer = user_list[randint(0, 2)]

    keep_going = input("\nPush <enter> to play again or any key to stop ")
