"""
Create a function that takes a list of numbers, all of which are the same except one. 
Find and return the number in the list that differs from all the rest.

Problem:
    -input: list of numbers
    -output: number that is differs from the rest of the list

Algorithm:
    -count the number of times that digits appear in the list
    -return the digit that only appears one time
"""

def what_is_different(digits):
    unique_nums = set(digits)

    for num in unique_nums:
        if digits.count(num) == 1:
            return num


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)