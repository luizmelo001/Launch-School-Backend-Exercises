"""
Write a function group_anagrams that takes a list of strings and groups them by their anagram status.
Return a dictionary where keys are sorted strings and values are lists of words that are anagrams of each other.

Problem:
    -input: list of words
    -output: dictionary
        *key = sorted word
        *value = list of anagrams

Data Type
    -Dictionary

Algorithm
    -sort the words and add them to the dictionary
    -Create the structure
    -Loop through the words argument, sort each word
    -Check if the word is in the dictinary
    -Add it to the list val
    -Return the dictionary
"""


def group_anagrams(lst):
    dct = {}
    for word in lst:
        anagram = ''.join(sorted(word))
        if anagram not in dct:
            dct[anagram] = []
        dct[anagram].append(word)

    return dct



words = ["listen", "silent", "enlist", "hello", "world", "tac", "cat", "act"]
print(group_anagrams(words))
# Should return:
# {
#   'eilnst': ['listen', 'silent', 'enlist'],
#   'ehllo': ['hello'],
#   'dlorw': ['world'],
#   'act': ['tac', 'cat', 'act']
# }