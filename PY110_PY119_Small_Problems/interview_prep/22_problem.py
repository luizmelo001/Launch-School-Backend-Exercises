"""
Create a function that takes a list of integers as an argument. 
The function should determine the minimum integer value that can be appended to the list so the sum of all the 
elements equal the closest prime number that is greater than the current sum of the numbers. 
For example, the numbers in [1, 2, 3] sum to 6.
The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

Problem:
    -input: list of integers
    -output: single integer
        *sum of all the elements
        *closest prime number 
        *greater than the current sum of the numbers

Algorithm
    -Create a helper function that determines if a number is prime
    -Inside the main function
        *compute the sum o all elements in the lst and store them in `current_sum`
        *Initialize `number_to_add` to 1 to begin the count after the `current_sum`

        While no prime is found:
            *add current_sum to number_to_add
            *check if the result is prime
            *if it is, return `number_to_add`
            *if it is not, add 1 to `number_to_add`
    -Return `number_to_add`
"""

def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def nearest_prime_sum(lst):
    current_sum = sum(lst)
    number_to_add = 1

    while True:
        # start counter after the first number
        candidate = current_sum + number_to_add
        if is_prime(candidate):
            return number_to_add
        number_to_add += 1




print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)