"""
Create a function that takes two string arguments and returns the number of times that the second 
string occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.
You may assume that the second argument is never an empty string.

Problem:
    input: Two strings, str1 (the main string) and str2 (the substring to find).
    output: integer counting how many times str2 appears in str1

Rules:
    -str2 is never empty
    -Overlaping strings don't count

Algorithm
    -Initialize a counter for matches.
    -Use a single loop with an index i to track your position in str1.
    -At each i, check if the substring starting at i matches str2
    -Stop when i + len(str2) would exceed len(str1) to avoid out-of-bounds errors.
"""

def count_substrings(str1, str2):
    counter= 0
    i = 0
    
    while i <= len(str1) - len(str2):
        if str1[i:i + len(str2)] == str2:
            counter += 1
            i += len(str2)
        else:
            i += 1

    return counter



#print(count_substrings('babab', 'bab') ) # == 1
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') ) #== 1