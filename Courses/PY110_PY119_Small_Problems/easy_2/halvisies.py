"""
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. 
Put the first half of the original list elements in the first element of the return value and put the second half in the second element. 
If the original list contains an odd number of elements, place the middle element in the first half list.

Problem
    -Input: list

    -Output: list with two elements (both lists)

    -Rules
        *First half in the first element
        *Second half in the second element

    -Question:
        *Empty lists?
        *Check for non lists?
        *Uneven lists
        *Original list mutated?

Examples

Data Type

Algorithm
    -check the lenght of the original lst
    -divide it by 2 and check if it is integer
    -if integer: slice up to the number +1 (because slicing in non inclusive)
    -if it is a float add one to get the first half and slice it again
    -return both lists

Code
"""

def halvsies(lst):
    idx = (len(lst) + 1) // 2
    half_1 = lst[:idx]
    half_2 = lst[idx:]

    return [half_1, half_2]

print(halvsies([1, 2, 3, 4]) ) == [[1, 2], [3, 4]]
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
