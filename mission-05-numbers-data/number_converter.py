"""
number_converter.py
-------------------
Asks the user to enter a decimal integer, then displays
its binary and hexadecimal equivalents.
"""

decimal_input = input("Enter a decimal number: ")

try:
    number = int(decimal_input)
    binary_result = bin(number)
    hex_result = hex(number)
    print(f"Decimal   : {number}")
    print(f"Binary    : {binary_result}")
    print(f"Hexadecimal: {hex_result}")
except ValueError:
    print("Please enter a valid whole number.")
