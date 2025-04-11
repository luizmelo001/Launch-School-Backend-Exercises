"""
Write a function organize_by_tag that takes a list of dictionaries representing articles. 
Each article has a 'title', 'author', and 'tags' (a list of strings).
The function should return a dictionary where the keys are tags and the values are lists of article titles that have that tag.

Problem:
    -input: a list of dictionaries
    -output: a dictionary
        *keys: tags
        *vals: list of articles that contain the tag key

Data Structure:
    -set
    -dictionary
"""

def select_titles(tag, dct_lst):
    return [dct["title"] for dct in dct_lst if tag in dct["tags"]]

def organize_by_tag(lst):
    tags = set()

    for dct in lst:
        for tag in dct["tags"]:
            tags.add(tag)

    return {tag: select_titles(tag, lst) for tag in tags}



# Example usage:
articles = [
    {"title": "Python Tips", "author": "Alice", "tags": ["python", "programming", "tips"]},
    {"title": "Web Development Basics", "author": "Bob", "tags": ["web", "programming"]},
    {"title": "Data Science with Python", "author": "Charlie", "tags": ["python", "data science"]},
    {"title": "Cooking Recipes", "author": "Diana", "tags": ["cooking", "food", "tips"]}
]

# Should return:
expected =  {
   "python": ["Python Tips", "Data Science with Python"],
   "programming": ["Python Tips", "Web Development Basics"],
   "tips": ["Python Tips", "Cooking Recipes"],
   "web": ["Web Development Basics"],
   "data science": ["Data Science with Python"],
   "cooking": ["Cooking Recipes"],
   "food": ["Cooking Recipes"]
 }

print(organize_by_tag(articles) == expected)

