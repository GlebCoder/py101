import random

VALID_CHOICES = ["r", "p", "sc", "l", "sp",
                 "rock", "paper", "scissors", "lizard", "spock"]
COMPUTER_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
WINS_AGAINST = {
                "rock": ["scissors", "lizard"],
                "paper": ["rock", "spock"],
                "scissors": ["paper", "lizard"],
                "spock": ["rock", "scissors"],
                "lizard": ["paper", "spock"],
}

MAP_CHOICES = {
                "r": "rock",
                "p": "paper",
                "sc": "scissors",
                "l": "lizard",
                "sp": "spock",
}
WINS_SCORE = 3

def prompt(message):
    print(f"==> {message}")


def display_valid_choices():
    list_of_valid_choices = []
    for key in MAP_CHOICES:
        choice = f"{MAP_CHOICES[key]}({key})"
        list_of_valid_choices.append(choice)
    prompt(", ".join(list_of_valid_choices))

def find_winner(choice, computer_choice):
    if choice == computer_choice:
        return "tie"

    if computer_choice in WINS_AGAINST[choice]:
        return "you"

    return "computer"

def display_winner(game_result):
    if game_result == "tie":
        prompt("It's a tie!")
    elif game_result == "computer":
        prompt("Computer wins!")
    else:
        prompt("You win!")

prompt(f"We are playing rock, paper, scissors, lizard, or spock!")
prompt("Below the rules:")
for key in WINS_AGAINST:
    print(f"{key.capitalize()}: wins {WINS_AGAINST[key][0]} and {WINS_AGAINST[key][1]}")

while True:
    your_wins = 0
    computer_wins = 0
    while your_wins < WINS_SCORE and computer_wins < WINS_SCORE:
        prompt("Choose one:")
        display_valid_choices()

        choice = input().casefold().strip()

        while choice not in VALID_CHOICES:
            prompt("It's not a valid choice!")
            choice = input().casefold().strip()

        if choice not in COMPUTER_CHOICES:
            choice = MAP_CHOICES[choice]
        computer_choice = random.choice(COMPUTER_CHOICES)

        prompt(f"You chose {choice}, computer chose {computer_choice}")
        game_result = find_winner(choice, computer_choice)
        display_winner(game_result)

        if game_result == "computer":
            computer_wins += 1

        if game_result == "you":
            your_wins += 1

        prompt(f"The game score: your wins {your_wins} and computer wins {computer_wins}")

    if your_wins == WINS_SCORE:
        prompt("Match is over. You win!")
    else:
        prompt("Match is over. Computer wins!")

    prompt(f"Play again? (y/n)")
    answer = input().casefold().strip()
    while not answer or (answer[0] != "y" and answer[0] != "n"):
        prompt("It's not a valid answer! You have to choose 'y' or 'n'")
        answer = input().casefold().strip()

    if answer[0] == "n":
        break




