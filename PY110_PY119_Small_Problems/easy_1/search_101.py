"""
Write a program that solicits six (6) numbers from the user and prints a message that 
describes whether the sixth number appears among the first five.

Algorithm
1. Initialize an empty list to store the first five numbers
2. For i from 1 to 5:
    Prompt user with "Enter the [i]st/nd/rd/th number:"
    Add the input number to the list
3. Prompt user with "Enter the last number:"
4. Store the sixth number
5. Convert the list of first five numbers into a comma-separated string
6. If the sixth number is in the list of first five numbers:
    Print "[sixth number] is in [comma-separated list]."
   Else:
    Print "[sixth number] is not in [comma-separated list]."
"""

numbers = []

for idx in range(1,6):
    match idx:
        case 1:
            suffix = "st"
        case 2:
            suffix = "nd"
        case 3:
            suffix = "rd"
        case _:
            suffix = "th"
    
    print(f"Enter the {idx}{suffix} number:")
    number_input = input()
    numbers.append(number_input)

print("Enter the last number:")
last_num = input()

if last_num in numbers:
    print(f"{last_num} is in {','.join(numbers)}.")
else:
    print(f"{last_num} isn't in {','.join(numbers)}.")


