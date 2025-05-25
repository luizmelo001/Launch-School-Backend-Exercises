"""
Write a function bouncy_count(n) that counts how many “bouncy” numbers exist below a given positive 
integer n (i.e., numbers from 1 to n-1

Define “Bouncy”:
    A number is bouncy if its digits are neither strictly increasing nor strictly decreasing.

    To check if a number is bouncy, examine its digits:
    If there’s both an increase (some digit > previous digit) and a decrease (some digit < previous digit), the number is bouncy.

    Alternatively, a number is not bouncy if it’s either:
    Strictly increasing: Each digit ≥ previous digit.

    Strictly decreasing: Each digit ≤ previous digit.



"""

def is_bouncy(num):
    digits = str(num)

    if len(digits) <= 1:
        return False
    
    #Track if there is an increse or decrease
    has_increase = False
    has_decrease = True

    for i in range(len(digits)-1):
        current = int(digits[i])
        nxt = int(digits[i + 1])

        if current < nxt:
            has_increase = True
        elif current > nxt:
            has_decrease = True

        # If there is both an increase and a decrease, the number is bouncy
        if has_increase and has_decrease:
            return True
    # The number is either increasing or decreasing
    return False

def bouncy_count(num):
    count = 0

    if num < 0:
        return 0
    
    for number in range(1, num):
        if is_bouncy(number):
            count += 1

    return count
        

#bouncy_count(10) # 0
print(bouncy_count(100)) # 36
#bouncy_count(1000) # 525
#bouncy_count(1) # 0
#bouncy_count(10000) # 8586
#bouncy_count(200) # 126

