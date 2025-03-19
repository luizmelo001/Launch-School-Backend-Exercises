"""
Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an 
argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when 
the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the 
foreseeable future.

hint1: 
Use the datetime.date function to determine whether the 13th of a given month falls on a Friday.

hint2:
Here is one possible algorithm for solving the problem:

Iterate over all the months of the given year.
For each month, get the day that falls on the 13th.
Count the 13ths that fall on a Friday.
Return the count.

Use datetime.date to create a date object for the 13th of each month in the given year.
Use the .weekday() method, where Monday = 0, Tuesday = 1, ..., Friday = 4, ..., Sunday = 6.
Iterate over all 12 months, check if the 13th is a Friday, and increment a counter.
Return the total count.
"""

from datetime import date

def friday_the_13ths(year):
    friday_counter = 0

    for month in range(1, 13):
        # Create date object for the 13th of the month
        day_13 = date(year, month, 13)
        if day_13.weekday() == 4:
            friday_counter += 1
    
    return friday_counter

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True