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
        print("Invalid input")

# create a list of play options
t = ["Rock", "Paper", "Scissors", "R", "P", "S"]

# assign a random play to the computer
computer = t[randint(0, 5)]

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

            player = input("Rock, Paper, Scissors? ").capitalize()
            print("Computer:", computer)
            if player == computer:
                print("It's a tie, no one wins this round\n")

            # Player plays rock
            elif player == "Rock" or player == "R":

                # Computer plays paper into rock (player loses round)
                if computer == "Paper" or computer == "P":
                    bot_win_counter += 1
                    print("{} beats rock, you lose (computer has {} points)\n"
                          .format(computer, bot_win_counter))

                # Computer plays scissors into rock and lose (player wins round)
                else:
                    player_win_counter += 1
                    print("You win this round! You have {} points\n".format(player_win_counter))

            # Player plays Paper
            elif player == "Paper" or player == "P":

                # Computer plays scissors into paper (player loses round)
                if computer == "Scissors" or computer == "S":
                    bot_win_counter += 1
                    print("{} beat paper, you lose (computer has {} points)\n"
                          .format(computer, bot_win_counter))

                # Computer plays rock into paper and loses (player wins round)
                else:
                    player_win_counter += 1
                    print("You win this round! You have {} Points\n".format(player_win_counter))

            # Player plays Scissors
            elif player == "Scissors" or player == "S":

                # Computer plays rock into scissors (player loses round)
                if computer == "Rock" or computer == "R":
                    bot_win_counter += 1
                    print("{} beats scissors, you lose (computer has {} points)\n"
                          .format(computer, bot_win_counter))

                # Computer plays paper into scissors and loses (player wins round)
                else:
                    player_win_counter += 1
                    print("You win this round! You have {} points\n".format(player_win_counter))

            # Invalid input error
            else:
                print("Error! Please enter: r, p, s (rock, paper, scissors) ")

            # States winner of game
            if bot_win_counter == first_to_win:
                print("Computer won by {}, you lost".format(bot_win_counter - player_win_counter))
            elif player_win_counter == first_to_win:
                if player_win_counter - bot_win_counter == 1:
                    print("You won by one point")
                else:
                    print("You won by {} points, computer you lost".format(player_win_counter - bot_win_counter))

        # Keeps the loop going until someone reaches the goal
        player = False
        computer = t[randint(0, 5)]

    keep_going = input("\nPush <enter> to play again or any key to stop ")
