"""
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither

All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. 
Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

Problem:
    input: string
    output: dictionary with the percentage (represented as a string of a float num) of lower, upper and non alpha chars

    Rules:
        * Each value should be rounded to two decimal points.
    
    Questions:
        *Should spaces be counted?

Algorithm:
    -get the total len of the string
    -check the ord() of each character and see if it in the range for uppercase and lower case
    -count the occurencies of lower, upper an none
    -divide each count (lower, upper and none) by the total len then divide by 100%
    -after getting the values, create a dictionary and set the result as values

ASCII: 65 - 90 (A-Z)
       97 - 122 (a-z)
"""

def letter_percentages(string):
    total_len = len(string)
    lower_count = 0
    upper_count = 0
    neither = 0

    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            upper_count += 1
        elif ord(char) >= 97 and ord(char) <= 122:
            lower_count += 1
        else:
            neither += 1

    neither_percent = (neither / total_len) * 100
    upper_percent = (upper_count / total_len) * 100
    lower_percent = (lower_count / total_len) * 100

    percent_dict = {
        "lowercase": f"{lower_percent:.2f}",
        "uppercase": f"{upper_percent:.2f}",
        "neither": f"{neither_percent:.2f}"
    }

    return percent_dict

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result) # 

#expected_result = {
#    'lowercase': "37.50",
#    'uppercase': "37.50",
#    'neither': "25.00",
#}
#print(letter_percentages('AbCd +Ef') == expected_result)
#
#expected_result = {
#    'lowercase': "0.00",
#    'uppercase': "0.00",
#    'neither': "100.00",
#}
#print(letter_percentages('123') == expected_result)