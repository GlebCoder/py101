# Ask for the first number
# Ask for the second number
# Ask for the operation
# Print the result
import json

LANGUAGE = "en"

def prompt(message):
    message = messages(message, LANGUAGE)
    print(f"==> {message}")

def invalid_num(num_str):
    try:
        float(num_str)
    except ValueError:
        return True
    return False

def messages(message, LANGUAGE):
    return MESSAGES[LANGUAGE][message]

with open("config_message_calculator.json", 'r') as f:
   MESSAGES = json.load(f)

prompt("welcome")

prompt("your name")
name = input()

print(f'{messages("hello",  LANGUAGE)} {name}!')

while True:
    prompt("first number")
    first_num = input()

    while invalid_num(first_num):
        prompt("invalid number")
        first_num = input()

    prompt("second number")
    second_num = input()

    while invalid_num(second_num):
        prompt("invalid number")
        second_num = input()

    prompt("operation")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("must choose")
        operation = input()

    first_num = float(first_num)
    second_num = float(second_num)

    match operation:
        case "1":
            output = first_num + second_num
        case "2":
            output = first_num - second_num
        case "3":
            output = first_num * second_num
        case "4":
            output = first_num / second_num

    print(f'{messages("result", LANGUAGE)}: {output}')
    prompt("continue")
    answer = input()
    if answer[0].casefold() != "y":
        break