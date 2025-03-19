"""
Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or 
lowercase each letter. 
The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

Algorithm
    -Start with empty string to build the result
    -Use a variable to track how many alphabetic characters have been processed
    -Loop through each character in the input string
        *if it's alphabetic and even: uppercase it
        *if alphabetive, but odd: lowercase it
        *increment alpha
"""

def staggered_case(string):
    new_str = ''
    alpha_count = 0

    for char in string:
        if char.isalpha():
            new_str += char.upper() if alpha_count % 2 == 0 else char.lower()
            alpha_count += 1
        else:
            new_str += char

    return new_str
        

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True