"""
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, 
the time is after midnight. If the number of minutes is negative, the time is before midnight.

Problem
Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). 
Your function should work with any integer input.

    input: integer (minutes)
    output: string in 24-hour format

    Rules
    You may not use Python's datetime module.
    Disregard Daylight Savings and Standard Time and other complications.
    Format hh:mm

Examples

Data Type

Algorithm
    -Extract how many "days" fit within the given minutes by dividing by 1440 (total minutes in a day)
    -Adjust for negative numbers by adding the 1440
    -Extract the hours by geting the left over from the division of the minutes by minutes_in_day
    -Extract the minutes by getting the left-over result from the minutes_in_day buy 60 (minutes_in_hour)

days = 3000 // 1440
hours = (3000 % 1440) / 60 288
minutes = hours % 60

"""

MINUTES_PER_DAY = 1440
MINUTES_PER_HOUR = 60

def time_of_day(minutes):
    minutes_in_day = (minutes % MINUTES_PER_DAY)

    hours = minutes_in_day // MINUTES_PER_HOUR
    minutes = minutes_in_day % MINUTES_PER_HOUR

    return f"{hours:02d}:{minutes:02d}"

print(time_of_day(-686))

#print(time_of_day(0) == "00:00")        
#print(time_of_day(-3) == "23:57")       # True
#print(time_of_day(35) == "00:35")       # True
#print(time_of_day(-1437) == "00:03")    # True 
#print(time_of_day(3000) == "02:00")     # True
#print(time_of_day(800) == "13:20")      # True
#print(time_of_day(-4231) == "01:29")    # True