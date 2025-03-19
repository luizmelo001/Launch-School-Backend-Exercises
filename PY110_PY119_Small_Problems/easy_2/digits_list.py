"""
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

Problem
    Input: positive integer
    output: list of digits in the number

Algorithm
    -Convert the integer to str and split it
    -return a comprehension
"""

def digit_list(num):
    num_str = str(num)
    return [int(num_str[idx]) for idx in range(len(num_str))]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True  
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True  
print(digit_list(444) == [4, 4, 4])               # True

