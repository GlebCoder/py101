def prompt(message):
    print(f"==> {message}")

def is_invalid_int(number):
    try:
        number = int(number)
    except ValueError:
        return True
    return number <= 0

def is_invalid_float(number):
    try:
        number = float(number)
    except ValueError:
        return True
    return number <= 0

def get_monthly_payment(loan_amount, months, annual_rate):
    monthly_rate = annual_rate / 100 / 12
    monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** (-months)))
    return monthly_payment

def get_valid_input(msg, validator, error_msg):
    prompt(msg)
    number = input()
    while validator(number):
        prompt(error_msg)
        number = input()
    return number

prompt("Welcome to Mortgage Calculator")
while True:
    loan_amount =float(get_valid_input("Please enter the loan amount",
                                  is_invalid_float,
                                  "You should enter a positive number."))


    months = int(get_valid_input("Please enter a whole number of months for the loan",
                             is_invalid_int,
                             "You should enter a positive whole number."))

    annual_rate = float(get_valid_input("Please enter the annual rate",
                                  is_invalid_float,
                                  "You should enter a positive number."))

    monthly_payment = get_monthly_payment(loan_amount, months, annual_rate)
    prompt(f"Your monthly payment for the loan is: ${monthly_payment:.2f}")

    prompt("Another calculation? Please enter yes or no.")
    answer = input().casefold()
    if not answer or answer[0].casefold() != "y":
        break




