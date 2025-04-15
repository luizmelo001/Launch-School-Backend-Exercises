"""
Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. 
There will always be exactly one such integer in the input list.

Problem:
    -input: list of integers
    -output: integer that appears an odd number of times

Data Type:
    -List
    -Dictionary

Algorithm
    -create a dictionary that counts the numbers of times the numbers appear in the list
    -filter the val that is odd
    -return the key, representing the number
"""

def odd_fellow(numbers):
    numbers_count = {key: numbers.count(key) for key in numbers}

    for key, val in numbers_count.items():
        if val % 2 != 0:
            return key
        
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)