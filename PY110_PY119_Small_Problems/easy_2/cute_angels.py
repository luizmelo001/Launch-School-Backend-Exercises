"""
Problem:
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns 
a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) 
to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. 
There are 60 minutes in a degree, and 60 seconds in a minute.


    Input:
        -Float: representing an angle between 0 and 360 degrees
    Output:
        -a string representing that angle in degrees, minutes, and seconds

    Rules
        -use a degree symbol (°) to represent degrees
        -a single quote (') to represent minutes
        -double quote (") to represent seconds
        -1 degree = 60 min / 1 min = 60 sec
        -Use the given constant to represent the degree symbol

        Edge cases:
            - round numbers
            - 0
    
    Questions

Examples
    -See test cases

Data Type
    -Integer
    -String

Algorithim
    -Initialize variables for degrees, minutes and seconds
    -set the degree variable to the corresponding integer
    -get the remainder (number after the decimal) and multiply it by 60 to get the minutes
    -get the reaminder of the minutes and multiply it by 60 to get the seconds
    -convert to strin and join the results with the corresponding symbols
Code
...
"""

DEGREE = "\u00B0"

def dms(angle):
    # Handle edge case for exact integers
    if angle.is_integer():
        return f"{angle}{DEGREE}00'00\""

    degree = int(angle)
    minutes = int((angle - degree) * 60)
    minutes_float = (angle - degree) * 60
    seconds = int((minutes_float - minutes) * 60) 
    
    minutes_str = f"{minutes:02d}"
    seconds_str = f"{seconds:02d}"

    return f"{degree}{DEGREE}{minutes_str}'{seconds_str}\""

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")