import random


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

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response")

# player_wins = 0
# computer_wins = 0


def outcomes(user, computer):
    player_wins = 0
    computer_wins = 0

    if user == computer:
        result = "\nDraw\n"

    elif user == "paper" and computer == "rock":
        player_wins += 1
        result = "\nUser Wins     │Player has {} points\n".format(player_wins)

    elif user == "rock" and computer == "scissors":
        player_wins = + 1
        result = "\nUser wins     │Player has {} points\n".format(player_wins)

    elif user == "scissors" and computer == "paper":
        player_wins =+ 1
        result = "\nUser wins     │Player has {} points\n".format(player_wins)

    else:
        computer_wins += 1
        result = "\nUser loses    │Computer has {} points\n".format(computer_wins)
    return result

# list of play choices
game_items = ["rock", "paper", "scissors"]

# set player to False
player = False

# ftw = first to reach 'x' wins, starts a "rounds" loop
# ftw = int_check("First to reach *1 - 10* wins: ", 1, 10)


while player is False:

    # computer range of choices
    computer = random.choice(game_items)

    print(computer)
    user = string_checker("Rock, Paper, Scissors, Shoot! ", game_items)
    print(outcomes(user, computer))
