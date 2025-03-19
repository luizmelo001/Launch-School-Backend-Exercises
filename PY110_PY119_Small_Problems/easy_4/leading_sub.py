"""
Write a function that takes a string argument and returns a list of substrings of that string. 
Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.
"""

def leading_substrings(str):
    str_len = len(str)
    return [str[:idx + 1] for idx in range(str_len)]

print(leading_substrings('abc') == ['a', 'ab', 'abc']) 
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])