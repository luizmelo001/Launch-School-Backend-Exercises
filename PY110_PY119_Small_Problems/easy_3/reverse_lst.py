"""
Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. 
The returned object should be the same object used as the argument.

Problem
    -input: list
    -output: list with elements reversed

Rule:
    -Mutate the list
    -Don't use list.reverse / [::-1]

"""

def reverse_list(lst):
    reversed = []
    while lst:
        reversed.append(lst.pop())
    lst.extend(reversed) 
    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result )               # True  == [4, 3, 2, 1]
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True