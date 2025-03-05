"""
1) Write a function that takes a string argument consisting of a first name, a space, and a last name. 
The function should return a new string consisting of the last name, a comma, a space, and the first name.

2) Suppose the named person has one or more middle names? Refactor the current solution so it can accommodate this. 
The middle names should be listed after the first name:
"""

#def swap_name(name):
#    return ", ".join(name.split()[::-1])

def swap_name(name):
    str_len = len(name.split()) -1
    last_name = name.split().pop()
    middle_name = name.split()[:str_len]

    return f"{last_name}, {" ".join(middle_name)}"

print(swap_name('Karl Oskar Henriksson Ragvals') == "Ragvals, Karl Oskar Henriksson")  
