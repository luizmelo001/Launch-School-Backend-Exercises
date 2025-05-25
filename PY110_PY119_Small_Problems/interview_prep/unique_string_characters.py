"""
Write a function unique_string_characters that takes two strings and returns a new string containing 
only the characters that are unique to either string but not both.

Problem:
    -Input: two strings
    -Output: one string that represent the chars that are not present in both string (but unique to one of them)

Algorithm:
    -create two set with unique chars of each string passed as argument
    -Loop though chars in str1 and check if they are not present in set2 (unique chars of str2)
    -If they are also unique to the result list, append it
    -Do the same process with chars in str2
    -join the result and return it
"""

def unique_string_characters(str1, str2):
    set1, set2 = set(str1), set(str2)
    result = []
    
    # Characters unique to str1, in order
    for char in str1:
        if char not in set2 and char not in result:
            result.append(char)
    
    # Characters unique to str2, in order
    for char in str2:
        if char not in set1 and char not in result:
            result.append(char)
    
    return "".join(result)

print(unique_string_characters("xyab", "xzca"))  