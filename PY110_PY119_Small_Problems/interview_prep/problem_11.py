"""
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. 
 If we call the string argument s, the string component of the returned tuple t, 
 and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. 
 The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

 Problem
    input: string
    output: tuple representing the substring and an integer that, when multiplied by the substring equals the original string


Algorithm
    -Loop through the whole string, in order to create all possible substrings
    -For each substring, mutiply from 1 up to the string lenght and mutiply it by the substring created
    -Check if the substring multipled by the numbers in the range up to the string len equals the string
    -Return the substring and the integers representing the number of multiplications
    -Default Case: If no repetition is found, return the full string with k = 1

    1. Measure the total length of the string (call it n).
    2. Try cutting the string into pieces of length 1, 2, 3, up to n:
        - For each piece length (call it l), grab the substring from the start of the string up to l.
        - Figure out how many times this piece would need to repeat to match the total length (k = n / l).
        - Only proceed if k is a whole number (i.e., l divides n evenly).
    3. Test if repeating that piece k times rebuilds the original string.
    4. As soon as you find a match, stop and return the piece and how many times it repeats (t, k).
    5. If no smaller piece works, return the whole string with a repeat count of 1.
"""

def repeated_substring(string):
    n = len(string)

    for l in range(1, n + 1):
        if n % l == 0:
            sub = string[:l]
            times = n // l # checks how many times it needs to be repeated
            if sub * times == string:
                return (sub, times)
                
    return (string, 1)  # Default case: the whole string repeated once

print(repeated_substring('xyzxyzxyz')) #  == ('xyz', 3)
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))  # True
print(repeated_substring('xyxy') == ('xy', 2))        # True
print(repeated_substring('xyz') == ('xyz', 1))        # True
print(repeated_substring('aaaaaaaa') == ('a', 8))     # True
print(repeated_substring('superduper') == ('superduper', 1))  # True

