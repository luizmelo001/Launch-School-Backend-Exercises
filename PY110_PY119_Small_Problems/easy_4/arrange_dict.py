"""
Given a dictionary, return its keys sorted by the values associated with each key.
"""

def order_by_value(my_dict):
    sorted_by_keys = sorted(my_dict.items(), key=lambda x: x[1])
    
    return [key for key, val in sorted_by_keys]

keys = ['q', 'r', 'p']
my_dict = {'p': 8, 'q': 2, 'r': 6}

print(order_by_value(my_dict) )  # True == keys