"""
Write a function word_pattern that takes two strings: a pattern and a string of words. 
The pattern contains only letters from 'a' to 'z'. Each unique letter in the pattern should map to a unique word in the string. 
Return True if the pattern and the string follow this mapping, otherwise return False.

Problem
    -input: string containing a pattern of words
    -output: boolean that checks if the string given follows the pattern

Algorithm
    -Split the string into a list of words
    -Compare the lenght of pattern and the lenght of the words list
    -Use two dictionaries:
        *one maps a letter of a word. Ex: char_to_word = {'a': 'dog'}
        *one maps a word to a letter. Ex: word_to_char = {'dog': 'a'}
    -Use zip(pattern, words) to iterate over the pair of words
    -Check if the char is a key in the dictionary / do the same with the word
    -If they are already a key, compare the vals to the corresponding word and char
    -Return False if any inconsistency is found
    -Return True otherwise

"""

def word_pattern(pattern, string):
    words = string.split()

    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char not in char_to_word and word not in word_to_char:
            char_to_word[char] = word
            word_to_char[word] = char
        elif char_to_word.get(char) != word or word_to_char.get(word) != char:
            return False
    
    return True
    
# Example usage:
print(word_pattern("abba", "dog cat cat dog"))  # True
print(word_pattern("abba", "dog cat fish dog"))  # True
print(word_pattern("aaaa", "dog dog dog dog"))  # True
print(word_pattern("abba", "dog dog dog dog"))  # False
print(word_pattern("abbc", "dog cat cat fish"))  # True
#