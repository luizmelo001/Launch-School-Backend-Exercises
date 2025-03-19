"""
Write a function that rotates the last count digits of a number. To perform the rotation, 
move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

Algorithm
    -convert the input to string for easier digit manipulation
    -if count is one, return the number (rotating one digit does nothing)
    -Split the digit into two parts:
        *prefix: the digits before the last "count"
        *rotate_group: the digits that will be rotated

    -performa the rotation on "rotate_group"
    -concatenate "prefix" with "rotated_group"
    -convert the result back to int and return it
"""

def rotate_rightmost_digits(number, count):
    if count == 1:
        return number

    str_num = str(number)
    prefix = str_num[:-count]
    rotate_group = str_num[-count:]
    rotated = rotate_group[1:] + rotate_group[0]
    
    return int(prefix + rotated)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True 
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True 
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True