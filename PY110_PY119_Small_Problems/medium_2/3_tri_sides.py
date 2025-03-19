"""
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.

To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length 
of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, 
the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns 
one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'

Algorithm:
    -Helper function to determine if the tringle is valid based on the instructions
        *sort items
        *check if the the first two are greater than the last
    -Isosceles: if any side is different
    -Equilateral: if all sides are the same
    -Scalene: all sides are different


"""

def valid_triangle(sides):
    return ((sides[0] + sides[1]) > sides[2]) and all(side > 0 for side in sides)

def triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    if not valid_triangle(sides):
        return "invalid"
    
    if sides[0] == sides[1] == sides[2]:
        return "equilateral"
    elif sides[0] != sides[1] != sides[2]:
        return "scalene"
    else:
        return "isosceles"

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True