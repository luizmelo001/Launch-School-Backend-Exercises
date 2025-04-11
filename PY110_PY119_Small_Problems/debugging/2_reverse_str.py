def reverse_string(string):
    reversed = ""

    for char in string:
        reversed = char + reversed

    return reversed

print(reverse_string("hello") == "olleh")