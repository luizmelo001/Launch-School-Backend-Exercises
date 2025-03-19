"""
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 
'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

Data Type:
    -Dictionary

Algorithm:
    -Split the text
    -Loop through each word
    -Check if the word matches that dict key
    -If so, replace it with the number
    -join the string
    -Return the result
"""

NUM_DICT = {
    "zero":"0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def word_to_digit(text):
    words_lst = text.split()

    for idx, word in enumerate(words_lst):
        if word in NUM_DICT.keys():
            words_lst[idx] = NUM_DICT[word]
            
    return " ".join(words_lst)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4") 
# Should print True

