
from datetime import datetime

"""
Write two functions that each take a time of day in 24 hour format,
and return the number of minutes before and after midnight, respectively. 
Both functions should return a value in the range 0 through 1439.

Problem
    -input: string representing time hh:mm
    -output: integer representing the total of minutes
    
    Rules
        -One function for "after midnight" one for "before midnight"
        -If the number of minutes is negative, the time is before midnight
        -If the number of minutes is positive, the time is after midnight
"""

MINUTES_PER_DAY = 1440
MINUTES_PER_HOUR = 60

def time_to_minutes(time):
    hour = int(time[:2])
    minutes = int(time[3:])
    total_minutes = (hour * MINUTES_PER_HOUR) + minutes
    return total_minutes

def after_midnight(time):
    time_in_minutes = time_to_minutes(time)
    return 0 if time_in_minutes == 1440 else time_in_minutes

    
def before_midnight(time):
    time_in_minutes = time_to_minutes(time)
    #Adjust for negative numbers
    result = MINUTES_PER_DAY - time_in_minutes
    return 0 if result == 1440 else result

#print(after_midnight("00:00") == 0)     # True 
#print(before_midnight("00:00") == 0)    # True  
#print(after_midnight("12:34") == 754)   # True
#print(before_midnight("12:34") == 686)  # True
#print(after_midnight("24:00") == 0)     # True  
#print(before_midnight("24:00") == 0)    # True  

time_obj = datetime.strptime("12:34", "%H:%M")
print(time_obj.minute)