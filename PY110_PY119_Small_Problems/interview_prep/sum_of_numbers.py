"""
Write a function sum_of_numbers that takes a string containing a mix of letters and numbers, 
and returns the sum of all numbers in the string. Consecutive digits should be treated as a single number.

Problem:
    -input: string containing letters and numbers
    -output: sum of numbers in the string

Rules:
    -Consecutive numbers are considered a single number

Data Type:
    -List

Algorithm:
    -Loop through the chars in the string
    -Check if the char is numeric
    -If so concatenate it to an empty string
    -If a char is not numeric, append the current digits to a list and reset the digits variable
        *Make sure the last element if not numeric to ensure the last group of digits is appended to the list
    -Convert the digits in the list to integers and sum them
    -Return the final result
"""

def sum_of_numbers(string):
    digit = ""
    digits =[]
    
    for char in string:
        if char.isdigit():
            digit += char
        else:
            if digit:
                digits.append(int(digit))
            digit = ""

    if digits:
        digits.append(int(digit))


    return sum(digits)


        


print(sum_of_numbers("abc123def456"))  # Should return 579 (123 + 456)