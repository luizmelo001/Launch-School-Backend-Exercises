
def greetings(full_name, info):
    return f"Hello, {" ".join(full_name)}! Nice to have a {info["title"]} {info["occupation"]} around."


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.