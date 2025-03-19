"""
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers 
sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, 
thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
"""

NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

def alphabetic_number_sort(lst):
    #numbers_dict = {NUMBER_WORDS[idx]: number for idx, number in enumerate(lst)}
    #ordered_nums = sorted(NUMBER_WORDS)

    #return [numbers_dict[num] for num in ordered_nums]
    return sorted(lst, key = lambda x: NUMBER_WORDS[x] )

print(alphabetic_number_sort(input_list))
