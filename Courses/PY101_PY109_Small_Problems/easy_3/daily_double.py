#Write a function that takes a string argument and returns a new string that contains 
# the value of the original string with all consecutive duplicate characters collapsed into a single character.

def crunch(string):
    str_lst = list(string)

    if not str_lst:
        return string
    
    unique_char = str_lst.pop(0)
    unique_lst = []
    unique_lst.append(unique_char)

    for char in str_lst:
        if unique_char != char:
            unique_lst.append(char)
            unique_char = char

    return "".join(unique_lst)

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')







print(crunch('abc'))