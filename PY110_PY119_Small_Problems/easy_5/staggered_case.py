"""
Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. 
Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. 
Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between 
upper and lower case.

Algorithm
    -Loop through the string
    -Select even chars that are alpha and make them uppercase
"""

def staggered_case(string):
    new_str = ''

    for idx, char in enumerate(string.lower()):
        if idx % 2 == 0:
            new_str += string[idx].upper()
        else:
            new_str += char
    return new_str

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True