"""
A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits 
occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), 
and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. 
Issue an error message if there is no next featured number.

The largest possible featured number is 9876543201.

Problem
    input: integer
    output: integer that complies to rules

    Rules:
        *odd number that is a multiple of 7, with all of its digits occurring exactly once each

Data Type
    -String
    -Integer
    -List

Algorithm
    -Helper function to check if the number is divisible by 7 and has unique chars
    -While loop that keeps adding to the number 
    -Check to see if the number contains all the digits 0-9, if so, return error msg
    -Check if the num is divisible by 7, if so, return it
    -Keep adding one
"""

def valid(number):
    num_str = sorted(str(number))
    unique = True

    for idx in range (len(num_str) -1):
        if num_str[idx] == num_str[idx + 1]:
            unique = False
    return number % 7 == 0 and number % 2 != 0 and unique

def next_featured(num):
    num = num + 1 if num % 2 == 0 else num + 2
    while num <= 9876543201:
        if valid(num):
            return num
        num += 2
    return "There is no possible number that fulfills those requirements."


print(next_featured(12) == 21)                  # True 
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True 
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True