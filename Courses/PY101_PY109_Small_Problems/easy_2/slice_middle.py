
#Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. 
#If the string has an even length, you should return exactly two characters.

def center_of(string):
    is_even = len(string) % 2 == 0
    center_index = len(string) // 2

    if is_even:
        return string[center_index -1 : center_index + 1]
    else:
        return string[center_index]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True