"""
Create a function that takes a list of integers as an argument. The function should return 
the minimum sum of 5 consecutive numbers in the list. 
If the list contains fewer than 5 elements, the function should return None.

Problem:
    input: list of integers
    output: integer representing the minimum sum of 5 consecutive numbers

Examples:
    [1, 2, 3, 4, 5, 6]

    There are 2 possible sequences of 5 numbers:
        [1, 2, 3, 4, 5] = 15
        [2, 3, 4, 5, 6] = 20

        The final result is 15 (which is the smaller number)

    Rules:
        * Return none is len is < 5

Algorithm
    -Return None if len(lst) < 5
    -Use the slice operator to create all the possible combinations of 5 numbers
        * idx + 4 =< len(lst) - 1 
        * idx =< len(lst) - 5 (since ranges are exclusive, we have to subtract one)
        * idx =< len(lst) - 4
        
    -Sum them and add the result to a list
    -Return the smallest value from the list
"""

def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    min_sum = sum(lst[0:5])

    for idx in range(1, len(lst) - 4):
        current_sum = sum(lst[idx:idx+5])
        min_sum = min(min_sum, current_sum)

    return min_sum
    


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]))  == 15
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)