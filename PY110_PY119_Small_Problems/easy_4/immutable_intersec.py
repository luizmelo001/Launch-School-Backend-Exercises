"""
Transform two lists into frozen sets and find their common elements.
"""

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]

def intersection_func(list1, list2):
    return frozenset(list1).intersection(frozenset(list2))

expected_result = frozenset({8})
print(intersection_func(list1, list2) == expected_result) # True