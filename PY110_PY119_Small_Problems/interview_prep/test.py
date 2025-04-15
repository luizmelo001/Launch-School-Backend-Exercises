"""

Write a function sort_by_digit_sum that takes a list of integers and returns a new list sorted 
by the sum of their digits in ascending order. 
If two numbers have the same digit sum, they should maintain their original relative order in the list.

Algorithm:
    -Create helper function that returns the sum of digits
    -Pass it as a function to determine the sorting sequence
"""

def sum_of_digits(num):
    return sum([int(digit) for digit in str(num)])

print(sum_of_digits(13), sum_of_digits(7))

def sort_by_digit_sum(numbers):
    return sorted(numbers, key=sum_of_digits)

# python

# Example usage:
#print(sort_by_digit_sum([13, 20, 7, 45, 91]))  
# Should return [20, 13, 7, 45, 91]
# Explanation: digit sums are 20->2, 7->7, 13->4, 45->9, 91->10, so sorted becomes [20, 13, 7, 45, 91]

