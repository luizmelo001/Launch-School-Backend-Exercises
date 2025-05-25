"""
Write a function max_non_overlapping_palindromes that finds the maximum number of non-overlapping palindromic substrings in a given string. 
Each character can only be part of one palindrome.

Problem
    -input: string
    -output: integer representing the number of non-overlaping palindromic substrings

Algorithm   
    -Create non overlaping substrings
    -Filter the ones that are palindromes
    -
"""
def is_palindrome(sub):
    return sub == sub[::-1]

def max_non_overlapping_palindromes(string):
    substrings = []

    for i in range(len(string)-1):
        for j in range(i + 1,len(string)):
            sub = string[i:j]
            if is_palindrome(sub):
                substrings.append(sub)

    return substrings

print(max_non_overlapping_palindromes("racecarannakayak"))
# Should return 3
# Explanation: "racecar", "anna", "kayak" are all palindromes that don't overlap