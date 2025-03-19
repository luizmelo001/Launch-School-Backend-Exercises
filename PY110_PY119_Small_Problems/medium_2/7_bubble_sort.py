"""
Bubble Sort is one of the simplest sorting algorithms available. It is not an efficient algorithm, so developers rarely use 
it in real code. However, it is an excellent exercise for student developers. In this exercise, you will write a function that 
sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. On each pass, the two values of each pair of consecutive 
elements are compared. If the first value is greater than the second, the two elements are swapped. This process is repeated until a 
complete pass is made without performing any swaps. At that point, the list is completely sorted.

We can stop iterating the first time we make a pass through the list without making any swaps since that means the entire list is sorted.

For further information -- including pseudo-code that demonstrates the algorithm, as well as a minor optimization technique -- 
see the Bubble Sort Wikipedia page.

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. 
The sorting should be done "in-place" -- that is, the function should mutate the list. You may assume that the list contains at least 
two elements.

Algorithm
        -While loop
        -Loop through the array and the indexes 
        -Nested loop to check the position of each item in array
"""

def bubble_sort(lst):
    sorted = False

    while not sorted:
        sorted = True
        end = len(lst) - 1
        for idx in range(end):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                end = idx
                sorted = False




#lst1 = [5, 3]
#bubble_sort(lst1)
#print(lst1 == [3, 5])                   # True
#
#lst2 = [6, 2, 7, 1, 4]
#bubble_sort(lst2)
#print(lst2 == [1, 2, 4, 6, 7])          # True
#
#lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#        'Kim', 'Bonnie']
#bubble_sort(lst3)
#
#expected = ["Alice", "Bonnie", "Kim", "Pete",
#            "Rachel", "Sue", "Tyler"]
#print(lst3 == expected)                 # True