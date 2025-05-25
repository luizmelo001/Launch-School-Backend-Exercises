"""
Write a function that takes a list of words and returns a list of integers representing the count of letters in each word that occupy the same position in the word as they do in the alphabet.

For example, the letter 'a' is at position 1 in the alphabet, 'b' is at position 2, etc.

Problem:
    -input: list of words
    -output: list of integers representing the count of letter that are in the same position in the alphabet as int the given string

Data Type:
    -Dictionary

Algorithm:
    -create a dictionary key letters as keys and their position in the dictionary as val
    -Loop through the string and add the val if the val is equal to the index in the string
    -account for uppercase letters
    -store the results in a list
    -return the list
"""

from string import ascii_lowercase

def alphabet_symmetry(words):
    alphabet = ascii_lowercase
    # Predefined dictionary for alphabet positions
    alpha_vals = {letter: idx + 1 for idx, letter in enumerate(alphabet)}
    result = []
    
    for word in words:
        if not isinstance(word, str):  # Validate input
            result.append(0)  # Or raise an error
            continue
        count = 0
        for idx, char in enumerate(word):
            char = char.lower()
            if char in alpha_vals and alpha_vals[char] == idx + 1:
                count += 1
        result.append(count)
    
    return result

print(alphabet_symmetry(["abode", "ABc", "xyzD"]))