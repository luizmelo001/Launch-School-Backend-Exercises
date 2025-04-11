"""
You have a function that should check whether a key exists in a dictionary and returns its value. 
However, it's raising an error. Why is that? How would you fix this code?
"""

def get_key_value(my_dict, key):
    return my_dict.get(key, None)