# Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.
#Leap year 2: update the function to use the Gregorian calendar (>1752) or the Julian one (<1752)

def is_gregorian(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
       return True
    return False

def is_leap_year(year):
    if year < 1752:
        return year % 4 == 0
    if year >= 1752:
        return is_gregorian(year)
    

print(is_leap_year(1100))

# These examples should all print True

print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)