"""
Write a function that takes a string as an argument and returns a list that contains every word from the string, 
with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, 
the function should return an empty list.
You may assume that every pair of words in the string will be separated by a single space.
"""

def word_lengths(text = ''):
    return [f"{word} {len(word)}" 
            for word in text.split()] if text else []

words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']

print(word_lengths(words) == expected_result)

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])  