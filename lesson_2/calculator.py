# Ask for the first number
# Ask for the second number
# Ask for the operation
# Print the result
import json

def prompt(message):
    print(f"==> {message}")

def invalid_num(num_str):
    try:
        int(num_str)
    except ValueError:
        return True
    return False

with open("config_message_calculator.json", 'r') as f:
    messages = json.load(f)

prompt(messages["welcome"])
prompt(messages["your name"])
name = input()

prompt(f'{messages["hello"]} {name}!')

while True:
    prompt(messages["first number"])
    first_num = input()

    while invalid_num(first_num):
        print(messages["invalid number"])
        first_num = input()

    prompt(messages["second number"])
    second_num = input()

    while invalid_num(second_num):
        print(messages["invalid number"])
        second_num = input()

    prompt(messages["operation"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        print(messages["must choose"])
        operation = input()

    first_num = int(first_num)
    second_num = int(second_num)

    match operation:
        case "1":
            output = first_num + second_num
        case "2":
            output = first_num - second_num
        case "3":
            output = first_num * second_num
        case "4":
            output = first_num / second_num

    print(f'{messages["result"]}: {output}')
    print(messages["continue"])
    answer = input()
    if answer[0].casefold() != "y":
        break