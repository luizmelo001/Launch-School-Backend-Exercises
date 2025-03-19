"""
You will be given a number and you will need to return it as a string in expanded form:

Problem
Given a number, return it as a string in expanded form
- input: integer
- output: string representation of expanded form of number

- explicit rules:
    * all input numbers are whole numbers greater than 0
    * the expanded form for 12 is 10 + 2
- implicit rules:
    * a zero input returns an empty string

  Examples/test cases
    p expanded_form(12) == '10 + 2'
    p expanded_form(42) == '40 + 2'
    p expanded_form(70304) == '70000 + 300 + 4'

Data structure
    input: integer
    intermediate: convert integer to string or maybe array of digits
output: string representation of expanded form of number

Algorithm
    -Use the division and modulo operation to separate the decimal places
"""

def expanded_form(num):
    container = []
    num_str = str(num)[::-1]
    num_len = len(num_str)

    for idx, digit in enumerate(num_str):
        if digit != '0':
            result = int(digit) * (10 ** idx)
            container.append(str(result))

    container = container[::-1]
    return " + ".join(container)

print(expanded_form(12))

