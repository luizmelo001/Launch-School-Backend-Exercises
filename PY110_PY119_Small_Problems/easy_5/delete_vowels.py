"""
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.
"""

def remove_vowels(lst):
    result = []

    for strg in lst:
        tmp_str = ""
        for char in strg:
            if char not in "AEIOUaeiou":
                tmp_str += char
        result.append(tmp_str)
    return result


original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True 


original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True 

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True 