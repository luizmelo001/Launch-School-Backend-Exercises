"""
Write a function that takes a string of digits and returns the appropriate number as an integer. 
You may not use any of the standard conversion functions available in Python, such as int. 
Your function should calculate the result by using the characters in the string.

Problem
    Input:
        -String of numbers

    Output:
        -Integer that represents the string of numbers
        -Account for positive and negative signs

    Rules
        -Do not use int function
        -There will be no invalid characters
        -If there it no sign, return a positive integer

    Questions
        -Do I need to account for negative numbers? YES

Examples
    -See test cases

Data Type
    -Dictionary


Algorithim
    -Define a helper function that:
        -loop through the string of numbers
        -Acess the integer equivalent
        -Multiply the int by 10 elevated by the power of each idx (which represents its decimal place)
        -Return the result
    
    -Define the main function that:
        -Checks for a sign in the beggining of the string
        -If present, convert the string into an integer and turn it into positive or negative, depending on the sign
        -If no sign is present, return the integer as positive

Code
...

"""

def string_to_integer(num):
    DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    result = 0

    for idx, num in enumerate(reversed(num)):
        result += DIGITS[num] * 10**idx

    return result

def string_to_signed_integer(num_str):
    SIGNS = {'+': 1, '-': -1}

    if num_str[0] in SIGNS.keys():
        return (string_to_integer(num_str[1:])) * SIGNS[num_str[0]]
    else:
        return(string_to_integer(num_str))
        

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True 