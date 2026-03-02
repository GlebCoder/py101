# Ask for the first number
# Ask for the second number
# Ask for the operation
# Print the result

def prompt(message):
    print(f"==> {message}")

def invalid_num(num_str):
    try:
        int(num_str)
    except ValueError:
        return True
    return False

prompt("Welcome to calculator!")
prompt("What is your name?")
name = input()

prompt(f"Hello {name}!")
prompt("What is your first number?")
first_num = input()

while invalid_num(first_num):
    print("Hm-m, it does not look like a number")
    first_num = input()

prompt("What is your second number?")
second_num = input()

while invalid_num(second_num):
    print("Hm-m, it does not look like a number")
    second_num = input()

prompt("What operation you would like to perform?\n"
      "1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

while operation not in ["1", "2", "3", "4"]:
    print("You must choose 1, 2, 3, or 4")
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

print(f"The result is: {output}")