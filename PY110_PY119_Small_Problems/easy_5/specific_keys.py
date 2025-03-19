"""
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.
"""

def  keep_keys(my_dict, keys):
    return { key:val for key, val in my_dict.items() if key in keys}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

print(keep_keys(input_dict, keys) == expected_dict) # True