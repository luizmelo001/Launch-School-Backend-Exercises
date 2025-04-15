"""
Create a function that takes a list of integers as an argument. 
Determine and return the index N for which all numbers with an index less than N 
sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.
The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.

Algorithm:
    total_sum = left_sum + right_sum
    -Compute the total sum of all elements in `numbers` and store it as `total_sum`
    -Initialize `left_sum` to 0 to track the sum of elements before the current index
    -For each `index` from 0 to `lenght of numbers -1`
      For each `index` from 0 to `length of numbers - 1`:
         a. Compute `right_sum` as `total_sum - numbers[index] - left_sum` (excludes the current element).
          b. If `left_sum` equals `right_sum`, return `index`.
          c. Add `numbers[index]` to `left_sum` to include the current element for the next iteration.
    - If no index is found, return -1.   
"""

def equal_sum_index(numbers):
    index = 0
    left_sum = 0
    total_sum = sum(numbers)    

    while index < len(numbers) - 1:
         # Right sum is total_sum minus current element and left_sum
        right_sum = total_sum - numbers[index] - left_sum
        if right_sum == left_sum:
            return index
        left_sum += numbers[index]
        index += 1

    return -1


print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)