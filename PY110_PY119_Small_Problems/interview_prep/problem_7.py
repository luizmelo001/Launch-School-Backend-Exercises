"""
Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. 
For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.
If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], 
the function should return 2. The first list contains two complete pairs while
the second has an extra 2 that isn't part of the other two pairs.

Problem:
    input: list of integers
    output: integer representing the the number of identical pairs

    Rules:
        -If the list is empty or contains exactly one value, return 0.
        -Count the pairs and not the extras

Example:
    [2, 2, 2, 2, 2] = 2 pairs + 1 extra (which is not counted)

Algorithm
    -sort the list
    -create a list o nums that appear more than once
    -count the list of numbers that appear more than once and return the result
"""

def pairs(lst):
    if not lst or len(lst) == 1:
        return 0

    unique = set(lst)
    pairs = [lst.count(item) for item in unique if lst.count(item) > 1]

    result = 0

    for item in pairs:
        result += item // 2

    
    return result

# Try to solve it using the Counter collection

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)