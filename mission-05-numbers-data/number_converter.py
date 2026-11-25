"""
number_converter.py
-------------------
Asks the user to enter a positive decimal integer, then displays
its binary and hexadecimal equivalents.
"""

decimal_input = input("Enter a positive decimal number: ")

try:
    number = int(decimal_input)
    if number == 0:
        print("Zero is not allowed. Please enter a positive whole number greater than 0.")
    elif number < 0:
        print("Negative numbers are not allowed. Please enter a positive whole number greater than 0.")
    else:
        binary_result = bin(number)
        hex_result = hex(number)
        print(f"Decimal    : {number}")
        print(f"Binary     : {binary_result}")
        print(f"Hexadecimal: {hex_result}")
except ValueError:
    print("Invalid input. Please enter a valid positive whole number.")
