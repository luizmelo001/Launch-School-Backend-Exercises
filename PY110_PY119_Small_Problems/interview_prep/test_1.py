"""
Write a function count_occurrences that takes a string of text and returns a dictionary where the keys are words and the values 
are dictionaries containing:
1.  'count': the number of times that word appears
2.  'positions': a list of positions (indices) where the word appears in the text
Ignore case and punctuation when counting words.

Algorithm
    -Loop though the words in the original string 
    -Remove punctuation from each word 
    -Check if it is alpha
    -Create an empty dictionary (and structure)
    -Check if the word is in the dictionary
    -If the is not, create the structure 
    -If it is in the dictionary, add to the counter and add the index to the list
    -Return dictionary

"""
import string

def count_occurrences(text):
    dct = {}

    for idx, word in enumerate(text.split()):
        cleaned_word = word.translate(str.maketrans("","", string.punctuation)).lower()

        if cleaned_word not in dct:
            dct[cleaned_word] = {'count': 0, 'positions': []}
        dct[cleaned_word]['count'] += 1
        dct[cleaned_word]['positions'].append(idx)

    return dct
 
text = "The quick brown fox jumps over the lazy dog. The fox is quick!"
print(count_occurrences(text))
# Should return something like:
# {
#   'the': {'count': 3, 'positions': [0, 7, 12]},
#   'quick': {'count': 2, 'positions': [1, 14]},
#   'brown': {'count': 1, 'positions': [2]},
#   'fox': {'count': 2, 'positions': [3, 13]},
#   ...
# }
