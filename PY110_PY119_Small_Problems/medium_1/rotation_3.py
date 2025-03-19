"""
Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit 
fixed in place and rotate the remaining digits to get 329175. 
Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits 
fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate 
the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. 
You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

Algorithm
   Algorithm for max_rotation(number):
    1. Convert the number to a string to get its length (total digits).
    2. Initialize result as the input number.
    3. Perform the first full rotation: rotate all digits using rotate_rightmost_digits with count = length.
    4. Loop from length-1 down to 2 (inclusive):
        - At each step, fix the first (length - count) digits.
        - Rotate the last 'count' digits of the current result using rotate_rightmost_digits.
        - Update result with the new rotated number.
    5. Return the final result.
"""

def rotate_rightmost_digits(number, count):
    if count == 1:
        return number

    str_num = str(number)
    prefix = str_num[:-count]
    rotate_group = str_num[-count:]
    rotated = rotate_group[1:] + rotate_group[0]
    
    return int(prefix + rotated)

def max_rotation(number):
    str_len = len(str(number))
    result = number

    for idx in range(str_len, 1, -1):
        result = rotate_rightmost_digits(result, idx)
    
    return result


print(max_rotation(735291) )          # True == 321579
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True
#
## Note that the final sequence here is `015`. The leading
## zero gets dropped, though, since we're working with
## an integer.
print(max_rotation(105) == 15)                 # True