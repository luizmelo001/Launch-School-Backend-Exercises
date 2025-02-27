
# Convert this loop into a list comprehension:
numbers = [1, 2, 3, 4, 5]

# Can you generate this output using a nested list comprehension?
# [ [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5] ]

nested = []

for num in numbers:
    temp = []
    for item in range(1,num+1):
        temp.append(item)
    nested.append(temp)

def create_list(num):
    lst = []

    for item in range(1, num + 1):
        lst.append(item)
    return lst

nested = [create_list for num in numbers]

print(nested)