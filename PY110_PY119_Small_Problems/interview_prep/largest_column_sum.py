"""
Write a function that takes a list of lists (representing a table of numbers) and returns the index of the column with the largest sum. If there are multiple columns with the same maximum sum, return the smallest index.

Problem
    -input: a list of lists that compose a matrix
    -output: number of column with the highest vals

Algorithm
    -get the number of columns by the lenght of the first row
    -Initialize a variable for storing the sum of each column
    -Sum the numbers of the columns
    -use the variable with the biggest number to filter the number of the biggest column

"""


def largest_column_sum(matrix):
    col_numbers = len(matrix[0])
    col_sums = [0] * col_numbers

    for row in matrix:
        for idx, val in enumerate(row):
            col_sums[idx] += val

    max_sum = max(col_sums)
    return col_sums.index(max_sum) + 1


table = [
     [1, 3, 5],
     [2, 6, 8],
     [4, 2, 1]
]

print(largest_column_sum(table))