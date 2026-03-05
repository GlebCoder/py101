import random
import pdb
from pdb import set_trace

VALID_CHOICES = ["r", "p", "sc", "l", "sp"]
WINS_AGAINST = {
                "r": ["sc", "l"],
                "p": ["r", "sp"],
                "sc": ["p", "l"],
                "sp": ["r", "sc"],
                "l": ["r", "sc"],
}

def prompt(message):
    print(f"==> {message}")

def find_winner(choice, computer_choice):
    if choice == computer_choice:
        return "It's a tie"
    if computer_choice in WINS_AGAINST[choice]:
        return "You win"
    return "Computer wins"


prompt(f"We are playing rock, paper, scissors, lizard, or spock!")
while True:
    your_wins = 0
    computer_wins = 0
    #set_trace()
    while your_wins < 3 and computer_wins < 3:
        prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
        choice = input().casefold()
        while choice not in VALID_CHOICES:
            prompt("It's not a valid choice!")
            choice = input().casefold()

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f"You chose {choice}, computer chose {computer_choice}")
        game_result = find_winner(choice, computer_choice)
        prompt(game_result)

        if game_result == "Computer wins":
            computer_wins += 1

        if game_result == "You win":
            your_wins += 1

    if your_wins == 3:
        prompt("Match is over. You win!")
    else:
        prompt("Match is over. Computer wins!")

    prompt(f"Play again? (y/n)")
    answer = input().casefold()
    while not answer or (answer[0] != "y" and answer[0] != "n"):
        prompt("It's not a valid answer! You have to choose 'y' or 'n'")
        answer = input().casefold()

    if answer[0] == "n":
        break




