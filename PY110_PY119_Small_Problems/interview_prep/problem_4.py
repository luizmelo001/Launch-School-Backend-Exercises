"""
Create a function that takes a list of integers as an argument and returns a tuple of two numbers 
that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

Problem:
    input: a list
    output: tuple representing the two numbers that a closer together (smaller difference between numbers)

    Rules:
        -If equally close, return the pair that occurs first

Algorithm
    Work with the original list (not sorted) to preserve order.
    Compare all adjacent pairs in the original list.
    Track the smallest difference and the first pair with that difference.


"""

def closest_numbers(lst):
    if len(lst) < 2:
        return None
    min_diff = abs(lst[0] - lst[1])
    result = (lst[0], lst[1])

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            current_diff = abs(lst[i] - lst[j])
            if current_diff < min_diff:
                min_diff = current_diff
                result = (lst[i], lst[j])  # Fixed: use i,j indices

    return result
       
    
print(closest_numbers([5, 25, 15, 11, 20]) ) #== (15, 11)
print(closest_numbers([19, 25, 32, 4, 27, 16]) ) # == (25, 27)
print(closest_numbers([12, 22, 7, 17]) ) # == (12, 7)
