"""
You want to multiply all elements of a list by 2. However, 
the function is not returning the expected result. Explain the bug, and provide a solution.
"""

def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])