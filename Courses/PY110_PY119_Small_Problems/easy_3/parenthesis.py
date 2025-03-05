"""
Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, 
False otherwise. 
To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

Problem
    input: string
    output: True if there are matching parenthesis, False otherwise

    Rule:
    "What is considered balanced"?
        -Item wrapped by the same number of parenthesis

Algorithm:
    -Implement a counter that increase if it finds a '(' and decreases if it finds a ')'
    -Stop if counter goes negative
"""

def is_balanced(word):
    counter = 0

    for char in word:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1

        if counter < 0:
            return False
    
    return counter == 0

print(is_balanced("What (is) this?") )        # True == True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True