# Yara Volodin 22/112019
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

# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[randint(0, 2)]

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

            # Tie

            player = input("Rock, Paper, Scissors? ").capitalize()
            if player == computer:
                print("It's a tie, no one wins this round\n")

            elif player == "Rock" or "R":
                if computer == "Paper":
                    bot_win_counter += 1
                    print("{} beats {}, you lose (computer has {} points)\n".format(computer, player, bot_win_counter))
                else:
                    player_win_counter += 1
                    print("You win this round! You have {} points\n".format(player_win_counter))

            elif player == "Paper" or "P":
                if computer == "Scissors":
                    bot_win_counter += 1
                    print("{} beat {}, you lose (computer has {} points)\n".format(computer, player, bot_win_counter))
                else:
                    player_win_counter += 1
                    print("You win this round! You have {} Points\n".format(player_win_counter))

            elif player == "Scissors" or "S":
                if computer == "Rock":
                    bot_win_counter += 1
                    print("{} beats rock, you lose (computer has {} points)\n".format(computer, player, bot_win_counter))
                else:
                    player_win_counter += 1
                    print("You win this round! You have {} points\n".format(player_win_counter))

            else:
                print("Error!")

            # Says who won
            if bot_win_counter == first_to_win:
                print("Computer won by {}, you lost".format(bot_win_counter - player_win_counter))
            elif player_win_counter == first_to_win:
                print("You won by {}, you lost".format(player_win_counter - bot_win_counter))

        # Keeps the loop going until someone reaches the goal
        player = False
        computer = t[randint(0, 2)]

    keep_going = input("\nPush <enter> to play again or any key to stop ")
