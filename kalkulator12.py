import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
                    filename="calc.log")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def first_input():
    num1
    return num1

def next_input():
    num2
    return num2

while True:
    choice = input(
        "Podaj działanie posługując się odpowiednią liczbą(1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie): ")

    if choice == '1':
        try:
            num1 = float(input("Podaj pierwszy składnik: "))
            num2 = float(input("Podaj drugi składnik: "))
        except ValueError:
            print("Spróbuj ponownie i wpisz liczbę, poprawną liczbę!")
        else:
            print("try again")
            add_result = add(num1, num2)
            logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))
            print(num1, "+", num2, "=", add(num1, num2))
            print(f"Dodaję {num1} oraz {num2} i otrzymuję: {add(num1, num2)}")

    elif choice == '2':
        try:
            num1 = float(input("Podaj pierwszy składnik: "))
            num2 = float(input("Podaj drugi składnik: "))
        except ValueError:
            print("Spróbuj ponownie i wpisz liczbę, poprawną liczbę!")
        else:
            print("try again")
            sub_result = subtract(num1, num2)
            logging.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))
            print(num1, "-", num2, "=", subtract(num1, num2))
            print(f"Odejmuję od {num1} {num2} i otrzymuję: {subtract(num1, num2)}")

    elif choice == '3':
        try:
            num1 = float(input("Podaj pierwszy składnik: "))
            num2 = float(input("Podaj drugi składnik: "))
        except ValueError:
            print("Spróbuj ponownie i wpisz liczbę, poprawną liczbę!")
        else:
            print("try again")
            mul_result = multiply(num1, num2)
            logging.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))
            print(num1, "*", num2, "=", multiply(num1, num2))
            print(f"Mnożę {num1} oraz {num2} i otrzymuję: {multiply(num1, num2)}")

    elif choice == '4':
        # if num2 != 0:
        #     div_result = divide(num1, num2)
        #     logging.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
        #     print(num1, "/", num2, "=", divide(num1, num2))
        #     print(f"Dzielę {num1} przez {num2} i otrzymuję: {round(divide(num1, num2), 2)}")
        # else:
        #     print("Nie można dzielić przez zero!!!")
        try:
            num1 = float(input("Podaj pierwszy składnik: "))
            num2 = float(input("Podaj drugi składnik: "))
        except ValueError:
            print("Spróbuj ponownie i wpisz liczbę, poprawną liczbę!")
        else:
            print("try again")
        try:
            div_result = divide(num1, num2)
            logging.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
            print(num1, "/", num2, "=", divide(num1, num2))
            print(f"Dzielę {num1} przez {num2} i otrzymuję: {round(divide(num1, num2), 2)}")
        except ZeroDivisionError:
            print("Nie można dzielić przez zero!!!")

    next_calculation = input("Czy wykonać następne działanie? (tak/nie): ")
    if next_calculation == "nie":
        break
else:
    logging.info("Nieprawidłowy wpis")