"""
Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. 
For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.
If a substring occurs more than once, you should count each occurrence as a separate substring.

Problem:
    input: string of digits
    output: integer that represents the total of even-numbered substrings

    Rules:
        - If a substring occurs more than once, it should be counted

Algorithm
    -Helper function to create substrings
    -Only count the substrings that are even numbers
    -Return the result
"""

def substrings(string):
    #subs = []
    #for i in range(len(string)):
    #    for j in range(i, len(string)):
    #        subs.append(string[i:j+1])
    #return subs

    return [string[i:j+1] for i in range(len(string)) 
             for j in range(i, len(string))]

def even_substrings(string):
    return len([sub for sub in substrings(string) if int(sub) % 2 == 0])


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)