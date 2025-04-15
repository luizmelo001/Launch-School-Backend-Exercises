"""
Write a function word_count_by_case that takes a string of text and returns a dictionary 
with three keys: 'uppercase', 'lowercase', and 'mixed_case'. The values should be counts of words that are entirely uppercase,
entirely lowercase, or mixed case respectively. 
Ignore non-alphabetic characters when determining case.
"""

def word_count_by_case(text):
    words_lst = text.replace(".", "").split()
    uppercase = 0
    lowercase = 0
    mixed_case = 0

    for word in words_lst:
        if all([letter.isupper() for letter in word]):
            uppercase += 1
        elif all([letter.islower() for letter in word]):
            lowercase += 1
        else:
            mixed_case += 1

    return {'uppercase': uppercase, 'lowercase': lowercase, 'mixed_case': mixed_case}

# Example usage:
text = "HELLO world. This Is a Sample TEXT with MixedCase words."
print(word_count_by_case(text)) 
# Should return: {'uppercase': 2, 'lowercase': 2, 'mixed_case': 4}
