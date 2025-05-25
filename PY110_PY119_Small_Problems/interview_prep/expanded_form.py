"""
Write a function expanded_form that takes a number and returns a string showing the number in expanded form.

Problem:
    -input: integer
    -output: string of numbers in extended form

Algorithm:
    -convert the integer to a string
    -split the string into digits in a list
    -reverse the list
    -loop through the list and use the indexes to square each power of 10
    -Convert the digits into integer to perform the operation
    -Convert the numbers back to string
    -join them with a '+'
"""

def expanded_form(num):
    num_str = list(str(num))[::-1]
    numbers = []

    for idx, digit in enumerate(num_str):
        if digit != "0":
            number = int(digit) * (10**idx)
            numbers.insert(0,str(number))

    return " + ".join(numbers)

# Example usage:
#expanded_form(12)  # Should return "10 + 2"
#expanded_form(42)  # Should return "40 + 2"
expanded_form(70304)  # Should return "70000 + 300 + 4"
