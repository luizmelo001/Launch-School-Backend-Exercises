# Write a function to reverse a string using slicing. 

def reverse_string(test_str):
    return test_str[::-1]


test_strings = [
    "Hello, World!",
    "Python",
    "A man, a plan, a canal: Panama",
    "",
    "12345",
    "a"
]

# Testing the function with the examples
for test_str in test_strings:
    reversed_str = reverse_string(test_str)
    print(f"Original: '{test_str}', Reversed: '{reversed_str}'")