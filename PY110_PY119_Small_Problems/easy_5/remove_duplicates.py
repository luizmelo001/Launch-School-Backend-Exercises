"""
Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. 
Return the refined sequence.
"""

def unique_sequence(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    
    return unique

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True  == expected