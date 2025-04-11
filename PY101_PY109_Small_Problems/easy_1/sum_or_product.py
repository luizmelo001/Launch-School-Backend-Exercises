# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

def sum_or_product():
    print("Please enter an integer greater than 0:")
    number = int(input())

    print("Enter 's' to compute the sum, or 'p' to compute the product.")
    choice = input()

    if choice == 's':
        result = sum(range(1, number + 1))
        print(f"The sum of the integers between 1 and {number} is {result}.")            
    elif choice == 'p':
        import math
        result = math.prod(range(1, number + 1))
        print(f"The product of the integers between 1 and {number} is {result}.")
 
sum_or_product()
        
