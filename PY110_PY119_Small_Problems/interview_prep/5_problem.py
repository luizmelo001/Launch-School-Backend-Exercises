"""
Create a function that takes a string argument and returns the character that occurs most often in the string. 
If there are multiple characters with the same greatest frequency, return the one that appears first in the string. 
When counting characters, consider uppercase and lowercase versions to be the same.

Problem:
    -input: string
    -output: string represent the letter that appears most frequently

Rules:
    -return the first on that appears in case there are multiple characters

Algorithm   
    -Use a dictionary to store the keys and the values that represent how many times the char appears
    -loop through the vals and return the key that corresponds to the biggest val
"""

def most_common_char(string):
    lower_str = string.lower().replace(" ", "")
    char_count = {key: lower_str .count(key) for key in lower_str }
    
    biggest = max(char_count.values())

    for key, val in char_count.items():
        if val == biggest:
            return key
    

print(most_common_char('Hello World') == 'l') 
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')
my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')