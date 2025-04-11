"""
Write a function group_by_attributes that takes a list of dictionaries and a list of attribute names. 
The function should return a dictionary where the keys are tuples containing values of the specified attributes, 
and the values are lists of dictionaries that have those attribute values.

Algorithm:
    -First build the tuples that will serve as keys
    -
"""

def group_by_attributes(people, attributes):
    tupples_lst = []

    #Create the tupples
    for dct in people:
        tupples_lst.append((dct[attributes[0]], dct[attributes[1]]))

    return {key: [dct for dct in people if key[0] and key[1] in dct.values()] for key in tupples_lst}

# Example usage:
people = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Boston"},
    {"name": "Charlie", "age": 25, "city": "New York"},
    {"name": "Diana", "age": 30, "city": "Chicago"}
]

print(group_by_attributes(people, ["age", "city"]))
# Should return:
# {
#   (25, 'New York'): [{"name": "Alice", "age": 25, "city": "New York"}, 
#                      {"name": "Charlie", "age": 25, "city": "New York"}],
#   (30, 'Boston'): [{"name": "Bob", "age": 30, "city": "Boston"}],
#   (30, 'Chicago'): [{"name": "Diana", "age": 30, "city": "Chicago"}]
# }
