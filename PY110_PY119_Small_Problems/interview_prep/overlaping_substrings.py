"""
Write a function that groups a list of strings into anagrams. Two strings are anagrams if they contain the same characters in a different order.

Algorithm
    -initialize a set to get the unique numbers
    -initialize a max_lenght counter that will keep track of the longest streak of consecutive numbers
    -Loop through the set
    -Test for possible numbers that initiate a sequence
    -initialize a current count to 1 (minimum initial sequence)
    -while loop that checks if the initial number + 1 is in the set
    -For every number found add one to counter and one to max_lenght counter and to current counter
    -update the max-counter to the longest streak
    -return max_counter
"""

def longest_consecutive(lst):
    unique_nums = set(lst)
    max_lenght = 1 

    #filter possible initial sequence starters

    for num in unique_nums:
        if num - 1 not in unique_nums:

            current_num = num
            current_len = 1

            while current_num + 1 in unique_nums:
                current_num += 1
                current_len += 1

            max_lenght = max(max_lenght, current_len)
    return max_lenght

    

#print(longest_consecutive([1, 2, 0, 1]))  # Returns 3 (for sequence 0,1,2)

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Returns 4 (for sequence 1,2,3,4)