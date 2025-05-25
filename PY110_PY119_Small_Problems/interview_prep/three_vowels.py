"""
Write a function three_vowels that takes a string and returns all words that contain at least three vowels (a, e, i, o, u). 
Return the words in the same order they appear in the original string.

Problem
    -input: string
    -output: list of words that contain at least 3 vowels

Algorithm
    -Initialize an empty list
    -Split the text into words
    -Loop through each word
    -Loop through each char in word
    -If count of vowels >= 3 append the word to the list
    -Return the final list
"""

def three_vowels(text):
    vowel_words = []
    vowels = 'aeiou'

    for word in text.split():
        vowel_count = sum(1 for char in word.lower() if char in vowels)

        if vowel_count >= 3:
            vowel_words.append(word)

    return vowel_words


# Example usage:
print(three_vowels("The quick brown fox jumps over the lazy dog"))


print(three_vowels("Python programming is beautiful and educational"))
