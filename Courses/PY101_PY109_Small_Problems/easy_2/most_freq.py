
# Create a function to find the most frequent element in a list. 

def most_frequent(lst):
    if not lst:
        return None  # Return None for empty list
    
    #use dictionary to count occurences
    count = {}

    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    #Find the max count
    max_count = max(count.values(), default = 0)

    #iterate through the dictionary and return the item that has the highest value
    for item, freq in count.items():
        if freq == max_count:
            return item


print(most_frequent([1, 2, 3, 2, 1, 2, 3, 2]))
print(most_frequent([1]))
print(most_frequent(['a', 'b', 'c', 'a', 'b', 'a']))