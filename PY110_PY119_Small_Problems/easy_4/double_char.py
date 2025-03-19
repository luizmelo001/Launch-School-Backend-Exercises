"""
Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. 
The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.
"""
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def double_consonants(str):
    result = []

    for char in str:
        if char.lower() in CONSONANTS:
            result.append(char*2)
        else:
            result.append(char)
    return "".join(result)

# All of these examples should print True
print(double_consonants('String') ) #== "SSttrrinngg"
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")