"""
Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.
You may assume that both input lists are non-empty, and that they have the same number of elements.
Bonus: write is as a comprehension
"""

def inter_leave(lst1, lst2):
    #result = []

    #for idx, num in enumerate(lst1):
    #    result.append(num)
    #    result.append(lst2[idx])

    result = [element for pair in zip(lst1, lst2) for element in pair]
        
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(inter_leave(list1, list2))