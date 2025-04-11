"""
Write a function fibonacci_index_select that accepts a list of elements (of any type) as input. 
The function should return a new list containing only the elements whose indices in the original list correspond to Fibonacci numbers. 
A Fibonacci number is a number in the sequence where each number is the sum of the two preceding ones, starting with 0 and 1 (i.e., 0, 1, 1, 2, 3, 5, 8, 13, 21, ...). 
The function should:
Select elements at indices 0, 1, 1, 2, 3, 5, 8, etc., up to the length of the list.
Not mutate the original list.
Return an empty list if the input list is empty or if no Fibonacci indices exist within its bounds (beyond index 0 or 1).

Problem
    Input: a list of element (integers, strings, etc)
    Ouput: a list containing elements with the same index as the fibonatti sequence

Rules:
    -The list can be of any lenght
    -Indices start at 0
    -If the fibonacci number exceeds the list's lenght, ingnore it

Test Cases
# Test Case 1: Basic list of integers
lst1 = [10, 20, 30, 40, 50, 60, 70]
# Fibonacci indices: 0, 1, 1, 2, 3, 5 (8 is out of bounds)
# Expected: [10, 20, 20, 30, 40, 60]
print(fibonacci_index_select(lst1) == [10, 20, 20, 30, 40, 60])  # True
print(lst1 == [10, 20, 30, 40, 50, 60, 70])                      # True (no mutation)

# Test Case 2: Short list
lst2 = [1, 2, 3]
# Fibonacci indices: 0, 1, 1, 2 (3 is out of bounds)
# Expected: [1, 2, 2, 3]
print(fibonacci_index_select(lst2) == [1, 2, 2, 3])  # True
print(lst2 == [1, 2, 3])                             # True

# Test Case 3: Mixed types
lst3 = ["a", "b", "c", 4, "e", 6, 7, 8]
# Fibonacci indices: 0, 1, 1, 2, 3, 5 (8 is out of bounds)
# Expected: ["a", "b", "b", "c", 4, 6]
print(fibonacci_index_select(lst3) == ["a", "b", "b", "c", 4, 6])  # True
print(lst3 == ["a", "b", "c", 4, "e", 6, 7, 8])                    # True

# Test Case 4: Empty list
lst4 = []
# Fibonacci indices: None applicable
# Expected: []
print(fibonacci_index_select(lst4) == [])  # True
print(lst4 == [])                          # True

# Test Case 5: Single element
lst5 = [42]
# Fibonacci indices: 0 (1 is out of bounds)
# Expected: [42]
print(fibonacci_index_select(lst5) == [42])  # True
print(lst5 == [42])                          # True

Algorithm
    -Generate a fibonacci sequence up to the list lenght
    -Store the values on a list object
    -Loop through the fib sequence up to the lenght of the argument list object
    -Use the indexes of the fib sequence to extract the corresponding values from the list argument
    -return the final lst

"""

def fib_generator(num):
    a = 0
    b = 1
    fib_lst = [0, 1]

    while b <= num:
        c = a + b
        a = b
        b = c
        fib_lst.append(c)
    return fib_lst[:-1]


def fibonacci_index_select(lst):
    if not lst:
        return []
    
    fib_lst = fib_generator(len(lst) - 1) 
    return [lst[idx] for idx in fib_lst]




# Test Case 1: Basic list of integers
lst1 = [10, 20, 30, 40, 50, 60, 70]
# Fibonacci indices: 0, 1, 1, 2, 3, 5 (8 is out of bounds)
# Expected: [10, 20, 20, 30, 40, 60]
print(fibonacci_index_select(lst1) == [10, 20, 20, 30, 40, 60])  # True
print(lst1 == [10, 20, 30, 40, 50, 60, 70])                      # True (no mutation)

# Test Case 2: Short list
lst2 = [1, 2, 3]
# Fibonacci indices: 0, 1, 1, 2 (3 is out of bounds)
# Expected: [1, 2, 2, 3]
print(fibonacci_index_select(lst2) == [1, 2, 2, 3])  # True
print(lst2 == [1, 2, 3])                             # True

# Test Case 3: Mixed types
lst3 = ["a", "b", "c", 4, "e", 6, 7, 8]
# Fibonacci indices: 0, 1, 1, 2, 3, 5 (8 is out of bounds)
# Expected: ["a", "b", "b", "c", 4, 6]
print(fibonacci_index_select(lst3) == ["a", "b", "b", "c", 4, 6])  # True
print(lst3 == ["a", "b", "c", 4, "e", 6, 7, 8])                    # True

# Test Case 4: Empty list
lst4 = []
# Fibonacci indices: None applicable
# Expected: []
print(fibonacci_index_select(lst4) == [])  # True
print(lst4 == [])                          # True

# Test Case 5: Single element
lst5 = [42]
# Fibonacci indices: 0 (1 is out of bounds)
# Expected: [42]
print(fibonacci_index_select(lst5) == [42])  # True
print(lst5 == [42])                          # True