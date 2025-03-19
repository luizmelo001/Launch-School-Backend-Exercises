"""
Write a function that takes two list arguments, each containing a list of numbers, and returns
a new list that contains the product of each pair of numbers from the arguments that have the same index. 
You may assume that the arguments contain the same number of elements.

Problem 
Example
Data Structure

Algorithm
    -iterate through the first list with value and index
    -use the index to acess list 2
    -multiply value on list one by the item on list 2 with the same index
    -return the list
"""

def multiply_list(lst1, lst2):
    #result = []

    #for idx, item in enumerate(list1):
    #    product = item * list2[idx]
    #    result.append(product)

    multiplied = [item1 * item2 for (item1, item2) in zip(list1, list2)]

    return multiplied

list1 = [3, 5, 7]
list2 = [9, 10, 11]

print(multiply_list(list1, list2))