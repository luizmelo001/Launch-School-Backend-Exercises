"""
Create a function that takes two strings as arguments and returns True if some portion of 
the characters in the first string can be rearranged to match the characters in the second. 
Otherwise, the function should return False.

Algorithm
    -count chars in str1 and str2
    -check if chars in str1 are present in str 2
    -check if the chars in str1 that are in str2 appear at least the same number of times

"""

def unscramble(str1, str2):

    #count chars in str1
    count1 = {key: str1.count(key) for key in str1}

    #count chars in str2
    count2 = {key: str2.count(key) for key in str2}

    # all keys are present and appear enough times to reconstruct str2
    return all([count1.setdefault(key,0) >= val for key, val in count2.items()])
        
    


print(unscramble('ansucchlohlo', 'launchschool') == True) 
print(unscramble('phyarunstole', 'pythonrules') == True)  
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)