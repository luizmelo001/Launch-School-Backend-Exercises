"""
Write a function flatten_nested_dict that takes a nested dictionary and returns a flat dictionary.
The keys in the flat dictionary should be the paths to each value in the nested dictionary, with keys joined by dots.
"""

def flatten_nested_dict(dct):
    pass

# Example usage:
nested = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "f": 4
        }
    },
    "g": 5
}

flatten_nested_dict(nested)
# Should return: {'a': 1, 'b.c': 2, 'b.d.e': 3, 'b.d.f': 4, 'g': 5}