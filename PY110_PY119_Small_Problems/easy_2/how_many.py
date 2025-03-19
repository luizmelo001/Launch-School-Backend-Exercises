"""
Write a function that counts the number of occurrences of each element in a given list. 
Once counted, print each element alongside the number of occurrences. 
Consider the words case sensitive e.g. ("suv" != "SUV").

Problem:
    input: list of itens
    output: printed key (item) and value(how many times it appears)

    Rules:
        -case sensitive

Examples

Data Type
    -Dictionary

Algorithm
    -Initialize an empty dictionary
    -Iterate through every element of the list and check if it is in the dictionary
    -If not add 1 to value, if present, add + 1
    -Iterate through the dictionary and print the key value pairs onf the screen
"""

def count_occurrences(items):
    dict = {}

    for item in items:
         item = item.lower()
         dict[item] = dict.setdefault(item, 0) + 1


    for key, val in dict.items():
         print(F"{key} => {val}")

vehicles = ['CAR', 'car', 'truck', 'cAr', 'Suv', 'truck',
            'motorCYCLE', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)