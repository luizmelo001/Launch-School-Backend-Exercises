"""
Write a function that takes a list of positive integers as input, multiplies all of the integers together, 
divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

Problem:
    input: list of positive integers

    output: string with the valued rounded three decimal places

    Rules:
        *multiplies all of the integers together
        *divides the result by the number of entries in the list

Examples

Data Types:
    -List
    -Float
    -String

Algorithm
    -Initialize a placeholder
    -Iterate through the values in the list
    -Multiply the number by the placeholder and reassign it
    -Return the result of the multiplication divided by the lenght of the list
    -Use a fstring to convert it to string and adjust to 3 decimal places
"""
def multiplicative_average(lst):
    result = 1

    for val in lst:
        result *= val

    return f"{result / len(lst):.3f}"

print(multiplicative_average([3, 5]) == "7.500") 
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")