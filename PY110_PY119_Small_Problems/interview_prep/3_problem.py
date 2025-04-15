"""
Create a function that takes a string argument and returns a copy of the string 
with every second character in every third word converted to uppercase. 
Other characters should remain the same.

Porblem:
    input: string
    output: string with every second letter of third word uppercased

Algorithm:
    Split the input string into words.
    Iterate over every third word (index 2, 5, 8, ...).
    Modify that word by capitalizing every second character (0-based index).
    Join the words back into a string.
"""

def to_weird_case(string):
    new_str = []

    for idx1, word in enumerate(string.split()):
        if (idx1 + 1) % 3 == 0:
            tmp = ''
            for idx2, char in enumerate(word):
                if idx2 % 2 != 0:
                    tmp += char.upper()
                else:
                    tmp += char
            new_str.append(tmp)
        else:
            new_str.append(word)
    return ' '.join(new_str)
                

#def to_weird_case(string):
#    words = string.split()
#    for i in range(2, len(words), 3):  # Every third word (0-based index)
#        words[i] = ''.join(c.upper() if j % 2 else c for j, c in enumerate(words[i]))
#    return ' '.join(words)


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) ) # == expected