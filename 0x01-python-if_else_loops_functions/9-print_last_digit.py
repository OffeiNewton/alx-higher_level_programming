#!/usr/bin/python3

def print_last_digit(number):
    # Get the absolute value of the number
    number = abs(number)

    # Get the last digit
    last_digit = number % 10

    # Print the last digit
    print(last_digit)

    # Return the last digit value
    return last_digit

