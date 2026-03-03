def prompt(message):
    return f"==> {message}"

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
    loan_amount = float(loan_amount)
    loan_duration_months = int(months)
    monthly_rate = float(annual_rate) / 100 / 12
    monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** (-loan_duration_months)))
    return monthly_payment

def get_valid_input(msg, validator, error_msg):
    print(prompt(msg))
    number = input()
    if validator(number):
        while validator(number):
            print(prompt(error_msg))
            number = input()
    return number

print(prompt("Welcome to Mortgage Calculator"))
while True:
    loan_amount = get_valid_input("Please enter the loan amount",
                                  is_invalid_float,
                                  "You should enter a positive number.")


    months = get_valid_input("Please enter a whole number of months for the loan",
                             is_invalid_int,
                             "You should enter a positive whole number.")

    annual_rate = get_valid_input("Please enter the annual rate",
                                  is_invalid_float,
                                  "You should enter a positive number.")

    monthly_payment = get_monthly_payment(loan_amount, months, annual_rate)
    print(prompt(f"Your monthly payment for the loan is: ${monthly_payment:.2f}"))

    print(prompt("Another calculation? Please enter yes or no."))
    answer = input().casefold()
    if answer[0].casefold() != "y":
        break




