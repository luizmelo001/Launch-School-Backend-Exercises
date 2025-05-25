"""
Write a function pairs that takes a list of values and returns a list of pairs (2-element tuples) 
of elements with matching values. Each element should be used only once.

Problem:
    -input: list of values
    -outup: list of tuples
        *The tuples are comprised of matching values

Algorithm:
    -create a set based on the lst to get the unique values
    -Loop through the list and count the occurrencies of each item
    -If the count is 2, add the pair as a tupple to an empty list
    -return the list of tuples
    -If there are no matches, return the empty list
"""

def pairs(lst):
    unique_items = set(lst)
    result = []

    for item in unique_items:
        if lst.count(item) == 2:
            result.append((item,item))

    return result

# Example usage:
print(pairs([1, 2, 5, 6, 5, 2]))  # Should return [(2, 2), (5, 5)]
print(pairs(['a', 'b', 'c', 'a', 'd', 'c']))  # Should return [('a', 'a'), ('c', 'c')]
print(pairs([1, 2, 3, 4]))  # Should return []
