import random

VALID_CHOICES = ["rock", "paper", "scissors"]

def prompt(message):
    print(f"==> {message}")

def game_result(choice, computer_choice):
    if choice == computer_choice:
        prompt("It's a tie!")
    if ((choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")):
        prompt("You win")
    if ((choice == "rock" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "rock")):
        prompt("Computer wins")



prompt(f"We are playing {', '.join(VALID_CHOICES)}!")
while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input().casefold()
    while choice not in VALID_CHOICES:
        prompt("It's not a valid choice!")
        choice = input().casefold()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}")
    game_result(choice, computer_choice)

    prompt(f"Play again? (y/n)")
    answer = input().casefold()
    while True:
        if not answer or (answer[0] != "y" and answer[0] != "n"):
            prompt("It's not a valid answer! You have to choose 'y' or 'n'")
            answer = input().casefold()
        else:
            break
    if answer[0] == "n":
        break




