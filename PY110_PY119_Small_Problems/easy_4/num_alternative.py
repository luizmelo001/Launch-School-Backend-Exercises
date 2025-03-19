"""
You will be given a number and you will need to return it as a string in expanded form
"""

def expanded_form(num):
    if num == 0:  # Handle implicit rule
        return ""
    
    container = []
    place = 0
    while num > 0:
        digit = num % 10  # Get rightmost digit
        if digit != 0:
            container.append(str(digit * (10 ** place)))
        num //= 10  # Remove rightmost digit
        place += 1
    
    return " + ".join(container[::-1])  # Reverse to get highest to lowest