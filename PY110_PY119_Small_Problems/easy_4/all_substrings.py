"""
Write a function that returns a list of all substrings of a string. Order the returned list 
by where in the string the substring begins. 
This means that all substrings that start at index position 0 should come first,
then all substrings that start at index position 1, and so on.
Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

Problem:
    input: string
    output: list of all substrings

    Rules:
        -return the substrings at a given index from shortest to longest

Examples:

Data Type:
    -Lists

Algorithm
    -Use function that extracts the substrings
    -Iterate through the string and pass each substring to the function
    -Store the lists of substrings
    -Return a joint list of all substrings
"""

def leading_substrings(str):
    str_len = len(str)
    return [str[:idx + 1] for idx in range(str_len)]

def substrings(str):
    # return the substrings
    return [substring for idx in range(len(str))
                for substring in leading_substrings(str[idx:])]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') ) #== expected_result

