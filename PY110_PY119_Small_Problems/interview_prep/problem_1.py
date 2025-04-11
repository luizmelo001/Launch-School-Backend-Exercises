"""
Write a function custom_reverse that accepts a list of elements (of any type) as input and returns a new list with the elements 
in reverse order. The function must not use the built-in list.reverse() method to achieve this. Additionally:
"""

def custom_reverse(lst):
    return sorted(lst, reverse=True)
    #return [item for item in range(len(lst),0, -1)]

lst1 = [1, 2, 3, 4, 5]
# Expected: [5, 4, 3, 2, 1]
print(custom_reverse(lst1))  # True == [5, 4, 3, 2, 1]