"""
Write a function transform_scores that takes a list of student score dictionaries and returns a new dictionary where the keys 
are subject names and the values are dictionaries containing the highest, lowest, and average scores for that subject.

Problem:
    input: list
    output: dictionary
        key: subject name 
        value: dictionary containing highest, average and lowest scores

Algorithm:
    -Create helper function to get the scores
    -Helper function to get the highest, the lowest and average scores
    -Main function that:
        -Select the subjects
        -Extracts the scores
        -create the final dictionary with the corresponding values
    -Return the final result#
"""

def get_scores(subject, scores):
    """Helper function to collect all scores for a subject."""
    return [dct[subject] for dct in scores if subject in dct]

def highest(scores):
    """Helper function to compute the highest score from a list."""
    return max(scores)

def lowest(scores):
    """Helper function to compute the lowest score from a list."""
    return min(scores)

def average(scores):
    """Helper function to compute the average score from a list, rounded to 2 decimal places."""
    return round(sum(scores) / len(scores), 2)

def transform_scores(lst):
    # Step 1: Collect unique subjects
    subjects = set()
    for dct in lst:
        subjects.update(key for key in dct if key != "name")
    
    # Step 2: Build result dictionary
    result = {}
    for subject in subjects:
        scores = get_scores(subject, lst)  # Collect scores once
        if scores:  # Only process if there are scores
            result[subject] = {
                "highest": highest(scores),
                "lowest": lowest(scores),
                "average": average(scores)
            }
    
    return result

#
#def highest(subject, scores):
#    return max([val for dct in scores for key, val in dct.items() if key == subject])
#
#def lowest(subject, scores):
#    return min([val for dct in scores for key, val in dct.items() if key == subject])
#
#def average(subject, scores):
#    scores = [val for dct in scores for key, val in dct.items() if key == subject]
#    return round(sum(scores) / len(scores), 2)
#
#
#def transform_scores(lst):
#    return { 
#       key: {
#        "highest": highest(key, lst), 
#        "lowest": lowest(key, lst), 
#        "average": average(key, lst)
#        } 
#       for dct in lst 
#       for key, val in dct.items() 
#       if key != "name"
#       }


# Example usage:
scores = [
    {"name": "Alice", "math": 92, "science": 88, "history": 75},
    {"name": "Bob", "math": 78, "science": 93, "history": 82},
    {"name": "Charlie", "math": 85, "science": 81, "history": 90}
]


expected = {
   "math": {"highest": 92, "lowest": 78, "average": 85.0},
   "science": {"highest": 93, "lowest": 81, "average": 87.33},
   "history": {"highest": 90, "lowest": 75, "average": 82.33}
 }

print(transform_scores(scores)) # == expected
