"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character 
in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Problem:
    -input:
    -output:

Examples:
    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Data Type
    -Dictionary    
    -Hash Map

Algorithm
    Objective: create a dinamic window to check substrings
    -Create a dictionary with the count of each letter o 't'
    -Initialize a variable t_count, to store the required minimum lenght of the substrings to be formed
    -Initialize an empty dictionary 'window_count' to serve as a sort of 'conveyor belt' from which we can add and remove items dinamically
    -Initialize variables to track the smallest window
    -Initialize pointers 'start' and 'end' to expand and contract the window
    
    Outer While Loop
    *Initialize a while loop that stops when the point 'end' is greater than the lenght of the string
        -Add the first character to window dct and set it to the count of 1 or add one if it already exists
        -Check if char is in t's dictionary and it's count is similitar to t's
            *if it is, a match is found (update a match counter)

    Inner While Loop (logic for expanding and contracting the window)
        *Condition to stop the for loop the start (left window) must be lower than end (right window) and the matches must contain all chars in t
            -Keep adding chars if the window size is less than the min_len (lenght of t)

            -Shrink window by removing character at the start
            -Logic for when count is too low due to removed item
            -update start pointer
    update end pointer

"""
from collections import Counter


def min_window(s, t):
    pass

print(min_window("ADOBECODEBANC", "ABC"))






"""
Implement a function that takes s and k as input and returns the longest substring with at most k distinct characters.

Use the sliding window technique, maintaining a window with a frequency map (e.g., a dictionary or hash map) to track distinct characters.

Problem:
    -input: s = string, t = integer
    -output: string with at least 't' distinct letters

Rules
    - If multiple substrings have the same maximum length, any one is acceptable
    -Pay attention to edge cases, such as when k is greater than the number of distinct characters in s or when s is empty.
    -Case insensitive

Examples
Example 1:
Input: s = "eceba", k = 2
Output: "ece"

Explanation: The longest substring with at most 2 distinct characters is "ece" (contains 'e' and 'c', length 3). Another valid substring is "eceb", but "ece" is equally valid.


Example 2:
Input: s = "aa", k = 1
Output: "aa"

Explanation: The entire string "aa" has 1 distinct character ('a'), so it is the longest substring.


Example 3:
Input: s = "abc", k = 4
Output: "abc"

Explanation: The string "abc" has 3 distinct characters, which is less than or equal to k = 4, so the entire string is valid.


Example 4:
Input: s = "", k = 1
Output: ""

Explanation: An empty string has 0 distinct characters, so it satisfies k = 1, but the output is an empty string.

Data Type:
    -dictionary
    -hash map

Algorithm
    -initialize dictionary 'window_dct' to keep track of individual chars and their count
    -Initialize 'start' pointer to slide the window
    -Initialize a var to store the longest string
    -Initialize a var to store the index of the longest valid substring

Outer loop:
    -Loop through the chars in the string
    -Add first char to dictionary

    *Shrink window if there are more distinct chars than k


Issues
Expand the window = s[end]

Dictionary update
    -Add chars when they are new
    -Remove chars from dictionary when shrinking the window
    (which is necessary when distinct chars are greater than k)

Tracking the Longest Substring:
    -Compare the current window's lenght to the longest found so far

"""
def longest_sub(s, k):
    # Handle edge cases
    if not s or k == 0:
        return ""
    
    # Convert to lowercase for case insensitivity
    s = s.lower()
    
    # Initialize variables
    window_dct = {}  # Frequency map for characters in the window
    start = 0  # Left pointer
    max_length = 0  # Length of longest valid substring
    max_start = 0  # Start index of longest valid substring
    
    # Iterate with right pointer
    for end in range(len(s)):
        # Add character at end to window
        char = s[end]
        window_dct[char] = window_dct.get(char, 0) + 1
        
        # Shrink window if we have more than k distinct characters
        while len(window_dct) > k:
            left_char = s[start]
            window_dct[left_char] -= 1
            if window_dct[left_char] == 0:
                del window_dct[left_char]
            start += 1
        
        # Update longest substring if current window is longer
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            max_start = start
    
    # Return the longest substring
    return s[max_start:max_start + max_length]

print(longest_sub("eceba", 2)) # ece
