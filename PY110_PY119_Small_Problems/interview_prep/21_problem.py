"""
Create a function that takes a string argument that consists entirely of numeric digits and computes 
the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

Problem:
    -input: string of digits
    -output: integer representing the sum of the four greatest consecute digits

Algorithm:
    1. Initialize a variable `max_product` to 0 to track the largest product found.
    2. For each starting index `i` from 0 to `length of digits - 4`:
       a. Extract the substring of 4 digits starting at index `i`.
       b. Compute the product of the digits in this substring:
          - Initialize `current_product` to 1.
          - For each character in the substring:
            - Convert the character to an integer and multiply it into `current_product`.
       c. Update `max_product` to the larger of `max_product` and `current_product`.
    3. Return `max_product`.
"""


def greatest_product(digits):
    max_product = 0

    for i in range(0, len(digits) - 3):
        # Get a sequence of 4 digits
        current_sequence = digits[i:i+4]
        
        #cumput the product of the four digits
        current_product = 1
        for digit in current_sequence:
            current_product *= int(digit)
            #Select the max value by updating max_product if current_product is larger
            max_product = max(current_product, max_product)

    return max_product
    

#print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
#print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
#print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6