"""
Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters 
in the string, and the values represent how often the corresponding letter occurs in the string.
"""

def count_letters(string):
    stripped = ''.join(char.lower() for char in string if char not in '.!/? ')
    return {key: stripped.count(key) for key in stripped}


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)
print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

