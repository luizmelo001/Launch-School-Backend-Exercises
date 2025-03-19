"""
Write a function that returns a list of all palindromic substrings of a string. That is, each substring must consist 
of a sequence of characters that reads the same forward and backward. 
The substrings in the returned list should be sorted by their order of appearance in the input string. 
Duplicate substrings should be included multiple times.
You may (and should) use the substrings function you wrote in the previous exercise.
For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 
'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.

Problem
    -input: string
    -output: list of all strings that are palindromes

    Rules:
        -sorted by their order of appearance in the input string
        -Duplicate substrings should be included multiple times
        -You may (and should) use the substrings function you wrote in the previous exercise
        -Case sensitive
        -Single characters are not palindromes

Data Type
    -Lists
        
Algorithm
    -Helper function to check if the str is a palindrome
    -Helper function that returns a list with all the substrings of a give word
"""

def is_palindrome(str):
    return str == str[::-1] and len(str) > 1

def leading_substrings(str):
    str_len = len(str)
    return [str[:idx + 1] for idx in range(str_len)]

def substrings(str):
    # return the substrings
    return [substring for idx in range(len(str))
                for substring in leading_substrings(str[idx:])]

def palindromes(str):
    all_subs = [sub for sub in substrings(str) if is_palindrome(sub)]
    return all_subs


print(palindromes('knitting cassettes'))
print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ]) 