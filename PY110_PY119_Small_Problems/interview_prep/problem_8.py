"""
Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. 
The function should return the length of the longest vowel substring. 
The vowels of interest are "a", "e", "i", "o", and "u".

Problem
    input: non empty string
    output: integer representing the longest vowel substring

    Rules:
        - Vowels "aeiou"
        -lowercase
        -alphabetic

Algorithm
    -Create a variable to store the longest count of vowels
    -Loop through the string and check to see if the char is a vowel
    -Add the vowel to an empty string, check the lenght and update the "longest" variable val
    -Keep going until a non vowerl appears
    -Restart the process until the string ends

"""

def longest_vowel_substring(string):
    longest = 0
    current = 0
    vowels = "aeiou"

    for char in string:
        if char in vowels:
            current += 1
            longest = max(current, longest)
        else:
            current = 0

    return longest



print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)