# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def odd_or_not(n):
    if abs(n) % 2 == 0:
        return False
    else:
        return True

print(odd_or_not(3)) # "3 should return True"
print(odd_or_not(-3)) # "-3 should return True as absolute value is odd"
print(odd_or_not(0))  # "0 should return False"
print(odd_or_not(2))  # "2 should return False"
print(odd_or_not(-2))  # "-2 should return False as absolute value is even"
print(odd_or_not(5))  # "5 should return True"
print(odd_or_not(100))  # "100 should return False"
print(odd_or_not(-99)) # "-99 should return True as absolute value is odd"
    