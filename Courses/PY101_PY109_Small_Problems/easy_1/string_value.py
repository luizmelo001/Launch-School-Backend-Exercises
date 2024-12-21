# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

def utf16_value(string):
    total = 0
    for letter in list(string):
        if letter != " ":
            total += ord(letter)
    return total

OMEGA = "\u03A9"
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)