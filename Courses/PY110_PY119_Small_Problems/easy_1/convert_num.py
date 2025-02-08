"""
Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.
You may not use any of the standard conversion functions available in Python, such as str. 
Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

Problem
    Input:
        -Integer

    Output:
        -String of numbers representing the integer
        -Account for positive and negative signs

    Rules
        -Do not use bult in functions to convert integers to strings
        -There will be no invalid characters
        -If there it no sign, return a positive integer

    Questions
        -Do I need to account for negative numbers? YES

Examples
    -See test cases

Data Type
    -Dictionary


Algorithim


Code
...
"""

def integer_to_string(num):
    DIGITS = {0:"0", 1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
    result = ''

    if num == 0:
        return "0"

    while num > 0:
        result = DIGITS[num % 10] + result
        num //= 10

    return result
 
def signed_integer_to_string(number):
    if number == 0:
        return "0"
    elif number < 0:
        return "-" + integer_to_string(abs(number))
    else:
        return "+" + integer_to_string(number)



print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True