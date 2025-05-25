"""
Write a function square_digits that takes an integer and returns an integer where each digit in the original number is squared.

Problem:
    -input: integer
    -output: integer that represent each digit of the original integer squared

Algorithm:
    -Convert number to string
    -Split into digits
    -Loop through them and square each digit
    -conver them back to string and join them
    -Convert the result into an integer
    -Return the final integer

"""

def square_digits(num):
    numbers = "".join([str(int(num) * int(num)) for num in str(num)])

    return int(numbers)

# python

# Example usage:
print(square_digits(9119))  # Should return 811181
# Explanation: 9² = 81, 1² = 1, 1² = 1, 9² = 81

print(square_digits(765) == 493625)  # Should return 493625
# Explanation: 7² = 49, 6² = 36, 5² = 25
